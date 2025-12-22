# backend/app.py
from flask import Flask, request, jsonify, send_file, render_template
import os, io, csv, tempfile, shutil, math, json
from pathlib import Path
from datetime import datetime
import requests
from PIL import Image
import xml.etree.ElementTree as ET
import simplekml
from shapely.geometry import shape, Point, Polygon, mapping
from ultralytics import YOLO
from model_utils import deg2num, num2deg_center, tiles_in_poly, download_tile

# ---------- CONFIG ----------
MODEL_PATH = os.environ.get("MODEL_PATH", "C:/Users/devi.naidu/Desktop/water-detect-web/best.pt")
ZOOM = int(os.environ.get("ZOOM", "18"))   # tile zoom to use
CONF_THRESHOLD = float(os.environ.get("CONF_THRESHOLD", "0.8"))
TILE_SIZE = 512
# ----------------------------

app = Flask(__name__, template_folder="../frontend/templates", static_folder="../frontend/static")

print("Loading model:", MODEL_PATH)
model = YOLO(MODEL_PATH)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/detect', methods=['POST'])
def detect():
    """
    Accepts JSON: { "geojson": {...}, "zoom": 18 }
    Or accepts form field "kml" file via /upload_kml endpoint (see below)
    """
    data = request.get_json()
    if data is None or "geojson" not in data:
        return jsonify({"error": "No geojson provided"}), 400

    geojson = data["geojson"]
    zoom = int(data.get("zoom", ZOOM))
    conf_thresh = float(data.get("conf_threshold", CONF_THRESHOLD))

    # convert to shapely polygon (supports polygon or multipolygon)
    geom = shape(geojson["geometry"]) if "geometry" in geojson else shape(geojson)
    if not isinstance(geom, (Polygon,)):
        # accept multipolygon by taking union
        geom = geom

    # create temp working dir
    workdir = Path(tempfile.mkdtemp(prefix="wdetect_"))
    csv_path = workdir / "detections.csv"
    kml_path = workdir / "detections.kml"
    out_tiles_dir = workdir / "tiles"
    out_tiles_dir.mkdir(exist_ok=True)

    # find tiles whose center falls within polygon
    tiles = tiles_in_poly(geom, zoom)
    print(f"Tiles to process: {len(tiles)} at zoom {zoom}")

    # prepare CSV and KML
    csv_file = open(csv_path, "w", newline="")
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["lat", "lon", "class", "confidence", "tile_x", "tile_y"])

    kml = simplekml.Kml()

    # iterate and detect
    for x, y in tiles:
        latc, lonc = num2deg_center(x, y, zoom)  # center lat lon
        # download tile image
        tile_fname = out_tiles_dir / f"tile_{zoom}_{x}_{y}.jpg"
        img = download_tile(x, y, zoom, tile_fname, size=TILE_SIZE)
        if img is None:
            continue

        # run YOLO inference (Ultralytics)
        results = model(str(tile_fname), verbose=False)
        for box in results[0].boxes:
            cls = int(box.cls[0])
            conf = float(box.conf[0])
            if conf < conf_thresh:
                continue
            class_name = model.names.get(cls, str(cls))
            # store lat/lon of tile center (you could compute bbox center in image -> latlon but keeping tile center is simpler)
            csv_writer.writerow([latc, lonc, class_name, f"{conf:.4f}", x, y])

            p = kml.newpoint(name=f"{class_name} ({conf:.2f})", coords=[(lonc, latc)])
            p.style.labelstyle.color = "ff0000ff"
            p.style.iconstyle.scale = 1.2

    csv_file.close()
    kml.save(str(kml_path))

    # build summary counts
    counts = {}
    with open(csv_path, "r") as f:
        reader = csv.DictReader(f)
        for r in reader:
            counts[r["class"]] = counts.get(r["class"], 0) + 1

    # prepare response: return JSON summary and links to CSV/KML
    # We'll create endpoints to download these single-use files (or just send files directly)
    # Simpler: send files as attachments now as multipart response isn't convenient -> provide download URLs
    # For simplicity we'll return files directly as zip in-memory
    import zipfile
    zip_bytes = io.BytesIO()
    with zipfile.ZipFile(zip_bytes, "w") as zf:
        zf.write(csv_path, arcname="detections.csv")
        zf.write(kml_path, arcname="detections.kml")
    zip_bytes.seek(0)

    # cleanup when response sent? We'll keep the tempdir; user can re-run. (Optional: schedule cleanup)
    resp = app.response_class(zip_bytes.getvalue(), mimetype="application/zip")
    resp.headers.set("Content-Disposition", "attachment", filename="detections.zip")
    # Add summary header for client use
    resp.headers["X-Detection-Summary"] = json.dumps(counts)
    return resp

@app.route('/upload_kml', methods=['POST'])
def upload_kml():
    """
    Upload KML file: extract polygon (or placemarks -> buffer) and run detect similarly.
    """
    if 'kml' not in request.files:
        return jsonify({"error": "no kml file"}), 400
    file = request.files['kml']
    data = file.read()
    # parse kml coordinates to GeoJSON-like polygon extraction (simplified)
    root = ET.fromstring(data)
    ns = {"k": root.tag.split("}")[0].strip("{")}
    coords_nodes = root.findall(".//k:coordinates", ns)
    # build polygon from first coordinates block (if it's area)
    if not coords_nodes:
        return jsonify({"error": "no coordinates found in kml"}), 400

    raw = coords_nodes[0].text.strip()
    pts = []
    for line in raw.split():
        parts = line.split(",")
        if len(parts) >= 2:
            lon = float(parts[0]); lat = float(parts[1])
            pts.append([lon, lat])
    geojson = {"type":"Feature","geometry":{"type":"Polygon","coordinates":[pts]}}
    # reuse detect by sending to /detect logic - just call function directly
    from flask import current_app
    # convert to same format expected: pass geojson
    return detect()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

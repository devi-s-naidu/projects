# backend/model_utils.py
import math, requests
from PIL import Image
from io import BytesIO

def deg2num(lat_deg, lon_deg, zoom):
    lat_rad = math.radians(lat_deg)
    n = 2.0 ** zoom
    xtile = int((lon_deg + 180.0) / 360.0 * n)
    ytile = int((1.0 - math.log(math.tan(lat_rad) + (1/math.cos(lat_rad))) / math.pi) / 2.0 * n)
    return xtile, ytile

def num2deg(x, y, zoom):
    n = 2.0 ** zoom
    lon_deg = x / n * 360.0 - 180.0
    lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * y / n)))
    lat_deg = math.degrees(lat_rad)
    return lat_deg, lon_deg

def num2deg_center(x, y, zoom):
    # compute center of tile x,y
    lat1, lon1 = num2deg(x, y, zoom)           # top-left of tile x,y
    lat2, lon2 = num2deg(x + 1, y + 1, zoom)   # bottom-right of tile x+1,y+1
    center_lat = (lat1 + lat2) / 2.0
    center_lon = (lon1 + lon2) / 2.0
    return center_lat, center_lon

def tiles_in_poly(shapely_poly, zoom):
    # compute min/max tile x,y for bounding box and iterate
    min_lon, min_lat, max_lon, max_lat = shapely_poly.bounds  # shapely bounds returns (minx,miny,maxx,maxy) -> lon,lat
    x_min, y_max = deg2num(min_lat, min_lon, zoom)
    x_max, y_min = deg2num(max_lat, max_lon, zoom)

    # Ensure proper ordering
    x0 = min(x_min, x_max); x1 = max(x_min, x_max)
    y0 = min(y_min, y_max); y1 = max(y_min, y_max)

    tiles = []
    for x in range(x0, x1+1):
        for y in range(y0, y1+1):
            # compute center latlon
            latc, lonc = num2deg_center(x, y, zoom)
            # shapely expects (lon, lat) ordering for Point
            from shapely.geometry import Point
            pt = Point(lonc, latc)
            if shapely_poly.contains(pt) or shapely_poly.touches(pt):
                tiles.append((x, y))
    return tiles

def download_tile(x, y, zoom, out_path=None, size=512):
    # Google tile url (satellite)
    url = f"https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={zoom}"
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200 and len(r.content) > 100:
            img = Image.open(BytesIO(r.content)).convert("RGB")
            if out_path:
                img.save(out_path)
            return img
    except Exception as e:
        print("tile download error:", e)
    return None

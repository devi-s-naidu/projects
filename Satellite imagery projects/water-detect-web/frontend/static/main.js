// ------------------------------
// Status Box Helper
// ------------------------------
const statusBox = document.getElementById("statusBox");

function setStatus(msg, show = true) {
  statusBox.innerText = msg;
  statusBox.style.display = show ? "block" : "none";
}

// ------------------------------
// Map Initialization
// ------------------------------
const map = L.map('map').setView([26.2, 91.7], 8);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  maxZoom: 19
}).addTo(map);

const drawnItems = new L.FeatureGroup();
map.addLayer(drawnItems);

// Add drawing tools
const drawControl = new L.Control.Draw({
  edit: { featureGroup: drawnItems },
  draw: {
    polygon: true,
    rectangle: true,
    circle: false,
    polyline: false,
    marker: false
  }
});
map.addControl(drawControl);

// When a new polygon is drawn
map.on(L.Draw.Event.CREATED, function (e) {
  drawnItems.clearLayers();
  drawnItems.addLayer(e.layer);
});

// ------------------------------
// Handle KML Upload
// ------------------------------
document.getElementById('kmlFile').addEventListener('change', async (ev) => {
  const file = ev.target.files[0];
  if (!file) return;

  setStatus("Reading KML...");

  const text = await file.text();
  const xml = new DOMParser().parseFromString(text, "application/xml");

  // get ALL <coordinates> tags — not only first one
  const coordNodes = xml.getElementsByTagName("coordinates");

  if (!coordNodes || coordNodes.length === 0) {
    alert("No coordinate tags found in KML.");
    setStatus("", false);
    return;
  }

  let allPts = [];

  for (let node of coordNodes) {
    let raw = node.textContent.trim();

    // Cleanup formatting
    raw = raw.replace(/\n/g, " ").replace(/\s+/g, " ");

    // handle multiple rings or multiple polygons in a single KML
    const pts = raw.split(" ").map(s => {
      const parts = s.split(",");
      // longitude, latitude
      return [parseFloat(parts[1]), parseFloat(parts[0])];
    });

    // Valid polygon = at least 3 coordinates
    if (pts.length >= 3) {
      allPts.push(pts);
    }
  }

  if (allPts.length === 0) {
    alert("Invalid polygon or unsupported KML format.");
    setStatus("", false);
    return;
  }

  // Remove old drawings
  drawnItems.clearLayers();

  // Load first polygon (you can later extend to load multiple)
  const polygon = L.polygon(allPts[0]).addTo(drawnItems);
  map.fitBounds(polygon.getBounds());

  setStatus("KML polygon loaded successfully.");
});

// ------------------------------
// Run Detection
// ------------------------------
document.getElementById('detectBtn').addEventListener('click', async () => {
  if (drawnItems.getLayers().length === 0) {
    alert("Draw a polygon or upload a KML first.");
    return;
  }

  const zoom = parseInt(document.getElementById('zoomSel').value);
  const layer = drawnItems.getLayers()[0];
  const geojson = layer.toGeoJSON();

  setStatus("Sending data to server... Please wait.");

  try {
    const res = await fetch('/detect', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        geojson: geojson,
        zoom: zoom,
        conf_threshold: 0.8
      })
    });

    if (!res.ok) {
      setStatus("Server error: " + (await res.text()));
      return;
    }

    // Detection summary
    let summary = {};
    const summaryHeader = res.headers.get('X-Detection-Summary');
    try { summary = JSON.parse(summaryHeader || "{}"); } catch {}

    // Download ZIP
    const blob = await res.blob();
    const url = URL.createObjectURL(blob);

    const a = document.createElement('a');
    a.href = url;
    a.download = "detections.zip";
    document.body.appendChild(a);
    a.click();
    a.remove();
    URL.revokeObjectURL(url);

    setStatus("Detection completed. Summary: " + JSON.stringify(summary));

  } catch (err) {
    console.error(err);
    setStatus("Error: " + err.toString());
  }
});

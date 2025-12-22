# 🛰️ Median Opening Detection using YOLOv8 and KML Coordinates

This project trains a YOLOv8 model using a dataset annotated with [ MakeSense.ai ](https://www.makesense.ai) (without Roboflow), and detects  median openings  in highways by processing coordinates from a KML file. The detections are saved both as  CSV  (latitude–longitude points) and as  KML , so you can visualize results directly in  Google Earth .

---

## 📦 Project Structure

```
median_detection/
│
├── data.yaml                  # YOLO dataset configuration file (auto-created)
├── runs/                      # YOLO training output (contains best.pt)
├── sat_images/                # Downloaded satellite images
├── detections.csv             # Output detections with coordinates & confidence
├── detections.kml             # Detections visualized in Google Earth
└── your_dataset.zip           # Annotated dataset from MakeSense.ai
```

---

## ⚙️ Requirements

Make sure the following libraries are installed:

```bash
!pip install fastkml simplekml ultralytics Pillow tqdm requests pyyaml
```

---

## 📁 Step 1 — Dataset Setup (MakeSense.ai)

1. Annotate your dataset on  MakeSense.ai  and export it in  YOLO format .
2. Organize the folder structure as:
   ```
   dataset/
   ├── images/
   │   ├── train/
   │   └── val/
   └── labels/
       ├── train/
       └── val/
   ```
3. Zip the dataset and upload it to your  Google Drive :
   ```
   /content/drive/MyDrive/satellite_dataset_balanced.zip
   ```

---

## 🧠 Step 2 — Training the YOLOv8 Model

This script automatically extracts the dataset, creates a `data.yaml`, and starts training.

```python
from ultralytics import YOLO
import yaml, zipfile, os
from pathlib import Path

WORK_DIR = "/content/median_detection"
DATA_ZIP_PATH = "/content/drive/MyDrive/satellite_dataset_balanced.zip"

# Extract Dataset
os.makedirs(WORK_DIR, exist_ok=True)
with zipfile.ZipFile(DATA_ZIP_PATH, 'r') as zip_ref:
    zip_ref.extractall(WORK_DIR)

# Create data.yaml
data_dict = {
    "train": f"{WORK_DIR}/images/train",
    "val": f"{WORK_DIR}/images/val",
    "nc": 1,
    "names": ["median_opening"]
}
with open(f"{WORK_DIR}/data.yaml", "w") as f:
    yaml.safe_dump(data_dict, f)

# Train YOLOv8
model = YOLO("yolov8n.pt")
model.train(
    data=f"{WORK_DIR}/data.yaml",
    epochs=60,
    imgsz=640,
    batch=8,
    project=f"{WORK_DIR}/runs",
    name="median_yolo_run",
    patience=30
)
```

After training, the best weights will be stored at:

```
/content/median_detection/runs/median_yolo_run/weights/best.pt
```

---

## 🌍 Step 3 — Parsing KML and Detecting Median Openings

This part takes  latitude-longitude coordinates  from a KML file, downloads satellite images, and runs detection using your trained model.

### Inputs:
- `INPUT_KML`: Path to your `.kml` file (e.g., `Assam_project_center.kml`)
- `BEST_MODEL_PATH`: Path to the trained YOLO model (best.pt)
- `API_KEY`: Your  Google Maps Static API  key

### Code:
```python
from ultralytics import YOLO
import simplekml, requests, math, os, shutil, csv, xml.etree.ElementTree as ET
from tqdm import tqdm
from PIL import Image

WORK_DIR = "/content/median_detection"
API_KEY = "YOUR_GOOGLE_MAPS_API_KEY"
BEST_MODEL_PATH = "/content/median_detection/runs/median_yolo_run/weights/best.pt"
INPUT_KML = "/content/drive/MyDrive/Colab Notebooks/Assam_project_center.kml"
SAT_SAVE_DIR = f"{WORK_DIR}/sat_images"
OUT_CSV_PATH = f"{WORK_DIR}/detections.csv"
OUT_KML_PATH = f"{WORK_DIR}/detections.kml"
ZOOM = 20
IMG_SIZE = 640
CONF_THRES = 0.25
os.makedirs(SAT_SAVE_DIR, exist_ok=True)
```

The script:
1. Parses coordinates from the input KML.
2. Downloads satellite images for each coordinate using the Google Maps Static API.
3. Runs inference using the trained YOLOv8 model.
4. Converts detected pixel coordinates back to geographic coordinates (lat/lon).
5. Saves all detections to:
   -  CSV  → `detections.csv`
   -  KML  → `detections.kml`

You can open the KML output directly in  Google Earth  to visualize the detected median openings.

---

## 📊 Output Files

| File | Description |
|------|--------------|
| `detections.csv` | Contains image name, latitude, longitude, confidence, and class |
| `detections.kml` | Placemarks for each detected median opening (viewable in Google Earth) |
| `runs/median_yolo_run/weights/best.pt` | Trained YOLOv8 model weights |

Example CSV snippet:

| image | lat | lon | confidence | class |
|--------|-----|-----|-------------|-------|
| 26.49097_90.58296.png | 26.49097 | 90.58296 | 0.88 | 0 |
| 26.49112_90.58345.png | 26.49112 | 90.58345 | 0.91 | 0 |

---

## 📍 Visualization

1. Open `detections.kml` in  Google Earth Desktop  or  Google Earth Web .
2. Zoom into any placemark — it represents a detected  median opening .
3. The description includes model confidence and image name.

---

## ⚠️ Notes

- Make sure your dataset and KML are properly aligned geographically.
- API key must have access to  Google Static Maps API .
- Higher `zoom` (18–21) gives better accuracy but slower processing.
- If detections are missing, reduce `CONF_THRES` (e.g., `0.15`) or train with more diverse data.

---

## 🧩 Example Workflow Summary

| Step | Description |
|------|--------------|
| 1️⃣ | Annotate dataset on [MakeSense.ai](https://www.makesense.ai) |
| 2️⃣ | Export YOLO format and upload ZIP to Drive |
| 3️⃣ | Run training block in Colab |
| 4️⃣ | Provide KML file and Google Maps API key |
| 5️⃣ | Run detection block to generate CSV + KML |
| 6️⃣ | View results in Google Earth |

---

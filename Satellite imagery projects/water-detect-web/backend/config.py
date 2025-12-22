# ---------------------------------------------------------
# config.py
# Configuration settings for backend Flask server
# ---------------------------------------------------------

import os

# ================
# MODEL SETTINGS
# ================

# Path to your YOLO model (.pt file)
MODEL_PATH = os.environ.get(
    "MODEL_PATH",
    "C:/Users/devi.naidu/Desktop/water-detect-web/best.pt"  # change this path
)

# Confidence Threshold for YOLO detections
CONF_THRESHOLD = float(os.environ.get("CONF_THRESHOLD", 0.60))


# ================
# TILE DOWNLOAD SETTINGS
# ================

# Google satellite tile server
TILE_URL_TEMPLATE = "https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}"

# Default zoom level for satellite tiles
ZOOM_LEVEL = int(os.environ.get("ZOOM_LEVEL", 18))

# Image size for each tile
TILE_SIZE = int(os.environ.get("TILE_SIZE", 512))


# ================
# APP SETTINGS
# ================

# Folder where downloaded tiles + outputs will be saved
OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "output")

# Ensure folder exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

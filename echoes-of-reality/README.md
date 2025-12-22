# Echoes of Reality – Deepfake Detection System

A Flask-based deepfake video detection web application that analyzes uploaded videos and predicts whether they are REAL or FAKE using deep learning–based facial feature extraction and temporal modeling.

This project is intended for academic / demo purposes, not for production-grade forensic analysis.

---

## 🚀 Features

* Upload video files via a web interface
* Extract facial landmarks and frames
* Deepfake detection using a pretrained deep learning model
* Simple Flask UI for testing
* Modular project structure

---

## 📁 Project Structure

```
echoes-of-reality/
│
├── app.py                     # Flask application entry point
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
│
├── models/                    # Pretrained model files
│   ├── detector.pth
│   └── shape_predictor_68_face_landmarks.dat
│
├── utils/                     # Core logic
│   ├── video_utils.py         # Video & face processing
│   ├── detection_utils.py     # Deepfake detector model loader
│   └── __init__.py
│
├── templates/                 # HTML templates
│   └── index.html
│
├── static/                    # CSS, images
│   └── style.css
│
├── temp_files/                # Temporary uploaded videos
├── checkpoints/               # (Optional) training checkpoints
└── venv/                      # Virtual environment
```

---

## 🛠️ Installation & Setup

### 1️⃣ Clone / Open the project

```bash
git clone <repo-url>
cd echoes-of-reality
```

Or extract the ZIP and open the folder in VS Code.

---

### 2️⃣ Create virtual environment (recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

⚠️ Important notes:

* `dlib` may require Visual Studio C++ Build Tools on Windows
* If `dlib` fails, install using a precompiled wheel

---

### 4️⃣ Download required model files

Make sure these files exist:

```
models/
├── detector.pth
└── shape_predictor_68_face_landmarks.dat
```

If missing:

* Download `shape_predictor_68_face_landmarks.dat` from:

  > [http://dlib.net/files/](http://dlib.net/files/)

---

## ▶️ Running the Application

From the project root directory:

```bash
python app.py
```

Then open your browser at:

```
http://127.0.0.1:5000
```

---

## 🧪 How Detection Works (High Level)

1. User uploads a video
2. Frames are extracted
3. Faces & landmarks detected (dlib)
4. Features passed to deepfake detection model
5. Result displayed: REAL or FAKE

---

## ⚠️ Known Limitations

* Detection accuracy depends on video quality
* Model is pretrained (not trained in this project)
* Slow on CPU-only systems
* Not suitable for legal or forensic use

---

## 🧠 Technologies Used

* Python 3.10
* Flask
* PyTorch
* OpenCV
* dlib
* face-alignment
* HTML / CSS

---

## 📌 Troubleshooting

### ❌ `ModuleNotFoundError: dlib`

* Install Visual C++ Build Tools
* Use precompiled wheel

## 📄 Disclaimer

This project is for educational and demonstration purposes only. Deepfake detection is an evolving research area and results may not be reliable in real-world scenarios.

---

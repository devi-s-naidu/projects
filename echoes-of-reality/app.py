from flask import Flask, render_template, request, jsonify, send_file, session
from flask_cors import CORS
import os
import uuid
import json
from datetime import datetime
from werkzeug.utils import secure_filename
import cv2
import torch
import numpy as np

from utils.audio_utils import AudioProcessor
from utils.video_utils import VideoProcessor
from utils.detection_utils import DeepfakeDetector
from utils.generation_utils import DeepfakeGenerator

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['TEMP_FOLDER'] = 'temp_files'
app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024  # 500MB max file size

# Create directories
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['TEMP_FOLDER'], exist_ok=True)
os.makedirs('models', exist_ok=True)
os.makedirs('checkpoints', exist_ok=True)

CORS(app)

# Initialize processors
audio_processor = AudioProcessor()
video_processor = VideoProcessor()
detector = DeepfakeDetector()
generator = DeepfakeGenerator()

ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov', 'mkv', 'wav', 'mp3'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate')
def generate_page():
    return render_template('generate.html')

@app.route('/detect')
def detect_page():
    return render_template('detect.html')

@app.route('/api/generate', methods=['POST'])
def generate_deepfake():
    try:
        if 'video' not in request.files or 'audio' not in request.files:
            return jsonify({'error': 'Missing video or audio file'}), 400
        
        video_file = request.files['video']
        audio_file = request.files['audio']
        text_input = request.form.get('text', '')
        
        if video_file.filename == '' or audio_file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        
        if not (allowed_file(video_file.filename) and allowed_file(audio_file.filename)):
            return jsonify({'error': 'Invalid file type'}), 400
        
        # Generate unique IDs for files
        unique_id = str(uuid.uuid4())[:8]
        
        # Save uploaded files
        video_filename = f"input_video_{unique_id}_{secure_filename(video_file.filename)}"
        audio_filename = f"input_audio_{unique_id}_{secure_filename(audio_file.filename)}"
        
        video_path = os.path.join(app.config['TEMP_FOLDER'], video_filename)
        audio_path = os.path.join(app.config['TEMP_FOLDER'], audio_filename)
        
        video_file.save(video_path)
        audio_file.save(audio_path)
        
        # Process text if provided
        if text_input:
            # Convert text to speech
            tts_audio_path = audio_processor.text_to_speech(text_input, unique_id)
            audio_path = tts_audio_path
        
        # Generate deepfake
        output_path = generator.generate(
            video_path=video_path,
            audio_path=audio_path,
            output_id=unique_id
        )
        
        # Return result
        return jsonify({
            'success': True,
            'output_path': output_path,
            'download_url': f'/download/{os.path.basename(output_path)}'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/detect', methods=['POST'])
def detect_deepfake():
    try:
        if 'video' not in request.files:
            return jsonify({'error': 'No video file provided'}), 400
        
        video_file = request.files['video']
        
        if video_file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        
        if not allowed_file(video_file.filename):
            return jsonify({'error': 'Invalid file type'}), 400
        
        # Save uploaded file
        unique_id = str(uuid.uuid4())[:8]
        filename = f"detect_video_{unique_id}_{secure_filename(video_file.filename)}"
        video_path = os.path.join(app.config['TEMP_FOLDER'], filename)
        video_file.save(video_path)
        
        # Detect deepfake
        result = detector.detect(video_path)
        
        # Clean up
        os.remove(video_path)
        
        return jsonify({
            'success': True,
            'result': result
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/record_audio', methods=['POST'])
def record_audio():
    try:
        audio_data = request.get_json().get('audio_data')
        unique_id = str(uuid.uuid4())[:8]
        
        audio_path = audio_processor.save_audio_from_base64(audio_data, unique_id)
        
        return jsonify({
            'success': True,
            'audio_path': audio_path
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/speech_to_text', methods=['POST'])
def speech_to_text():
    try:
        if 'audio' not in request.files:
            return jsonify({'error': 'No audio file provided'}), 400
        
        audio_file = request.files['audio']
        text = audio_processor.speech_to_text(audio_file)
        
        return jsonify({
            'success': True,
            'text': text
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(
        os.path.join(app.config['TEMP_FOLDER'], filename),
        as_attachment=True
    )

@app.route('/api/process_realtime', methods=['POST'])
def process_realtime():
    try:
        data = request.get_json()
        text = data.get('text')
        video_file = request.files.get('video')
        
        if not text or not video_file:
            return jsonify({'error': 'Missing text or video'}), 400
        
        # Save video
        unique_id = str(uuid.uuid4())[:8]
        video_path = os.path.join(
            app.config['TEMP_FOLDER'],
            f"realtime_video_{unique_id}_{secure_filename(video_file.filename)}"
        )
        video_file.save(video_path)
        
        # Convert text to speech
        audio_path = audio_processor.text_to_speech(text, unique_id)
        
        # Generate lip-sync video
        output_path = generator.generate(video_path, audio_path, f"realtime_{unique_id}")
        
        return jsonify({
            'success': True,
            'output_path': output_path
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
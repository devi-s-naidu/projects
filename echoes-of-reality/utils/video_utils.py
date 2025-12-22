import cv2
import numpy as np
import os
from PIL import Image
import dlib
import face_alignment
from skimage import io
import torch

class VideoProcessor:
    def __init__(self):
        self.face_detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor('models/shape_predictor_68_face_landmarks.dat')
        self.fa = face_alignment.FaceAlignment(
            face_alignment.LandmarksType.TWO_D,
            flip_input=False,
            device='cuda' if torch.cuda.is_available() else 'cpu'
        )
    
    def extract_frames(self, video_path, output_folder):
        """Extract frames from video"""
        os.makedirs(output_folder, exist_ok=True)
        
        cap = cv2.VideoCapture(video_path)
        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_count = 0
        frames = []
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            frame_path = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
            cv2.imwrite(frame_path, frame)
            frames.append(frame_path)
            frame_count += 1
        
        cap.release()
        return frames, fps
    
    def detect_face(self, image_path):
        """Detect face in image"""
        image = io.imread(image_path)
        faces = self.face_detector(image)
        
        if len(faces) > 0:
            # Get the largest face
            face = max(faces, key=lambda rect: rect.width() * rect.height())
            return face
        return None
    
    def extract_face_landmarks(self, image_path):
        """Extract facial landmarks"""
        try:
            image = io.imread(image_path)
            landmarks = self.fa.get_landmarks(image)
            
            if landmarks is not None and len(landmarks) > 0:
                return landmarks[0]
            return None
        except Exception as e:
            print(f"Error extracting landmarks: {e}")
            return None
    
    def create_video_from_frames(self, frames, output_path, fps):
        """Create video from frames"""
        if not frames:
            return None
        
        # Read first frame to get dimensions
        frame = cv2.imread(frames[0])
        height, width, _ = frame.shape
        
        # Create video writer
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
        
        # Write frames
        for frame_path in frames:
            frame = cv2.imread(frame_path)
            out.write(frame)
        
        out.release()
        return output_path
    
    def preprocess_video(self, video_path, output_folder):
        """Preprocess video for lip-sync"""
        frames, fps = self.extract_frames(video_path, output_folder)
        
        # Process each frame
        processed_frames = []
        for frame_path in frames:
            # Detect and align face
            face = self.detect_face(frame_path)
            if face:
                # Extract face region
                x1, y1, x2, y2 = face.left(), face.top(), face.right(), face.bottom()
                face_img = cv2.imread(frame_path)[y1:y2, x1:x2]
                
                # Resize to standard size
                face_img = cv2.resize(face_img, (256, 256))
                
                # Save processed frame
                processed_path = frame_path.replace('.jpg', '_processed.jpg')
                cv2.imwrite(processed_path, face_img)
                processed_frames.append(processed_path)
        
        return processed_frames, fps
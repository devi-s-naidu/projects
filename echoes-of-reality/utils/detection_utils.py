import torch
import torch.nn as nn
import torchvision.models as models
import torchvision.transforms as transforms
from torch.nn import functional as F
import numpy as np
import cv2
import os
from PIL import Image
from collections import deque

class DeepfakeDetector:
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = self.build_detection_model()
        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])
        
    def build_detection_model(self):
        """Build ResNext + LSTM model for deepfake detection"""
        class ResNextLSTM(nn.Module):
            def __init__(self, num_classes=2, lstm_hidden=256, lstm_layers=2):
                super(ResNextLSTM, self).__init__()
                
                # ResNext backbone
                resnext = models.resnext50_32x4d(pretrained=True)
                self.feature_extractor = nn.Sequential(*list(resnext.children())[:-1])
                
                # LSTM for temporal features
                self.lstm = nn.LSTM(
                    input_size=2048,  # ResNext feature size
                    hidden_size=lstm_hidden,
                    num_layers=lstm_layers,
                    batch_first=True,
                    bidirectional=True,
                    dropout=0.5
                )
                
                # Classifier
                self.fc1 = nn.Linear(lstm_hidden * 2, 512)
                self.dropout = nn.Dropout(0.5)
                self.fc2 = nn.Linear(512, num_classes)
                self.relu = nn.ReLU()
                
            def forward(self, x):
                # x shape: (batch_size, sequence_length, channels, height, width)
                batch_size, seq_len = x.shape[0], x.shape[1]
                
                # Extract features for each frame
                features = []
                for i in range(seq_len):
                    frame_features = self.feature_extractor(x[:, i, :, :, :])
                    frame_features = frame_features.view(batch_size, -1)
                    features.append(frame_features)
                
                # Stack features
                features = torch.stack(features, dim=1)
                
                # LSTM for temporal modeling
                lstm_out, _ = self.lstm(features)
                
                # Use last hidden state
                last_hidden = lstm_out[:, -1, :]
                
                # Classification
                x = self.relu(self.fc1(last_hidden))
                x = self.dropout(x)
                x = self.fc2(x)
                
                return x
        
        model = ResNextLSTM()
        
        # Load pretrained weights if available
        checkpoint_path = 'models/detection_model.pth'
        if os.path.exists(checkpoint_path):
            checkpoint = torch.load(checkpoint_path, map_location=self.device)
            model.load_state_dict(checkpoint, strict=False)
        
        model = model.to(self.device)
        model.eval()
        return model
    
    def extract_frames(self, video_path, num_frames=32):
        """Extract frames from video for detection"""
        cap = cv2.VideoCapture(video_path)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        
        # Calculate frame indices to sample
        frame_indices = np.linspace(0, total_frames - 1, num_frames, dtype=int)
        
        frames = []
        for idx in frame_indices:
            cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
            ret, frame = cap.read()
            if ret:
                # Convert BGR to RGB
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = Image.fromarray(frame)
                frames.append(frame)
        
        cap.release()
        return frames
    
    def preprocess_frames(self, frames):
        """Preprocess frames for model input"""
        processed_frames = []
        for frame in frames:
            frame = self.transform(frame)
            processed_frames.append(frame)
        
        # Stack frames
        if processed_frames:
            video_tensor = torch.stack(processed_frames, dim=0)
            video_tensor = video_tensor.unsqueeze(0)  # Add batch dimension
            return video_tensor
        return None
    
    def detect(self, video_path):
        """Detect if video is deepfake"""
        try:
            # Extract frames
            frames = self.extract_frames(video_path)
            
            if len(frames) < 16:
                return {
                    'is_fake': False,
                    'confidence': 0.5,
                    'message': 'Not enough frames for detection'
                }
            
            # Preprocess frames
            video_tensor = self.preprocess_frames(frames)
            
            if video_tensor is None:
                return {
                    'is_fake': False,
                    'confidence': 0.5,
                    'message': 'Failed to process video'
                }
            
            # Move to device
            video_tensor = video_tensor.to(self.device)
            
            # Make prediction
            with torch.no_grad():
                outputs = self.model(video_tensor)
                probabilities = F.softmax(outputs, dim=1)
                fake_prob = probabilities[0][1].item()
            
            # Determine result
            is_fake = fake_prob > 0.5
            confidence = fake_prob if is_fake else 1 - fake_prob
            
            return {
                'is_fake': bool(is_fake),
                'confidence': round(confidence * 100, 2),
                'fake_probability': round(fake_prob * 100, 2),
                'real_probability': round((1 - fake_prob) * 100, 2),
                'message': 'Deepfake detected' if is_fake else 'Video appears to be real'
            }
            
        except Exception as e:
            print(f"Error in detection: {e}")
            return {
                'is_fake': False,
                'confidence': 0,
                'message': f'Error: {str(e)}'
            }
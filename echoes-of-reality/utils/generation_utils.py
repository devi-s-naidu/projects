import os
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import cv2
from models.wav2lip import Wav2Lip
import subprocess
import warnings
warnings.filterwarnings("ignore")

class DeepfakeGenerator:
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = self.load_wav2lip_model()
    
    def load_wav2lip_model(self):
        """Load Wav2Lip model"""
        model = Wav2Lip()
        
        # Load pretrained weights
        checkpoint_path = 'checkpoints/wav2lip_gan.pth'
        if os.path.exists(checkpoint_path):
            checkpoint = torch.load(checkpoint_path, map_location=self.device)
            model.load_state_dict(checkpoint['state_dict'])
        
        model = model.to(self.device)
        model.eval()
        return model
    
    def generate(self, video_path, audio_path, output_id):
        """Generate lip-synced video"""
        try:
            # Create output paths
            temp_dir = f"temp_files/generation_{output_id}"
            os.makedirs(temp_dir, exist_ok=True)
            
            # Extract audio features
            from utils.audio_utils import AudioProcessor
            audio_processor = AudioProcessor()
            processed_audio = audio_processor.process_audio(audio_path)
            
            # Extract video frames
            from utils.video_utils import VideoProcessor
            video_processor = VideoProcessor()
            frames, fps = video_processor.extract_frames(video_path, os.path.join(temp_dir, "frames"))
            
            # Generate lip-synced frames (simplified - in practice, use Wav2Lip inference)
            output_frames_dir = os.path.join(temp_dir, "output_frames")
            os.makedirs(output_frames_dir, exist_ok=True)
            
            # This is a simplified version - actual Wav2Lip inference would go here
            for i, frame_path in enumerate(frames[:min(100, len(frames))]):  # Limit frames for demo
                frame = cv2.imread(frame_path)
                # Apply some transformation (in practice, use model inference)
                output_frame = self.apply_lip_sync(frame, i)
                output_frame_path = os.path.join(output_frames_dir, f"frame_{i:04d}.jpg")
                cv2.imwrite(output_frame_path, output_frame)
            
            # Create output video
            output_video_path = f"temp_files/output_{output_id}.mp4"
            video_processor.create_video_from_frames(
                [os.path.join(output_frames_dir, f) for f in sorted(os.listdir(output_frames_dir))],
                output_video_path,
                fps
            )
            
            # Add audio to video
            final_output_path = f"temp_files/final_output_{output_id}.mp4"
            self.add_audio_to_video(output_video_path, processed_audio, final_output_path)
            
            # Clean up temporary files
            self.cleanup_temp_files(temp_dir)
            
            return final_output_path
            
        except Exception as e:
            print(f"Error in generation: {e}")
            return None
    
    def apply_lip_sync(self, frame, frame_index):
        """Apply lip sync to frame (placeholder - implement actual model inference)"""
        # In practice, this would use the Wav2Lip model
        # For demo purposes, just return the frame
        return frame
    
    def add_audio_to_video(self, video_path, audio_path, output_path):
        """Combine video and audio"""
        try:
            cmd = f'ffmpeg -i {video_path} -i {audio_path} -c:v copy -c:a aac -strict experimental {output_path} -y'
            subprocess.call(cmd, shell=True)
            return output_path
        except Exception as e:
            print(f"Error adding audio: {e}")
            return video_path
    
    def cleanup_temp_files(self, temp_dir):
        """Clean up temporary files"""
        import shutil
        try:
            shutil.rmtree(temp_dir)
        except:
            pass
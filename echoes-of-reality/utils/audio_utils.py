import speech_recognition as sr
from gtts import gTTS
import os
import io
import base64
import numpy as np
import librosa
import soundfile as sf
from pydub import AudioSegment
import tempfile
import wave

class AudioProcessor:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        
    def speech_to_text(self, audio_file):
        """Convert speech to text using Google Speech Recognition"""
        try:
            # Save audio file temporarily
            with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tmp_file:
                audio_file.save(tmp_file.name)
                
                # Use speech recognition
                with sr.AudioFile(tmp_file.name) as source:
                    audio_data = self.recognizer.record(source)
                    text = self.recognizer.recognize_google(audio_data)
                
                os.unlink(tmp_file.name)
                return text
                
        except Exception as e:
            print(f"Error in speech recognition: {e}")
            return ""
    
    def text_to_speech(self, text, output_id, language='en'):
        """Convert text to speech using gTTS"""
        try:
            output_path = f"temp_files/tts_output_{output_id}.mp3"
            tts = gTTS(text=text, lang=language, slow=False)
            tts.save(output_path)
            
            # Convert to WAV if needed
            if output_path.endswith('.mp3'):
                audio = AudioSegment.from_mp3(output_path)
                wav_path = output_path.replace('.mp3', '.wav')
                audio.export(wav_path, format='wav')
                os.remove(output_path)
                output_path = wav_path
            
            return output_path
            
        except Exception as e:
            print(f"Error in text-to-speech: {e}")
            return None
    
    def extract_audio_from_video(self, video_path):
        """Extract audio from video file"""
        try:
            output_path = video_path.replace('.mp4', '.wav')
            os.system(f"ffmpeg -i {video_path} -q:a 0 -map a {output_path} -y")
            return output_path
        except Exception as e:
            print(f"Error extracting audio: {e}")
            return None
    
    def save_audio_from_base64(self, audio_data, output_id):
        """Save audio from base64 encoded data"""
        try:
            # Decode base64
            audio_bytes = base64.b64decode(audio_data.split(',')[1])
            
            # Save as WAV
            output_path = f"temp_files/recorded_{output_id}.wav"
            with open(output_path, 'wb') as f:
                f.write(audio_bytes)
            
            return output_path
        except Exception as e:
            print(f"Error saving audio: {e}")
            return None
    
    def process_audio(self, audio_path, target_sr=16000):
        """Process audio for lip-sync"""
        try:
            # Load audio
            audio, sr = librosa.load(audio_path, sr=target_sr)
            
            # Normalize audio
            audio = audio / np.max(np.abs(audio))
            
            # Save processed audio
            output_path = audio_path.replace('.wav', '_processed.wav')
            sf.write(output_path, audio, target_sr)
            
            return output_path
        except Exception as e:
            print(f"Error processing audio: {e}")
            return audio_path
import sys
import subprocess

print("Testing Echoes of Reality setup...")
print("="*50)

# Check Python version
print(f"Python version: {sys.version}")

# Check required packages
required_packages = [
    'flask', 'torch', 'torchvision', 'opencv-python',
    'numpy', 'speechrecognition', 'gtts', 'librosa'
]

for package in required_packages:
    try:
        __import__(package.replace('-', '_'))
        print(f"✓ {package}")
    except ImportError:
        print(f"✗ {package} - NOT INSTALLED")

# Check FFmpeg
try:
    result = subprocess.run(['ffmpeg', '-version'], capture_output=True, text=True)
    if result.returncode == 0:
        print("✓ FFmpeg installed")
    else:
        print("✗ FFmpeg not found")
except FileNotFoundError:
    print("✗ FFmpeg not found in PATH")

# Check CUDA
import torch
print(f"✓ PyTorch version: {torch.__version__}")
print(f"  CUDA available: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"  GPU: {torch.cuda.get_device_name(0)}")

print("\n" + "="*50)
print("Setup test complete!")
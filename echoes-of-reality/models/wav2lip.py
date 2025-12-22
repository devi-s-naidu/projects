import torch
import torch.nn as nn
import torch.nn.functional as F

class Wav2Lip(nn.Module):
    def __init__(self):
        super(Wav2Lip, self).__init__()
        
        # Audio encoder
        self.audio_encoder = nn.Sequential(
            nn.Conv1d(1, 32, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),
            nn.Conv1d(32, 64, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),
            nn.Conv1d(64, 128, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),
            nn.AdaptiveAvgPool1d(1)
        )
        
        # Visual encoder
        self.visual_encoder = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=7, stride=2, padding=3),
            nn.ReLU(),
            nn.MaxPool2d(3, stride=2, padding=1),
            nn.Conv2d(64, 128, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),
            nn.Conv2d(128, 256, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),
            nn.AdaptiveAvgPool2d((1, 1))
        )
        
        # Fusion and decoder
        self.fusion = nn.Sequential(
            nn.Linear(256 + 128, 512),
            nn.ReLU(),
            nn.Linear(512, 256 * 8 * 8)
        )
        
        self.decoder = nn.Sequential(
            nn.ConvTranspose2d(256, 128, kernel_size=4, stride=2, padding=1),
            nn.ReLU(),
            nn.ConvTranspose2d(128, 64, kernel_size=4, stride=2, padding=1),
            nn.ReLU(),
            nn.ConvTranspose2d(64, 32, kernel_size=4, stride=2, padding=1),
            nn.ReLU(),
            nn.Conv2d(32, 3, kernel_size=7, padding=3),
            nn.Tanh()
        )
    
    def forward(self, audio, visual):
        # Audio encoding
        audio_features = self.audio_encoder(audio)
        audio_features = audio_features.view(audio_features.size(0), -1)
        
        # Visual encoding
        visual_features = self.visual_encoder(visual)
        visual_features = visual_features.view(visual_features.size(0), -1)
        
        # Fusion
        combined = torch.cat([audio_features, visual_features], dim=1)
        fused = self.fusion(combined)
        fused = fused.view(-1, 256, 8, 8)
        
        # Decoding
        output = self.decoder(fused)
        
        return output
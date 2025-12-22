import torch
import torch.nn as nn
import torchvision.models as models
import torch.nn.functional as F

class ResNextLSTM(nn.Module):
    def __init__(self, num_classes=2, lstm_hidden=256, lstm_layers=2):
        super(ResNextLSTM, self).__init__()
        
        # Load pretrained ResNext
        resnext = models.resnext50_32x4d(pretrained=True)
        
        # Remove the final classification layer
        modules = list(resnext.children())[:-2]
        self.resnext = nn.Sequential(*modules)
        
        # Adaptive pooling
        self.adaptive_pool = nn.AdaptiveAvgPool2d((1, 1))
        
        # LSTM for temporal features
        self.lstm = nn.LSTM(
            input_size=2048,
            hidden_size=lstm_hidden,
            num_layers=lstm_layers,
            batch_first=True,
            bidirectional=True,
            dropout=0.5
        )
        
        # Classifier
        self.classifier = nn.Sequential(
            nn.Linear(lstm_hidden * 2, 512),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(512, 128),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(128, num_classes)
        )
        
    def forward(self, x):
        # x shape: (batch_size, seq_len, channels, height, width)
        batch_size, seq_len = x.shape[0], x.shape[1]
        
        # Extract features for each frame
        features = []
        for i in range(seq_len):
            frame = x[:, i, :, :, :]
            frame_features = self.resnext(frame)
            frame_features = self.adaptive_pool(frame_features)
            frame_features = frame_features.view(batch_size, -1)
            features.append(frame_features)
        
        # Stack features
        features = torch.stack(features, dim=1)
        
        # LSTM for temporal modeling
        lstm_out, _ = self.lstm(features)
        
        # Use last hidden state
        last_hidden = lstm_out[:, -1, :]
        
        # Classification
        output = self.classifier(last_hidden)
        
        return output
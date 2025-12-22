class EchoesOfReality {
    constructor() {
        this.currentMode = 'generate';
        this.audioRecorder = null;
        this.isRecording = false;
        this.audioChunks = [];
        this.initializeEventListeners();
    }

    initializeEventListeners() {
        // Navigation buttons
        document.querySelectorAll('.nav-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                this.switchMode(e.target.dataset.mode);
            });
        });

        // File upload preview
        document.querySelectorAll('input[type="file"]').forEach(input => {
            input.addEventListener('change', (e) => {
                this.showFilePreview(e.target);
            });
        });

        // Record audio button
        const recordBtn = document.getElementById('recordAudio');
        if (recordBtn) {
            recordBtn.addEventListener('click', () => {
                this.toggleAudioRecording();
            });
        }

        // Process buttons
        document.getElementById('generateBtn').addEventListener('click', () => {
            this.processGeneration();
        });

        document.getElementById('detectBtn').addEventListener('click', () => {
            this.processDetection();
        });

        // Real-time processing
        const realtimeBtn = document.getElementById('processRealtime');
        if (realtimeBtn) {
            realtimeBtn.addEventListener('click', () => {
                this.processRealtime();
            });
        }
    }

    switchMode(mode) {
        this.currentMode = mode;
        
        // Update active button
        document.querySelectorAll('.nav-btn').forEach(btn => {
            btn.classList.remove('active');
            if (btn.dataset.mode === mode) {
                btn.classList.add('active');
            }
        });
        
        // Show active content
        document.querySelectorAll('.content-area').forEach(content => {
            content.classList.remove('active');
            if (content.id === `${mode}Content`) {
                content.classList.add('active');
            }
        });
        
        // Clear previous results
        this.clearResults();
    }

    showFilePreview(input) {
        const file = input.files[0];
        if (!file) return;
        
        const previewId = input.id + 'Preview';
        const previewDiv = document.getElementById(previewId);
        
        if (previewDiv) {
            previewDiv.innerHTML = `
                <div class="file-preview">
                    <strong>${file.name}</strong>
                    <span>${this.formatFileSize(file.size)}</span>
                    <span>Type: ${file.type}</span>
                </div>
            `;
        }
    }

    async toggleAudioRecording() {
        const recordBtn = document.getElementById('recordAudio');
        
        if (!this.isRecording) {
            await this.startRecording();
            recordBtn.textContent = 'Stop Recording';
            recordBtn.classList.add('recording');
        } else {
            await this.stopRecording();
            recordBtn.textContent = 'Record Audio';
            recordBtn.classList.remove('recording');
        }
        
        this.isRecording = !this.isRecording;
    }

    async startRecording() {
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
            this.audioRecorder = new MediaRecorder(stream);
            this.audioChunks = [];
            
            this.audioRecorder.ondataavailable = (event) => {
                if (event.data.size > 0) {
                    this.audioChunks.push(event.data);
                }
            };
            
            this.audioRecorder.start();
        } catch (error) {
            this.showAlert('Error accessing microphone: ' + error.message, 'error');
        }
    }

    async stopRecording() {
        return new Promise((resolve) => {
            this.audioRecorder.onstop = async () => {
                const audioBlob = new Blob(this.audioChunks, { type: 'audio/wav' });
                await this.saveRecordedAudio(audioBlob);
                resolve();
            };
            
            this.audioRecorder.stop();
            this.audioRecorder.stream.getTracks().forEach(track => track.stop());
        });
    }

    async saveRecordedAudio(audioBlob) {
        const reader = new FileReader();
        reader.readAsDataURL(audioBlob);
        
        reader.onloadend = async () => {
            const base64Audio = reader.result;
            
            // Send to server
            try {
                const response = await fetch('/api/record_audio', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ audio_data: base64Audio })
                });
                
                const result = await response.json();
                if (result.success) {
                    this.showAlert('Audio recorded successfully!', 'success');
                    
                    // Update audio file input
                    const audioInput = document.getElementById('audioFile');
                    if (audioInput) {
                        const file = new File([audioBlob], 'recorded_audio.wav', { type: 'audio/wav' });
                        const dataTransfer = new DataTransfer();
                        dataTransfer.items.add(file);
                        audioInput.files = dataTransfer.files;
                        this.showFilePreview(audioInput);
                    }
                }
            } catch (error) {
                this.showAlert('Error saving audio: ' + error.message, 'error');
            }
        };
    }

    async processGeneration() {
        const videoFile = document.getElementById('videoFile').files[0];
        const audioFile = document.getElementById('audioFile').files[0];
        const textInput = document.getElementById('textInput').value;
        
        if (!videoFile && !audioFile) {
            this.showAlert('Please provide at least a video or audio file', 'error');
            return;
        }
        
        this.showLoading(true);
        this.clearResults();
        
        const formData = new FormData();
        if (videoFile) formData.append('video', videoFile);
        if (audioFile) formData.append('audio', audioFile);
        if (textInput) formData.append('text', textInput);
        
        try {
            const response = await fetch('/api/generate', {
                method: 'POST',
                body: formData
            });
            
            const result = await response.json();
            this.showLoading(false);
            
            if (result.success) {
                this.showGenerationResults(result);
            } else {
                this.showAlert(result.error || 'Generation failed', 'error');
            }
        } catch (error) {
            this.showLoading(false);
            this.showAlert('Error: ' + error.message, 'error');
        }
    }

    async processDetection() {
        const videoFile = document.getElementById('detectVideoFile').files[0];
        
        if (!videoFile) {
            this.showAlert('Please select a video file for detection', 'error');
            return;
        }
        
        this.showLoading(true);
        this.clearResults();
        
        const formData = new FormData();
        formData.append('video', videoFile);
        
        try {
            const response = await fetch('/api/detect', {
                method: 'POST',
                body: formData
            });
            
            const result = await response.json();
            this.showLoading(false);
            
            if (result.success) {
                this.showDetectionResults(result.result);
            } else {
                this.showAlert(result.error || 'Detection failed', 'error');
            }
        } catch (error) {
            this.showLoading(false);
            this.showAlert('Error: ' + error.message, 'error');
        }
    }

    async processRealtime() {
        const textInput = document.getElementById('realtimeText').value;
        const videoFile = document.getElementById('realtimeVideoFile').files[0];
        
        if (!textInput || !videoFile) {
            this.showAlert('Please provide both text and video', 'error');
            return;
        }
        
        this.showLoading(true);
        
        const formData = new FormData();
        formData.append('video', videoFile);
        
        // Convert text to speech first
        try {
            // Convert text to speech (client-side simulation)
            const ttsResponse = await fetch('/api/process_realtime', {
                method: 'POST',
                body: JSON.stringify({ text: textInput }),
                headers: { 'Content-Type': 'application/json' }
            });
            
            const ttsResult = await ttsResponse.json();
            
            if (ttsResult.success) {
                // Now generate with audio
                formData.append('audio', new Blob());
                formData.append('text', textInput);
                
                const generateResponse = await fetch('/api/generate', {
                    method: 'POST',
                    body: formData
                });
                
                const generateResult = await generateResponse.json();
                this.showLoading(false);
                
                if (generateResult.success) {
                    this.showGenerationResults(generateResult);
                }
            }
        } catch (error) {
            this.showLoading(false);
            this.showAlert('Error: ' + error.message, 'error');
        }
    }

    showGenerationResults(result) {
        const resultsSection = document.getElementById('generateResults');
        resultsSection.innerHTML = `
            <div class="result-item">
                <div class="result-label">Status</div>
                <div class="result-value success">Generation Complete!</div>
            </div>
            <div class="result-item">
                <div class="result-label">Output Video</div>
                <div>
                    <video controls style="width: 100%; max-width: 600px; border-radius: 10px;">
                        <source src="${result.output_path}" type="video/mp4">
                        Your browser does not support the video tag.
                    </video>
                </div>
            </div>
            <div class="result-item">
                <div class="result-label">Download</div>
                <a href="${result.download_url}" class="download-btn" download>
                    Download Video
                </a>
            </div>
        `;
        resultsSection.classList.add('active');
    }

    showDetectionResults(result) {
        const resultsSection = document.getElementById('detectResults');
        const isFake = result.is_fake;
        
        resultsSection.innerHTML = `
            <div class="result-item">
                <div class="result-label">Detection Result</div>
                <div class="result-value ${isFake ? 'error' : 'success'}">
                    ${result.message}
                </div>
            </div>
            <div class="result-item">
                <div class="result-label">Confidence</div>
                <div class="result-value">${result.confidence}%</div>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: ${result.confidence}%"></div>
                </div>
            </div>
            <div class="result-item">
                <div class="result-label">Fake Probability</div>
                <div class="result-value">${result.fake_probability}%</div>
            </div>
            <div class="result-item">
                <div class="result-label">Real Probability</div>
                <div class="result-value">${result.real_probability}%</div>
            </div>
        `;
        resultsSection.classList.add('active');
    }

    showLoading(show) {
        const loadingDiv = document.getElementById('loading');
        if (show) {
            loadingDiv.classList.add('active');
        } else {
            loadingDiv.classList.remove('active');
        }
    }

    showAlert(message, type = 'info') {
        const alertDiv = document.createElement('div');
        alertDiv.className = `alert ${type}`;
        alertDiv.textContent = message;
        
        const container = document.querySelector('.main-content');
        container.insertBefore(alertDiv, container.firstChild);
        
        setTimeout(() => {
            alertDiv.remove();
        }, 5000);
    }

    clearResults() {
        document.querySelectorAll('.results-section').forEach(section => {
            section.classList.remove('active');
            section.innerHTML = '';
        });
        
        document.querySelectorAll('.alert').forEach(alert => alert.remove());
    }

    formatFileSize(bytes) {
        if (bytes === 0) return '0 Bytes';
        const k = 1024;
        const sizes = ['Bytes', 'KB', 'MB', 'GB'];
        const i = Math.floor(Math.log(bytes) / Math.log(k));
        return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
    }
}

// Initialize the application when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    window.app = new EchoesOfReality();
});
from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO, emit
import threading
import time
from datetime import datetime
import json

# Create Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'network-ids-secret-key-2024'
socketio = SocketIO(app, cors_allowed_origins="*")

# Global dashboard instance
dashboard_instance = None

class Dashboard:
    def __init__(self, alert_handler, packet_sniffer, detectors):
        global dashboard_instance
        dashboard_instance = self
        
        self.alert_handler = alert_handler
        self.packet_sniffer = packet_sniffer
        self.detectors = detectors
        
        self.packet_count = 0
        self.start_time = datetime.now()
        self.stats_history = []
        self.max_history = 60  # Keep 60 data points (1 per second for 60 seconds)
        self.lock = threading.Lock()
        
        print("[✓] Dashboard initialized")
    
    def start(self, host='127.0.0.1', port=5000):
        print(f"[✓] Starting dashboard on http://{host}:{port}")
        print(f"[*] Open your browser and navigate to: http://{host}:{port}")
        
        # Start background thread for data updates
        update_thread = threading.Thread(target=self._update_dashboard_data)
        update_thread.daemon = True
        update_thread.start()
        
        # Start Flask app
        try:
            socketio.run(app, host=host, port=port, debug=False, use_reloader=False)
        except Exception as e:
            print(f"[!] Error starting dashboard: {e}")
    
    def _update_dashboard_data(self):
        while True:
            try:
                with self.lock:
                    self.packet_count = self.packet_sniffer.get_packet_count()
                
                # Get current stats
                stats = self._get_current_stats()
                
                # Update history
                self.stats_history.append(stats)
                if len(self.stats_history) > self.max_history:
                    self.stats_history = self.stats_history[-self.max_history:]
                
                # Emit update via WebSocket
                socketio.emit('stats_update', stats)
                
                # Get recent alerts
                alerts = self.alert_handler.get_active_alerts()
                if alerts:
                    socketio.emit('alerts_update', alerts[-20:])  # Last 20 alerts
                
                # Get detector stats periodically
                detector_stats = self._get_detector_stats()
                socketio.emit('detector_stats', detector_stats)
                
                time.sleep(1)  # Update every second
                
            except Exception as e:
                print(f"[!] Dashboard update error: {e}")
                time.sleep(5)
    
    def _get_current_stats(self):
        current_time = datetime.now()
        uptime = current_time - self.start_time
        
        with self.lock:
            return {
                'uptime': str(uptime).split('.')[0],  # Remove microseconds
                'packet_count': self.packet_count,
                'packets_per_second': self._calculate_pps(),
                'active_alerts': len(self.alert_handler.get_active_alerts()),
                'total_alerts': self.alert_handler.total_alerts,
                'current_time': current_time.strftime('%Y-%m-%d %H:%M:%S'),
                'system_status': self._get_system_status()
            }
    
    def _calculate_pps(self):
        if len(self.stats_history) < 2:
            return 0
        
        recent_packets = [s['packet_count'] for s in self.stats_history[-5:]]
        if len(recent_packets) < 2:
            return 0
        
        return max(0, recent_packets[-1] - recent_packets[0]) / min(len(recent_packets) - 1, 5)
    
    def _get_system_status(self):
        alerts = self.alert_handler.get_active_alerts()
        critical_alerts = [a for a in alerts if a.get('severity') == 'CRITICAL']
        
        if critical_alerts:
            return 'CRITICAL'
        elif alerts:
            return 'WARNING'
        else:
            return 'NORMAL'
    
    def _get_detector_stats(self):
        stats = {}
        for name, detector in self.detectors.items():
            if hasattr(detector, 'get_stats'):
                stats[name] = detector.get_stats()
        return stats

# ===================== FLASK ROUTES =====================

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/stats')
def get_stats():
    if dashboard_instance:
        return jsonify(dashboard_instance._get_current_stats())
    return jsonify({'error': 'Dashboard not initialized'})

@app.route('/api/alerts')
def get_alerts():
    if dashboard_instance:
        alerts = dashboard_instance.alert_handler.get_active_alerts()
        return jsonify(alerts[-50:])  # Last 50 alerts
    return jsonify([])

@app.route('/api/detectors')
def get_detectors():
    if dashboard_instance:
        stats = dashboard_instance._get_detector_stats()
        return jsonify(stats)
    return jsonify({})

@app.route('/api/history')
def get_history():
    if dashboard_instance:
        return jsonify(dashboard_instance.stats_history[-60:])  # Last 60 seconds
    return jsonify([])

@socketio.on('connect')
def handle_connect():
    print('[*] Client connected to dashboard')
    if dashboard_instance:
        # Send initial data
        emit('stats_update', dashboard_instance._get_current_stats())
        emit('detector_stats', dashboard_instance._get_detector_stats())

@socketio.on('disconnect')
def handle_disconnect():
    print('[*] Client disconnected from dashboard')
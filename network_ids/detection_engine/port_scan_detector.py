from collections import defaultdict
from datetime import datetime, timedelta
import threading

class PortScanDetector:
    def __init__(self, threshold=10, time_window=30):
        self.threshold = threshold
        self.time_window = time_window
        self.scan_data = defaultdict(list)  # IP: [(timestamp, port), ...]
        self.detected_scans = []
        self.lock = threading.Lock()
        
    def analyze_packet(self, packet_info):
        if not packet_info:
            return None
            
        # Only analyze TCP/UDP packets with ports
        protocol = packet_info.get('protocol')
        if protocol not in ['TCP', 'UDP']:
            return None
            
        src_ip = packet_info['source_ip']
        dst_port = packet_info.get('destination_port')
        
        if not dst_port:
            return None
            
        try:
            timestamp = datetime.fromisoformat(packet_info['timestamp'])
        except:
            timestamp = datetime.now()
        
        with self.lock:
            # Clean old entries
            now = datetime.now()
            self.scan_data[src_ip] = [
                (ts, port) for ts, port in self.scan_data[src_ip]
                if (now - ts).total_seconds() < self.time_window
            ]
            
            # Add new entry
            self.scan_data[src_ip].append((timestamp, dst_port))
            
            # Count unique ports
            ports = [port for _, port in self.scan_data[src_ip]]
            unique_ports = len(set(ports))
            
            # Check threshold
            if unique_ports >= self.threshold:
                # Create alert
                alert = {
                    'type': 'PORT_SCAN',
                    'source_ip': src_ip,
                    'severity': 'HIGH',
                    'message': f'Port scan detected from {src_ip}. Scanned {unique_ports} unique ports in {self.time_window} seconds.',
                    'timestamp': datetime.now().isoformat(),
                    'details': {
                        'unique_ports': unique_ports,
                        'ports_scanned': list(set(ports))[:10],  # First 10 ports
                        'time_window': self.time_window,
                        'protocol': protocol
                    }
                }
                
                # Store detection
                self.detected_scans.append(alert)
                
                # Clear data for this IP after detection
                self.scan_data[src_ip] = []
                
                return alert
        
        return None
    
    def get_stats(self):
        with self.lock:
            return {
                'active_monitoring': len(self.scan_data),
                'total_detected': len(self.detected_scans),
                'recent_detections': self.detected_scans[-5:] if self.detected_scans else []
            }
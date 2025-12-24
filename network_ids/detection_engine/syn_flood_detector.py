from collections import defaultdict
from datetime import datetime, timedelta
import threading

class SYNFloodDetector:
    def __init__(self, threshold=50, time_window=5):
        self.threshold = threshold
        self.time_window = time_window
        self.syn_counter = defaultdict(list)  # IP: [timestamp1, timestamp2, ...]
        self.detected_floods = []
        self.lock = threading.Lock()
        
    def analyze_packet(self, packet_info):
        if not packet_info:
            return None
            
        # Check if it's a TCP SYN packet
        if (packet_info.get('protocol') == 'TCP' and 
            packet_info.get('flags') == 2):  # SYN flag
            
            src_ip = packet_info['source_ip']
            
            try:
                timestamp = datetime.fromisoformat(packet_info['timestamp'])
            except:
                timestamp = datetime.now()
            
            with self.lock:
                # Clean old timestamps
                now = datetime.now()
                self.syn_counter[src_ip] = [
                    ts for ts in self.syn_counter[src_ip]
                    if (now - ts).total_seconds() < self.time_window
                ]
                
                # Add new timestamp
                self.syn_counter[src_ip].append(timestamp)
                
                # Count SYN packets
                syn_count = len(self.syn_counter[src_ip])
                
                # Check threshold
                if syn_count >= self.threshold:
                    # Create alert
                    alert = {
                        'type': 'SYN_FLOOD',
                        'source_ip': src_ip,
                        'severity': 'CRITICAL',
                        'message': f'SYN flood detected from {src_ip}. {syn_count} SYN packets in {self.time_window} seconds.',
                        'timestamp': datetime.now().isoformat(),
                        'details': {
                            'packet_count': syn_count,
                            'time_window': self.time_window,
                            'destination_ip': packet_info.get('destination_ip', 'Unknown'),
                            'destination_port': packet_info.get('destination_port', 'Unknown')
                        }
                    }
                    
                    # Store detection
                    self.detected_floods.append(alert)
                    
                    # Clear counter after detection
                    self.syn_counter[src_ip] = []
                    
                    return alert
        
        return None
    
    def get_stats(self):
        with self.lock:
            return {
                'active_monitoring': len(self.syn_counter),
                'total_detected': len(self.detected_floods),
                'recent_detections': self.detected_floods[-5:] if self.detected_floods else []
            }
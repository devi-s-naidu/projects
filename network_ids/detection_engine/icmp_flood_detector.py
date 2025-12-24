"""
ICMP Flood Detector
Detects ICMP (Ping) flood attacks
"""
from collections import defaultdict
from datetime import datetime, timedelta
import threading

class ICMPFloodDetector:
    def __init__(self, threshold=30, time_window=3):
        """
        Initialize ICMP flood detector
        :param threshold: Number of ICMP packets to trigger alert
        :param time_window: Time window in seconds
        """
        self.threshold = threshold
        self.time_window = time_window
        self.icmp_counter = defaultdict(list)  # IP: [timestamp1, timestamp2, ...]
        self.detected_floods = []
        self.lock = threading.Lock()
        
    def analyze_packet(self, packet_info):
        """
        Analyze packet for ICMP flood patterns
        Returns alert dict if detected, None otherwise
        """
        if not packet_info:
            return None
            
        # Check if it's an ICMP packet
        if packet_info.get('protocol') == 'ICMP':
            src_ip = packet_info['source_ip']
            
            try:
                timestamp = datetime.fromisoformat(packet_info['timestamp'])
            except:
                timestamp = datetime.now()
            
            with self.lock:
                # Clean old timestamps
                now = datetime.now()
                self.icmp_counter[src_ip] = [
                    ts for ts in self.icmp_counter[src_ip]
                    if (now - ts).total_seconds() < self.time_window
                ]
                
                # Add new timestamp
                self.icmp_counter[src_ip].append(timestamp)
                
                # Count ICMP packets
                icmp_count = len(self.icmp_counter[src_ip])
                
                # Check threshold
                if icmp_count >= self.threshold:
                    # Create alert
                    alert = {
                        'type': 'ICMP_FLOOD',
                        'source_ip': src_ip,
                        'severity': 'HIGH',
                        'message': f'ICMP flood detected from {src_ip}. {icmp_count} ICMP packets in {self.time_window} seconds.',
                        'timestamp': datetime.now().isoformat(),
                        'details': {
                            'packet_count': icmp_count,
                            'time_window': self.time_window,
                            'destination_ip': packet_info.get('destination_ip', 'Unknown'),
                            'packet_size': packet_info.get('packet_size', 0)
                        }
                    }
                    
                    # Store detection
                    self.detected_floods.append(alert)
                    
                    # Clear counter after detection
                    self.icmp_counter[src_ip] = []
                    
                    return alert
        
        return None
    
    def get_stats(self):
        """Get detection statistics"""
        with self.lock:
            return {
                'active_monitoring': len(self.icmp_counter),
                'total_detected': len(self.detected_floods),
                'recent_detections': self.detected_floods[-5:] if self.detected_floods else []
            }
import threading
import queue
import time
from datetime import datetime

class AlertHandler:
    def __init__(self, alert_logger):
        self.alert_logger = alert_logger
        self.alert_queue = queue.Queue(maxsize=500)
        self.active_alerts = []
        self.max_alerts = 100
        self.lock = threading.Lock()
        self.total_alerts = 0
        
        # Start processing thread
        self.processing_thread = threading.Thread(target=self._process_alerts)
        self.processing_thread.daemon = True
        self.processing_thread.start()
        
        print("[✓] Alert handler initialized")
    
    def add_alert(self, alert_data):
        if alert_data:
            try:
                self.alert_queue.put_nowait(alert_data)
                self.total_alerts += 1
            except queue.Full:
                print("[!] Alert queue is full, dropping alert")
    
    def _process_alerts(self):
        while True:
            try:
                alert = self.alert_queue.get(timeout=1)
                if alert:
                    # Log the alert
                    self.alert_logger.log_alert(alert)
                    
                    # Store in active alerts list
                    with self.lock:
                        self.active_alerts.append(alert)
                        
                        # Keep only recent alerts
                        if len(self.active_alerts) > self.max_alerts:
                            self.active_alerts = self.active_alerts[-self.max_alerts:]
                            
            except queue.Empty:
                continue
            except Exception as e:
                print(f"[!] Error processing alert: {e}")
                time.sleep(1)
    
    def get_active_alerts(self):
        with self.lock:
            return self.active_alerts.copy()
    
    def get_stats(self):
        with self.lock:
            return {
                'queue_size': self.alert_queue.qsize(),
                'active_alerts': len(self.active_alerts),
                'total_alerts': self.total_alerts,
                'recent_alerts': self.active_alerts[-10:] if self.active_alerts else []
            }
    
    def clear_alerts(self):
        with self.lock:
            self.active_alerts = []
            print("[✓] Active alerts cleared")
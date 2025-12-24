import json
import csv
import os
from datetime import datetime
from colorama import init, Fore, Style

# Initialize colorama for colored console output
init(autoreset=True)

class AlertLogger:
    def __init__(self, log_dir='logs'):
        self.log_dir = log_dir
        self.csv_file = os.path.join(log_dir, 'alerts.csv')
        self.json_file = os.path.join(log_dir, 'alerts.json')
        
        # Create log directory if it doesn't exist
        os.makedirs(log_dir, exist_ok=True)
        
        # Initialize CSV file with headers if it doesn't exist
        if not os.path.exists(self.csv_file):
            with open(self.csv_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([
                    'timestamp', 'alert_type', 'source_ip', 
                    'severity', 'message', 'details'
                ])
        
        print(f"[✓] Alert logger initialized. Logs stored in: {log_dir}")
    
    def log_alert(self, alert_data):
        if not alert_data:
            return
            
        # Add to CSV
        self._log_to_csv(alert_data)
        
        # Add to JSON
        self._log_to_json(alert_data)
        
        # Print to console with colors
        self._print_alert(alert_data)
    
    def _log_to_csv(self, alert_data):
        try:
            with open(self.csv_file, 'a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([
                    alert_data.get('timestamp', datetime.now().isoformat()),
                    alert_data.get('type', 'UNKNOWN'),
                    alert_data.get('source_ip', 'Unknown'),
                    alert_data.get('severity', 'MEDIUM'),
                    alert_data.get('message', 'No message'),
                    json.dumps(alert_data.get('details', {}))
                ])
        except Exception as e:
            print(f"[!] Error writing to CSV: {e}")
    
    def _log_to_json(self, alert_data):
        try:
            # Read existing alerts
            alerts = []
            if os.path.exists(self.json_file):
                with open(self.json_file, 'r', encoding='utf-8') as f:
                    try:
                        alerts = json.load(f)
                    except json.JSONDecodeError:
                        alerts = []
            
            # Add new alert
            alerts.append(alert_data)
            
            # Keep only last 1000 alerts
            if len(alerts) > 1000:
                alerts = alerts[-1000:]
            
            # Write back to file
            with open(self.json_file, 'w', encoding='utf-8') as f:
                json.dump(alerts, f, indent=2, default=str)
                
        except Exception as e:
            print(f"[!] Error writing to JSON: {e}")
    
    def _print_alert(self, alert_data):
        alert_type = alert_data.get('type', 'UNKNOWN')
        severity = alert_data.get('severity', 'MEDIUM')
        message = alert_data.get('message', 'No message')
        source_ip = alert_data.get('source_ip', 'Unknown')
        timestamp = alert_data.get('timestamp', datetime.now().isoformat())
        
        # Choose color based on severity
        if severity == 'CRITICAL':
            color = Fore.RED + Style.BRIGHT
        elif severity == 'HIGH':
            color = Fore.YELLOW + Style.BRIGHT
        elif severity == 'MEDIUM':
            color = Fore.CYAN
        else:
            color = Fore.GREEN
        
        # Format timestamp
        try:
            dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
            time_str = dt.strftime('%H:%M:%S')
        except:
            time_str = timestamp
        
        # Print alert
        print(f"\n{color}═{'═' * 60}")
        print(f"[{time_str}] {severity} ALERT: {alert_type}")
        print(f"{'═' * 60}")
        print(f"Source IP: {source_ip}")
        print(f"Message: {message}")
        print(f"{'═' * 61}{Style.RESET_ALL}")
    
    def get_recent_alerts(self, limit=50):
        if not os.path.exists(self.json_file):
            return []
        
        try:
            with open(self.json_file, 'r', encoding='utf-8') as f:
                alerts = json.load(f)
                return alerts[-limit:] if alerts else []
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    
    def clear_logs(self):
        try:
            if os.path.exists(self.csv_file):
                os.remove(self.csv_file)
            if os.path.exists(self.json_file):
                os.remove(self.json_file)
            print("[✓] Log files cleared")
        except Exception as e:
            print(f"[!] Error clearing logs: {e}")
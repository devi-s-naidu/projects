
import sys
import os
import time
import signal
import threading
from datetime import datetime

# Add current directory to path for module imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def print_banner():
    banner = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                   NETWORK INTRUSION DETECTION SYSTEM         ║
    ║                          Version 1.0.0                       ║
    ╚══════════════════════════════════════════════════════════════╝
    
    [*] Detecting: Port Scans, SYN Floods, ICMP Floods
    [*] Features: Real-time monitoring, Alert logging, Web Dashboard
    """
    print(banner)

def check_prerequisites():
    print("[*] Checking prerequisites...")
    
    # Check Python version
    if sys.version_info < (3, 7):
        print("[!] Python 3.7 or higher is required")
        return False
    
    # Check if running as root/Admin (optional but recommended)
    try:
        import os
        if os.name == 'posix' and os.geteuid() != 0:
            print("[!] Warning: Not running as root. Packet capture may not work.")
            print("    Try: sudo python main.py")
    except:
        pass
    
    # Check for required modules with more robust checking
    modules = [
        ('scapy', 'scapy'),
        ('flask', 'Flask'),
        ('flask_socketio', 'Flask-SocketIO'),
        ('colorama', 'colorama')
    ]
    
    all_installed = True
    for import_name, package_name in modules:
        try:
            __import__(import_name)
            print(f"[✓] {package_name} installed")
        except ImportError:
            print(f"[!] {package_name} not installed. Run: pip install {package_name}")
            all_installed = False
    
    return all_installed

def load_config():
    config = {
        'network': {
            'interface': None,  # None = default interface
            'packet_count_limit': 0  # 0 = unlimited
        },
        'detection': {
            'port_scan': {
                'threshold': 10,
                'time_window': 30
            },
            'syn_flood': {
                'threshold': 50,
                'time_window': 5
            },
            'icmp_flood': {
                'threshold': 30,
                'time_window': 3
            }
        },
        'dashboard': {
            'host': '127.0.0.1',
            'port': 5000
        }
    }
    
    # Try to load from config file if it exists
    try:
        # Use simple JSON instead of YAML to avoid dependencies
        import json
        with open('config.json', 'r') as f:
            file_config = json.load(f)
            # Merge configurations
            for key in file_config:
                if key in config:
                    if isinstance(config[key], dict) and isinstance(file_config[key], dict):
                        config[key].update(file_config[key])
                    else:
                        config[key] = file_config[key]
            print("[✓] Configuration loaded from config.json")
    except FileNotFoundError:
        print("[*] Using default configuration (config.json not found)")
    except Exception as e:
        print(f"[*] Using default configuration (Error loading config: {e})")
    
    return config

# Now import our modules AFTER prerequisite check
try:
    from packet_capture.packet_sniffer import PacketSniffer
    from detection_engine.port_scan_detector import PortScanDetector
    from detection_engine.syn_flood_detector import SYNFloodDetector
    from detection_engine.icmp_flood_detector import ICMPFloodDetector
    from alert_system.alert_logger import AlertLogger
    from alert_system.alert_handler import AlertHandler
    from dashboard.dashboard import Dashboard
except ImportError as e:
    print(f"[!] Failed to import module: {e}")
    print("[!] Make sure all project files are in the correct directories")
    sys.exit(1)

class NetworkIDS:
    def __init__(self, config):
        self.config = config
        self.running = False
        
        print("[*] Initializing Network IDS components...")
        
        # Initialize components
        self.packet_queue = None
        
        # Packet capture
        interface = config['network']['interface']
        self.sniffer = PacketSniffer(interface=interface)
        
        # Detection engines
        det_config = config['detection']
        
        self.port_scan_detector = PortScanDetector(
            threshold=det_config['port_scan']['threshold'],
            time_window=det_config['port_scan']['time_window']
        )
        
        self.syn_flood_detector = SYNFloodDetector(
            threshold=det_config['syn_flood']['threshold'],
            time_window=det_config['syn_flood']['time_window']
        )
        
        self.icmp_flood_detector = ICMPFloodDetector(
            threshold=det_config['icmp_flood']['threshold'],
            time_window=det_config['icmp_flood']['time_window']
        )
        
        # Alert system
        self.alert_logger = AlertLogger()
        self.alert_handler = AlertHandler(self.alert_logger)
        
        # Detector dictionary for dashboard
        self.detectors = {
            'port_scan': self.port_scan_detector,
            'syn_flood': self.syn_flood_detector,
            'icmp_flood': self.icmp_flood_detector
        }
        
        # Dashboard
        self.dashboard = Dashboard(
            alert_handler=self.alert_handler,
            packet_sniffer=self.sniffer,
            detectors=self.detectors
        )
        
        # Statistics
        self.stats = {
            'start_time': datetime.now(),
            'packets_processed': 0,
            'alerts_generated': 0,
            'detections_by_type': {
                'PORT_SCAN': 0,
                'SYN_FLOOD': 0,
                'ICMP_FLOOD': 0
            }
        }
        
        # Threads
        self.processing_thread = None
        self.dashboard_thread = None
        
        print("[✓] All components initialized successfully")
    
    def start(self):
        if self.running:
            print("[!] IDS is already running")
            return
            
        self.running = True
        
        print("\n[*] Starting Network IDS...")
        
        try:
            # Start packet capture
            self.sniffer.start_capture()
            
            # Start packet processing thread
            self.processing_thread = threading.Thread(target=self._process_packets)
            self.processing_thread.daemon = True
            self.processing_thread.start()
            
            # Start dashboard in a separate thread
            dash_config = self.config['dashboard']
            self.dashboard_thread = threading.Thread(
                target=self.dashboard.start,
                kwargs={
                    'host': dash_config['host'],
                    'port': dash_config['port']
                }
            )
            self.dashboard_thread.daemon = True
            self.dashboard_thread.start()
            
            print("[✓] Network IDS started successfully")
            print(f"[*] Dashboard available at: http://{dash_config['host']}:{dash_config['port']}")
            print("[*] Press Ctrl+C to stop\n")
            
            # Keep main thread alive
            while self.running:
                time.sleep(1)
                
        except KeyboardInterrupt:
            print("\n[*] Shutdown requested...")
            self.stop()
        except Exception as e:
            print(f"[!] Error starting IDS: {e}")
            import traceback
            traceback.print_exc()
            self.stop()
    
    def _process_packets(self):
        print("[*] Packet processing started")
        
        while self.running and self.sniffer.is_capturing:
            try:
                # Get packet from sniffer
                packet = self.sniffer.get_packet(timeout=0.5)
                
                if packet:
                    self.stats['packets_processed'] += 1
                    
                    # Run all detectors
                    alerts = []
                    
                    # Port scan detection
                    port_scan_alert = self.port_scan_detector.analyze_packet(packet)
                    if port_scan_alert:
                        alerts.append(port_scan_alert)
                        self.stats['detections_by_type']['PORT_SCAN'] += 1
                    
                    # SYN flood detection
                    syn_flood_alert = self.syn_flood_detector.analyze_packet(packet)
                    if syn_flood_alert:
                        alerts.append(syn_flood_alert)
                        self.stats['detections_by_type']['SYN_FLOOD'] += 1
                    
                    # ICMP flood detection
                    icmp_flood_alert = self.icmp_flood_detector.analyze_packet(packet)
                    if icmp_flood_alert:
                        alerts.append(icmp_flood_alert)
                        self.stats['detections_by_type']['ICMP_FLOOD'] += 1
                    
                    # Process all alerts
                    for alert in alerts:
                        self.alert_handler.add_alert(alert)
                        self.stats['alerts_generated'] += 1
                    
                    # Print progress every 1000 packets
                    if self.stats['packets_processed'] % 1000 == 0:
                        self._print_stats()
                        
            except Exception as e:
                print(f"[!] Error processing packet: {e}")
                time.sleep(1)
    
    def _print_stats(self):
        uptime = datetime.now() - self.stats['start_time']
        hours, remainder = divmod(int(uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        
        print(f"\n[📊] STATS: Uptime: {hours:02d}:{minutes:02d}:{seconds:02d} | "
              f"Packets: {self.stats['packets_processed']:,} | "
              f"Alerts: {self.stats['alerts_generated']}")
        
        # Print detector stats
        for detector_name, detector in self.detectors.items():
            if hasattr(detector, 'get_stats'):
                stats = detector.get_stats()
                print(f"    {detector_name}: {stats.get('total_detected', 0)} detections")
    
    def stop(self):
        if not self.running:
            return
            
        print("\n[*] Stopping Network IDS...")
        self.running = False
        
        # Stop packet capture
        if self.sniffer:
            self.sniffer.stop_capture()
        
        # Wait for processing thread
        if self.processing_thread:
            self.processing_thread.join(timeout=2)
        
        # Print final statistics
        self._print_final_stats()
        
        print("[✓] Network IDS stopped")
    
    def _print_final_stats(self):
        print("\n" + "=" * 60)
        print("FINAL STATISTICS")
        print("=" * 60)
        
        uptime = datetime.now() - self.stats['start_time']
        hours, remainder = divmod(int(uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        
        print(f"Total Runtime: {hours:02d}:{minutes:02d}:{seconds:02d}")
        print(f"Packets Processed: {self.stats['packets_processed']:,}")
        print(f"Alerts Generated: {self.stats['alerts_generated']}")
        print(f"Packets Captured: {self.sniffer.get_packet_count():,}")
        
        print("\nDetection Breakdown:")
        for alert_type, count in self.stats['detections_by_type'].items():
            print(f"  {alert_type.replace('_', ' ').title()}: {count}")
        
        print("=" * 60)

def signal_handler(sig, frame):
    print("\n[*] Ctrl+C detected. Shutting down...")
    sys.exit(0)

def main():
    # Setup signal handler for Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)
    
    # Print banner
    print_banner()
    
    # Check prerequisites
    if not check_prerequisites():
        print("\n[!] Some prerequisites are missing. Please install them first.")
        print("    Try: pip install -r requirements.txt")
        sys.exit(1)
    
    # Load configuration
    config = load_config()
    
    # Create and start IDS
    try:
        ids = NetworkIDS(config)
        ids.start()
    except KeyboardInterrupt:
        print("\n[*] Shutdown complete")
    except Exception as e:
        print(f"[!] Fatal error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
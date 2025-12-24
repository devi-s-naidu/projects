# Network Intrusion Detection System (NIDS)

A real-time Network Intrusion Detection System built from scratch using packet-level traffic analysis to detect port scans, SYN floods, and ICMP floods with alert logging and a live monitoring dashboard.

## 📋 Features

- Real-time Packet Capture: Captures network traffic using Scapy
- Multiple Detection Engines:
  - Port Scan Detection: Detects horizontal and vertical port scanning
  - SYN Flood Detection: Identifies TCP SYN flood (DoS) attacks
  - ICMP Flood Detection: Detects ICMP (Ping) flood attacks
- Alert System: Color-coded console alerts with CSV/JSON logging
- Web Dashboard: Real-time monitoring interface with charts and statistics
- Configurable: Easy to adjust detection thresholds and settings
- Cross-platform: Works on Windows, Linux, and macOS

## 🏗️ Architecture

```
network_ids/
├── packet_capture/          # Packet sniffing and parsing
│   ├── packet_sniffer.py
│   └── packet_parser.py
├── detection_engine/        # Detection algorithms
│   ├── port_scan_detector.py
│   ├── syn_flood_detector.py
│   └── icmp_flood_detector.py
├── alert_system/           # Alert handling and logging
│   ├── alert_logger.py
│   └── alert_handler.py
├── dashboard/              # Web interface
│   ├── dashboard.py
│   └── templates/
│       └── index.html
├── logs/                   # Alert logs (auto-generated)
├── config.json             # Configuration file
├── requirements.txt        # Python dependencies
└── main.py                # Main application
```

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- Administrator/root privileges (for packet capture)
- Npcap (Windows) or libpcap (Linux/macOS)

### Installation

1. Clone or download the project

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install packet capture libraries:

   For Windows:
   - Download and install [Npcap](https://npcap.com/)
   - Select "Install Npcap in WinPcap API-compatible mode"

   For Linux:
   ```bash
   sudo apt-get install libpcap-dev  # Debian/Ubuntu
   sudo yum install libpcap-devel    # RHEL/CentOS
   ```

   For macOS:
   ```bash
   brew install libpcap
   ```

### Configuration

Edit `config.json` to customize detection thresholds:

```json
{
  "network": {
    "interface": null,           # null = default interface
    "packet_count_limit": 0      # 0 = unlimited
  },
  "detection": {
    "port_scan": {
      "threshold": 10,           # Alert if 10+ unique ports scanned
      "time_window": 30          # Within 30 seconds
    },
    "syn_flood": {
      "threshold": 50,           # Alert if 50+ SYN packets
      "time_window": 5           # Within 5 seconds
    },
    "icmp_flood": {
      "threshold": 30,           # Alert if 30+ ICMP packets
      "time_window": 3           # Within 3 seconds
    }
  },
  "dashboard": {
    "host": "127.0.0.1",
    "port": 5000
  }
}
```

## 🎯 Usage

### Starting the IDS

Linux/macOS (requires sudo):
```bash
sudo python main.py
```

Windows (Run as Administrator):
1. Open Command Prompt as Administrator
2. Navigate to project directory
3. Run:
```bash
python main.py
```

### Accessing the Dashboard

Once started, open your browser and navigate to:
```
http://localhost:5000
```

### Dashboard Features

- Real-time Statistics: Packet count, alerts, uptime
- Traffic Charts: Live packet rate visualization
- Alert Display: Color-coded security alerts
- Detection Breakdown: Charts showing attack types

## 🔧 Detection Algorithms

### 1. Port Scan Detection
- Method: Tracks unique destination ports per source IP
- Alert: Triggers when threshold exceeded within time window
- Default: 10+ unique ports in 30 seconds

### 2. SYN Flood Detection
- Method: Monitors TCP SYN packets per source IP
- Alert: Triggers on excessive SYN packets (DoS attack)
- Default: 50+ SYN packets in 5 seconds

### 3. ICMP Flood Detection
- Method: Counts ICMP packets per source IP
- Alert: Detects ping flood attacks
- Default: 30+ ICMP packets in 3 seconds

## 📊 Alert System

Alerts are displayed in three ways:

1. Console Output: Color-coded messages with timestamps
2. CSV Logs: `logs/alerts.csv` for data analysis
3. JSON Logs: `logs/alerts.json` for programmatic access

Alert format:
```json
{
  "type": "PORT_SCAN",
  "source_ip": "192.168.1.100",
  "severity": "HIGH",
  "message": "Port scan detected from 192.168.1.100",
  "timestamp": "2024-01-01T10:00:00",
  "details": {
    "unique_ports": 15,
    "time_window": 30
  }
}
```

## 🛠️ Troubleshooting

### Common Issues

1. "Permission denied" for packet capture
   - Solution: Run with administrator/root privileges
   - Windows: Run Command Prompt as Administrator
   - Linux/macOS: Use `sudo`

2. Scapy import errors
   ```bash
   pip uninstall scapy -y
   pip install scapy==2.5.0
   ```

3. No packets captured
   - Check network interface in config
   - Verify Npcap/WinPcap installation (Windows)
   - Try different interface (eth0, wlan0, etc.)

4. Dashboard not accessible
   - Check if port 5000 is available
   - Change port in config.json
   - Check firewall settings

### Testing Without Admin Privileges

Run the test script:
```bash
python test_scapy.py
```

## 📈 Performance

- Packet Processing: Real-time with minimal latency
- Memory Usage: Configurable queue sizes prevent memory leaks
- Scalability: Thread-based architecture for concurrent processing
- Storage: Rotating logs with configurable limits

## 🔒 Security Notes

⚠️ IMPORTANT DISCLAIMER

This is an educational project for learning purposes only:

1. Not Production-Ready: This system is for educational use
2. Network Monitoring: Only use on networks you own or have permission to monitor
3. Legal Compliance: Ensure compliance with local laws and regulations
4. Privacy: This tool captures network packets - respect privacy laws

## 🧪 Testing

### Simulated Attacks for Testing

1. Port Scan Test (using nmap):
```bash
nmap -p 1-100 localhost
```

2. SYN Flood Test (using hping3):
```bash
hping3 -S -p 80 --flood 127.0.0.1
```

3. ICMP Flood Test (using ping):
```bash
ping -f 127.0.0.1
```

## 🤝 Contributing

This is an educational project. Suggestions and improvements are welcome!




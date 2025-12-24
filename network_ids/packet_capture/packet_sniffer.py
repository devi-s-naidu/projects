import threading
import queue
import time
from datetime import datetime
from scapy.all import sniff, IP, TCP, UDP, ICMP
import logging

# Disable Scapy warnings
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

class PacketSniffer:
    def __init__(self, interface=None, packet_queue=None):
        self.interface = interface
        self.packet_queue = packet_queue if packet_queue else queue.Queue(maxsize=10000)
        self.is_capturing = False
        self.sniff_thread = None
        self.packet_count = 0
        
    def start_capture(self):
        if self.is_capturing:
            print("[!] Capture already running")
            return
            
        self.is_capturing = True
        self.sniff_thread = threading.Thread(target=self._capture_packets)
        self.sniff_thread.daemon = True
        self.sniff_thread.start()
        
        interface_name = self.interface if self.interface else "default interface"
        print(f"[✓] Packet capture started on {interface_name}")
        
    def _capture_packets(self):
        def packet_handler(packet):
            if not self.is_capturing:
                return False  # Stop sniffing
                
            packet_info = self._parse_packet(packet)
            if packet_info:
                self.packet_count += 1
                # Put packet in queue if not full
                if not self.packet_queue.full():
                    self.packet_queue.put(packet_info)
            return True
        
        try:
            # Start sniffing
            sniff(
                iface=self.interface,
                prn=packet_handler,
                store=0,
                count=0,  # 0 = unlimited
                stop_filter=lambda x: not self.is_capturing
            )
        except Exception as e:
            print(f"[!] Error in packet capture: {e}")
            self.is_capturing = False
    
    def _parse_packet(self, packet):
        packet_info = {}
        
        # Check if packet has IP layer
        if IP in packet:
            ip_layer = packet[IP]
            
            # Basic packet info
            packet_info = {
                'timestamp': datetime.now().isoformat(),
                'source_ip': ip_layer.src,
                'destination_ip': ip_layer.dst,
                'protocol': 'Unknown',
                'packet_size': len(packet),
                'ttl': ip_layer.ttl
            }
            
            # Check for TCP
            if TCP in packet:
                tcp_layer = packet[TCP]
                packet_info['protocol'] = 'TCP'
                packet_info['source_port'] = tcp_layer.sport
                packet_info['destination_port'] = tcp_layer.dport
                packet_info['flags'] = tcp_layer.flags
                
            # Check for UDP
            elif UDP in packet:
                udp_layer = packet[UDP]
                packet_info['protocol'] = 'UDP'
                packet_info['source_port'] = udp_layer.sport
                packet_info['destination_port'] = udp_layer.dport
                
            # Check for ICMP
            elif ICMP in packet:
                packet_info['protocol'] = 'ICMP'
                
        return packet_info if packet_info else None
    
    def get_packet(self, timeout=1):
        try:
            return self.packet_queue.get(timeout=timeout)
        except queue.Empty:
            return None
    
    def stop_capture(self):
        self.is_capturing = False
        if self.sniff_thread:
            self.sniff_thread.join(timeout=2)
        print("[✓] Packet capture stopped")
    
    def get_packet_count(self):
        return self.packet_count
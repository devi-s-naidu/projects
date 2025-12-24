import ipaddress
from datetime import datetime

class PacketParser:
    @staticmethod
    def is_private_ip(ip):
        """Check if IP is private"""
        try:
            ip_obj = ipaddress.ip_address(ip)
            return ip_obj.is_private
        except:
            return False
    
    @staticmethod
    def get_protocol_name(protocol_num):
        protocol_map = {
            1: 'ICMP',
            6: 'TCP',
            17: 'UDP',
            2: 'IGMP',
            89: 'OSPF'
        }
        return protocol_map.get(protocol_num, f'Protocol-{protocol_num}')
    
    @staticmethod
    def format_timestamp(timestamp):
        if isinstance(timestamp, str):
            dt = datetime.fromisoformat(timestamp)
        else:
            dt = timestamp
        return dt.strftime('%H:%M:%S.%f')[:-3]
    
    @staticmethod
    def analyze_tcp_flags(flags):
        flag_names = []
        flag_map = {
            0x01: 'FIN',
            0x02: 'SYN',
            0x04: 'RST',
            0x08: 'PSH',
            0x10: 'ACK',
            0x20: 'URG',
            0x40: 'ECE',
            0x80: 'CWR'
        }
        
        for flag_value, name in flag_map.items():
            if flags & flag_value:
                flag_names.append(name)
        
        return ', '.join(flag_names) if flag_names else 'None'
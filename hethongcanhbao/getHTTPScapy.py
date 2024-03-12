from scapy.all import *
from scapy.layers.http import HTTP
def analyze_http(packet):
    if packet.haslayer(TCP) and packet.haslayer(Raw):
        raw_data = packet[Raw].load.decode('utf-8', errors='ignore')
        if 'HTTP' in raw_data:
            print("[+] HTTP Request:")
            print(raw_data)

# Lắng nghe và phân tích các gói tin
sniff(filter="tcp port 80", prn=analyze_http, store=0)

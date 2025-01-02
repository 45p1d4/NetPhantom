
from scapy.all import sniff, IP
from datetime import datetime
import json
from protocol_registry import ProtocolRegistry

class Detector:
    @staticmethod
    def log_traffic(proto_name, parsed_data, packet):
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "protocol": proto_name,
            "src_ip": packet[IP].src if packet.haslayer(IP) else "unknown",
            "dst_ip": packet[IP].dst if packet.haslayer(IP) else "unknown",
            "parsed_data": parsed_data,
        }

        with open("logs/traffic_log.json", "a") as log_file:
            json.dump(log_entry, log_file)
            log_file.write("\n")

        print(f"[{log_entry['timestamp']}] Protocol: {proto_name} | Src: {log_entry['src_ip']} -> Dst: {log_entry['dst_ip']}")

    @staticmethod
    def packet_handler(packet):
        protocol = ProtocolRegistry.identify(packet)
        if protocol:
            parsed_data = protocol.parse(packet)
            if parsed_data:
                Detector.log_traffic(protocol.name, parsed_data, packet)

    @staticmethod
    def start(interface="eth0"):
        print(f"Starting sniffer on {interface}...")
        sniff(iface=interface, prn=Detector.packet_handler, filter="tcp or udp", store=False)

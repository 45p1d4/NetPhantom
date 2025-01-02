
from scapy.all import TCP, Raw
from base_protocol import BaseProtocol

class MQTTProtocol(BaseProtocol):
    name = "mqtt"
    port = 1883

    @classmethod
    def matches(cls, packet):
        return packet.haslayer(TCP) and (packet[TCP].dport == cls.port or packet[TCP].sport == cls.port)

    @classmethod
    def parse(cls, packet):
        raw_data = packet[Raw].load if packet.haslayer(Raw) else None
        if not raw_data:
            return None

        message_type = raw_data[0] >> 4
        return {
            "message_type": message_type,
            "raw_payload": raw_data.hex(),
        }

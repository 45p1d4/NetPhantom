
from scapy.all import TCP, Raw
from base_protocol import BaseProtocol

class ModbusProtocol(BaseProtocol):
    name = "modbus"
    port = 502

    @classmethod
    def matches(cls, packet):
        return packet.haslayer(TCP) and (packet[TCP].dport == cls.port or packet[TCP].sport == cls.port)

    @classmethod
    def parse(cls, packet):
        raw_data = packet[Raw].load if packet.haslayer(Raw) else None
        if not raw_data or len(raw_data) < 7:
            return None

        transaction_id = int.from_bytes(raw_data[0:2], byteorder="big")
        protocol_id = int.from_bytes(raw_data[2:4], byteorder="big")
        length = int.from_bytes(raw_data[4:6], byteorder="big")
        unit_id = raw_data[6]
        function_code = raw_data[7] if len(raw_data) > 7 else None
        data = raw_data[8:] if len(raw_data) > 8 else None

        return {
            "transaction_id": transaction_id,
            "protocol_id": protocol_id,
            "length": length,
            "unit_id": unit_id,
            "function_code": function_code,
            "data": data.hex() if data else None,
        }

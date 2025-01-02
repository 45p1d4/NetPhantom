
class ProtocolRegistry:
    protocols = []

    @classmethod
    def register(cls, protocol):
        cls.protocols.append(protocol)

    @classmethod
    def identify(cls, packet):
        for protocol in cls.protocols:
            if protocol.matches(packet):
                return protocol
        return None

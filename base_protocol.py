
class BaseProtocol:
    name = "base_protocol"
    port = None

    @classmethod
    def matches(cls, packet):
        raise NotImplementedError("Must be implemented in subclasses")

    @classmethod
    def parse(cls, packet):
        raise NotImplementedError("Must be implemented in subclasses")

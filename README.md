# NetPhantom

## Descripción
**NetPhantom** es un detector de tráfico de red modular y extensible desarrollado en Python utilizando la biblioteca **Scapy**. Está diseñado para identificar y analizar 12 protocolos específicos en tiempo real, proporcionando herramientas para el hacking ético, la auditoría y el análisis de redes.

## Características
- **Captura en Tiempo Real**: Intercepta tráfico TCP/UDP desde cualquier interfaz de red.
- **Soporte Modular**: Implementa una arquitectura extensible que facilita la adición de nuevos protocolos.
- **Protocolos Soportados**:
  - Modbus
  - MQTT

- **Proximamente**:
  - OPC-UA
  - RTMP
  - BACnet
  - DNP3
  - FINS
  - SMB
  - Z-Wave
  - RDP
  - HART
  - CAN
- **Registro Detallado**: Genera logs en formato JSON para análisis posterior.

## Instalación
1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/45p1d4/netphantom.git
   cd netphantom
   ```

2. **Configura el entorno**:
   Asegúrate de tener **Python 3.8+** y las siguientes dependencias instaladas:
   ```bash
   pip install scapy
   ```

3. **Estructura del Proyecto**:
   ```
   NetPhantom/
   ├── __init__.py
   ├── base_protocol.py
   ├── protocol_registry.py
   ├── detector.py
   ├── protocols/
   │   ├── __init__.py
   │   ├── modbus_protocol.py
   │   ├── mqtt_protocol.py
   │   └── ...
   ├── logs/
   │   └── traffic_log.json
   ```

## Uso
1. **Registrar Protocolos**:
   Los protocolos ya están registrados por defecto en el archivo principal, pero puedes agregar nuevos en `protocols/`.

2. **Inicia el Detector**:
   ```bash
   python detector.py
   ```

3. **Opciones Personalizables**:
   Cambia la interfaz de red editando `Detector.start()` en `detector.py`:
   ```python
   Detector.start(interface="eth0")
   ```

## Cómo Extender
1. Crea un nuevo archivo en `protocols/` siguiendo la plantilla:
   ```python
   from scapy.all import TCP
   from base_protocol import BaseProtocol

   class NewProtocol(BaseProtocol):
       name = "new_protocol"
       port = 12345

       @classmethod
       def matches(cls, packet):
           return packet.haslayer(TCP) and (packet[TCP].dport == cls.port or packet[TCP].sport == cls.port)

       @classmethod
       def parse(cls, packet):
           raw_data = packet[Raw].load if packet.haslayer(Raw) else None
           return {"raw_payload": raw_data.hex() if raw_data else None}
   ```

2. Registra el protocolo en `__main__.py`:
   ```python
   from protocols.new_protocol import NewProtocol
   ProtocolRegistry.register(NewProtocol)
   ```

## Ejemplo de Salida
```json
{
  "timestamp": "2025-01-01T12:00:00.000Z",
  "protocol": "modbus",
  "src_ip": "192.168.1.10",
  "dst_ip": "192.168.1.20",
  "parsed_data": {
    "transaction_id": 1,
    "protocol_id": 0,
    "length": 6,
    "unit_id": 1,
    "function_code": 3,
    "data": "0a0b0c"
  }
}
```

## Roadmap
- [ ] Soporte para más protocolos.
- [ ] Generación de reportes en formato CSV.
- [ ] Alertas en tiempo real mediante Webhooks.
- [ ] Integración con interfaces gráficas.

## Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un **issue** o envía un **pull request** para mejoras.

## Licencia
Este proyecto está licenciado bajo la **MIT License**. Consulta el archivo `LICENSE` para más detalles.

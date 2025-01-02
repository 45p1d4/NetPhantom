# NetPhantom

## Descripción
**NetPhantom** es un detector de tráfico de red modular y extensible desarrollado en Python utilizando la biblioteca **Scapy**. Está diseñado para identificar y analizar 12 protocolos específicos en tiempo real, proporcionando herramientas para el hacking ético, la auditoría y el análisis de redes.

## Características
- **Captura en Tiempo Real**: Intercepta tráfico TCP/UDP desde cualquier interfaz de red.
- **Soporte Modular**: Implementa una arquitectura extensible que facilita la adición de nuevos protocolos.
- **Protocolos Soportados**:
  - Modbus
  - MQTT
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
   git clone https://github.com/45p1d4/NetPhantom.git
   cd NetPhantom
   
2. **Configura el entorno**: Asegúrate de tener Python 3.8+ y las siguientes dependencias instaladas:
  ```bash
  pip install scapy

3. **Estructura del proyecto**:
NetPhantomr/
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

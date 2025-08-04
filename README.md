# IoT-Based Server Room Monitoring System

This project is a real-time IoT monitoring system built using a Raspberry Pi and Joy-Pi educational platform. It collects sensor data (temperature, humidity, light, sound, GPS) and visualizes it through Grafana while also providing real-time warnings.

### Features
- 🛰️ GPS-based location tracking (Tinkerforge GPS V3)
- 🌡️ Temperature and humidity monitoring (DHT11)
- 💡 Light intensity detection
- 🔊 Sound detection
- ⚠️ Warning system using buzzer and vibration motor
- 📸 Automatic image capture on threshold breach
- 💾 Local logging for each sensor with timestamps
- 📡 MQTT transmission & InfluxDB storage
- 📊 Real-time Grafana dashboard with map & charts
- 🖥️ LCD screen display of key metrics

### Tech Stack
- Python (modular scripts for each sensor)
- Raspberry Pi + Joy-Pi
- InfluxDB, Grafana, MQTT (Mosquitto/public broker)
- Hardware GPIO interfaces (BCM)
- JSON configuration-based thresholds

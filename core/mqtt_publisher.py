import paho.mqtt.client as mqtt
import json

MQTT_BROKER = "localhost"
MQTT_PORT = 1883

client = mqtt.Client()
client.connect(MQTT_BROKER, MQTT_PORT, 60)

def publish_sensor_data(topic, payload_dict):
    """
    Publishes a JSON message to the given MQTT topic.
    :param topic: MQTT topic string (e.g., 'sensor/dht11')
    :param payload_dict: Dictionary to publish as JSON
    """
    try:
        payload = json.dumps(payload_dict)
        client.publish(topic, payload)
    except Exception as e:
        print(f"⚠️ MQTT publish failed ({topic}): {e}")

import paho.mqtt.client as mqtt
import json

MQTT_BROKER = "localhost"
MQTT_PORT = 1883

client = mqtt.Client()
client.username_pw_set("sensor_user", "123") #password 123
client.connect(MQTT_BROKER, MQTT_PORT, 60)

def publish_sensor_data(topic, payload_dict):
    
    try:
        payload = json.dumps(payload_dict)
        client.publish(topic, payload)
    except Exception as e:
        print(f"⚠️ MQTT publish failed ({topic}): {e}")

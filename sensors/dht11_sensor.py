import RPi.GPIO as GPIO
import dht11
import datetime

# Use BOARD mode to match Joy-Pi wiring
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

DHT_PIN = 4  # BCM pin 4 
instance = dht11.DHT11(pin=DHT_PIN)

def read_dht11():
    result = instance.read()
    timestamp = datetime.datetime.utcnow().isoformat()
    if result.is_valid():
        return {
            'timestamp': timestamp,
            'temperature': round(result.temperature, 1),
            'humidity': round(result.humidity, 1)
        }
    else:
        return {
            'timestamp': timestamp,
            'temperature': None,
            'humidity': None,
            'error': 'Failed to read from DHT11 sensor'
        }

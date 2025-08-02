import RPi.GPIO as GPIO
import time
from core.camera_manager import capture_image

# BCM pins used in project
BUZZER_PIN = 18
VIBRATION_PIN = 27

# Setup pins 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(VIBRATION_PIN, GPIO.OUT)

def trigger_alert(duration=1.5):
    """Activate buzzer and vibration for a set duration (seconds)"""
    GPIO.output(BUZZER_PIN, GPIO.HIGH)
    GPIO.output(VIBRATION_PIN, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(BUZZER_PIN, GPIO.LOW)
    GPIO.output(VIBRATION_PIN, GPIO.LOW)

    # Capture photo after alert
    image_path = capture_image()
    print(f"[📷] Image saved: {image_path}")

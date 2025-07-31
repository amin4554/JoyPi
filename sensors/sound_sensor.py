import RPi.GPIO as GPIO
import datetime

# sound_pin wird definiert
sound_pin = 24
# GPIO mode wird auf GPIO.BCM gesetzt
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# sound_pin wird als Eingang festgelegt
GPIO.setup(sound_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def detect_sound():
    state = GPIO.input(sound_pin)
    timestamp = datetime.datetime.utcnow().isoformat()
    return {
        "timestamp": timestamp,
        "sound_detected": state == 0  # LOW means sound triggered
    }
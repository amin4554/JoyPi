from sensors import sound_sensor
from core.log_manager import LogManager
import time

logger = LogManager("sound")
print("Monitoring sound... (Ctrl+C to stop)")

try:
    while True:
        data = sound_sensor.detect_sound()
        print(data)
        logger.log(data)
        time.sleep(0.2)
except KeyboardInterrupt:
    print("Stopped.")
finally:
    logger.close()

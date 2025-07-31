from sensors.light_sensor import LightSensor
from core.log_manager import LogManager
from core.alert_system import trigger_alert
import json
import time
import board
import busio
import adafruit_character_lcd.character_lcd_i2c as character_lcd

sensor = LightSensor()
logger = LogManager("light")

# LCD setup
lcd = character_lcd.Character_LCD_I2C(busio.I2C(board.SCL, board.SDA), 16, 2, 0x21)
lcd.backlight = True

# Load config
with open("config/light_config.json") as f:
    config = json.load(f)

print("Monitoring light sensor... (Ctrl+C to stop)")

try:
    while True:
        data = sensor.read_light()
        lux = data["lux"]
        print(data)
        logger.log(data)

        lcd.message = f"Light: {lux:.1f} lx    "

        if lux < config["min_lux"] or lux > config["max_lux"]:
            trigger_alert()

        time.sleep(2)

except KeyboardInterrupt:
    print("Stopped.")
finally:
    lcd.clear()
    lcd.backlight = False
    logger.close()

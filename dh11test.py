from sensors import dht11_sensor
from core.log_manager import LogManager
from core.alert_system import trigger_alert
import json
import time
import board
import busio
import adafruit_character_lcd.character_lcd_i2c as character_lcd

# LCD setup
lcd = character_lcd.Character_LCD_I2C(busio.I2C(board.SCL, board.SDA), 16, 2, 0x21)
lcd.backlight = True

# Load config
with open("config/dht11_config.json") as f:
    config = json.load(f)

logger = LogManager("dht11")
print("Monitoring DHT11 (Ctrl+C to stop)\n")

try:
    while True:
        data = dht11_sensor.read_dht11()
        print(data)
        logger.log(data)

        temp, hum = data.get("temperature"), data.get("humidity")
        if temp is not None and hum is not None:
            lcd.message = f"T:{temp:.1f}C H:{hum:.1f}%   "
            if temp < config["temperature"]["min"] or temp > config["temperature"]["max"] or \
               hum < config["humidity"]["min"] or hum > config["humidity"]["max"]:
                trigger_alert()
        else:
            lcd.message = "Sensor Error"
        time.sleep(5)
except KeyboardInterrupt:
    print("Stopped.")
finally:
    lcd.clear()
    lcd.backlight = False
    logger.close()

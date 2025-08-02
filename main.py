from sensors import dht11_sensor, sound_sensor
from sensors.light_sensor import LightSensor
from core.alert_system import trigger_alert
from core.log_manager import LogManager
from core.lcd_display import LCDDisplay
from core.influx_writer import write_measurement
from core.mqtt_publisher import publish_sensor_data
from sensors.gps_sensor import GPSSensor
import json
import time

# === Load configs ===
with open("config/dht11_config.json") as f:
    dht_config = json.load(f)
with open("config/light_config.json") as f:
    light_config = json.load(f)

# === Initialize ===
lcd = LCDDisplay()
light_sensor = LightSensor()
gps_sensor = GPSSensor()
dht_logger = LogManager("dht11")
light_logger = LogManager("light")
sound_logger = LogManager("sound")
gps_logger = LogManager("gps")


print("Monitoring all sensors... (Ctrl+C to stop)\n")

try:
    while True:
        # --- Read sensors ---
        dht_data = dht11_sensor.read_dht11()
        light_data = light_sensor.readLight()
        sound_data = sound_sensor.detect_sound()
        gps_data = gps_sensor.read_coordinates()

        # --- Extract values ---
        temp = dht_data.get("temperature")
        hum = dht_data.get("humidity")
        lux = light_data.get("lux")
        sound_detected = sound_data.get("sound_detected", False)
        latitude = gps_data.get("latitude")
        longitude = gps_data.get("longitude")

        # --- Log everything ---
        dht_logger.log(dht_data)
        light_logger.log(light_data)
        sound_logger.log(sound_data)
        gps_logger.log(gps_data)

        # --- Write to InfluxDB and publish via MQTT  ---
        if temp is not None and hum is not None:
            write_measurement("dht11", {
                "temperature": temp,
                "humidity": hum
            })
            publish_sensor_data("sensor/dht11", {"temperature": temp, "humidity": hum})

        if lux is not None:
            write_measurement("light", {
                "lux": lux
            })
            publish_sensor_data("sensor/light", { "lux": lux })

        write_measurement("sound", {
            "sound_detected": int(sound_detected)
        })
        publish_sensor_data("sensor/sound", {"sound_detected": int(sound_detected)})

        if latitude is not None and longitude is not None:
            write_measurement("gps", {
            "latitude": latitude,
            "longitude": longitude
            })
            publish_sensor_data("sensor/gps", {
                "latitude": latitude,
                "longitude": longitude
            })

        # --- Print readable summary ---
        temp_str = f"{temp:.1f}C" if temp is not None else "N/A"
        hum_str = f"{hum:.1f}%" if hum is not None else "N/A"
        lux_str = f"{lux:.1f}lx" if lux is not None else "N/A"
        sound_str = "Yes" if sound_data.get("sound_detected") else "No"
        gps_str = f"Lat: {latitude:.5f}, Lon: {longitude:.5f}" if latitude else "GPS: N/A"
        
        print(f"[{dht_data['timestamp']}] Temp: {temp_str}  Hum: {hum_str}  Light: {lux_str}  Sound: {sound_str}  {gps_str}")


        # --- DHT11 Alerts with image capturing ---
        if temp is not None and (
            temp < dht_config["temperature"]["min"] or
            temp > dht_config["temperature"]["max"]
        ) or hum is not None and (
            hum < dht_config["humidity"]["min"] or
            hum > dht_config["humidity"]["max"]
        ):
            trigger_alert()
            
        # --- Light Alerts with image capturing ---
        if lux is not None:
            if lux < light_config["min_lux"] or lux > light_config["max_lux"]:
                trigger_alert()

        # --- LCD Display ---
        lcd_line1 = f"T:{temp_str} H:{hum_str}"
        lcd_line2 = f"Light:{lux_str}"
        lcd.show_message(lcd_line1, lcd_line2)

        # --- Wait ---
        time.sleep(5)
        lcd.clear()

except KeyboardInterrupt:
    print("\nStopped.")
finally:
    lcd.shutdown()
    gps_sensor.disconnect()
    dht_logger.close()
    light_logger.close()
    sound_logger.close()
    gps_logger.close()              
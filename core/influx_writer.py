from influxdb import InfluxDBClient
import datetime

# === Connection Settings ===
INFLUX_HOST = "localhost"
INFLUX_PORT = 8086
INFLUX_USER = "sensor_user"
INFLUX_PASS = "123"
INFLUX_DB   = "server_room"

# === Initialize client once ===
client = InfluxDBClient(
    host=INFLUX_HOST,
    port=INFLUX_PORT,
    username=INFLUX_USER,
    password=INFLUX_PASS,
    database=INFLUX_DB
)

def write_measurement(sensor_name, fields_dict, tags={"location": "server_room"}):

    timestamp = datetime.datetime.utcnow().isoformat()

    data = [{
        "measurement": sensor_name,
        "tags": tags,
        "time": timestamp,
        "fields": fields_dict
    }]

    try:
        client.write_points(data)
    except Exception as e:
        print(f"⚠️ Failed to write to InfluxDB ({sensor_name}): {e}")

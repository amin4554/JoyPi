from influxdb import InfluxDBClient
import datetime

# Connect to InfluxDB with authentication
client = InfluxDBClient(
    host='localhost',
    port=8086,
    username='sensor_user',
    password='123',
    database='server_room'
)

timestamp = datetime.datetime.utcnow().isoformat()

data = [
    {
        "measurement": "dht11",
        "tags": {
            "location": "server_room"
        },
        "time": timestamp,
        "fields": {
            "temperature": 23.5,
            "humidity": 48.0
        }
    }
]

client.write_points(data)
print("✅ Data written to InfluxDB.")

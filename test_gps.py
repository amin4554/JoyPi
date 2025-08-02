from sensors.gps_sensor import GPSSensor

gps = GPSSensor()

fix, satellites = gps.gps.get_status()
print(f"🛰️  Fix status: {fix}  | Satellites: {satellites}")

coords = gps.read_coordinates()
print(coords)

gps.disconnect()

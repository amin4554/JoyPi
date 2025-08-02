from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_gps_v3 import BrickletGPSV3

class GPSSensor:
    def __init__(self, uid="21Sr", host="localhost", port=4223):
        self.ipcon = IPConnection()
        self.gps = BrickletGPSV3(uid, self.ipcon)
        self.ipcon.connect(host, port)

    def read_coordinates(self):
        try:
            fix, satellites = self.gps.get_status()

            if not fix:
                print("🛰️  GPS has no fix yet (waiting for 2D or 3D lock)...")
                return {
                    "latitude": None,
                    "longitude": None
                }

            coords = self.gps.get_coordinates()
            latitude = coords.latitude / 1000000.0
            longitude = coords.longitude / 1000000.0

            return {
                "latitude": latitude,
                "longitude": longitude
            }
            
        except Exception as e:
            print(f"GPS read failed: {e}")
            return {
                "latitude": None,
                "longitude": None
            }

    def disconnect(self):
        self.ipcon.disconnect()

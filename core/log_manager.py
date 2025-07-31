import os
import time

class LogManager:
    def __init__(self, sensor_name, log_dir="logs"):
        os.makedirs(log_dir, exist_ok=True)
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        self.filename = os.path.join(log_dir, f"{sensor_name}_{timestamp}.log")
        self.file = open(self.filename, "a")
        print(f"Logging to: {self.filename}")

    def log(self, data):
        self.file.write(str(data) + "\n")
        self.file.flush()

    def close(self):
        self.file.close()

from picamera2 import Picamera2
from datetime import datetime
import os
import shutil

picam = Picamera2()

def capture_image(save_dir="captured_images", public_dir="/var/www/html/captured_images"):
    # Create both local and public directories if they don't exist
    os.makedirs(save_dir, exist_ok=True)
    os.makedirs(public_dir, exist_ok=True)

    # Timestamped filename
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    filename = f"{save_dir}/image_{timestamp}.jpg"

    # Capture image
    config = picam.create_still_configuration()
    picam.configure(config)
    picam.start()
    picam.capture_file(filename)
    picam.stop()

    # Also copy it as 'latest.jpg' to the public directory
    public_latest = os.path.join(public_dir, "latest.jpg")
    shutil.copyfile(filename, public_latest)

    return filename

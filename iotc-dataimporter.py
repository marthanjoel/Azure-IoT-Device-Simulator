import json
import random
import time
from iotc import Device

# -----------------------------
# Configuration
# -----------------------------
number_of_messages = 10
interval = 2

with open("iotc-data-dtdls.json") as f:
    devices_config = json.load(f)

def generate_telemetry(content):
    if content["schema"] == "double":
        return round(random.uniform(content.get("minValue",0), content.get("maxValue",100)), content.get("decimalPlaces",2))
    elif content["schema"] == "integer":
        return random.randint(content.get("minValue",0), content.get("maxValue",100))
    else:
        return None

for device_conf in devices_config:
    device = Device(
        scope=device_conf["custom_device_scope"],
        device_id=device_conf["custom_device_id"],
        device_key=device_conf["custom_device_key"]
    )

    device.connect()
    print(f"Connected device {device_conf['custom_device_id']}")

    for i in range(number_of_messages):
        telemetry_data = {}
        for field in device_conf["contents"]:
            val = generate_telemetry(field)
            if val is not None:
                telemetry_data[field["name"]] = val

        print(f"Sending telemetry: {telemetry_data}")
        device.send_telemetry(telemetry_data)
        time.sleep(interval)

    device.disconnect()
    print(f"Device {device_conf['custom_device_id']} finished sending messages.")


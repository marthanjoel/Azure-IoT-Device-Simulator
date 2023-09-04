from iotc import (
    IOTCConnectType,
    IOTCLogLevel,
    IOTCEvents,
    Command,
    CredentialsCache,
    Storage,
)
from iotc.aio import IoTCClient
import json
import sys
from datetime import datetime
import asyncio
import random

number_of_messages = 1

class MemStorage(Storage):
    def retrieve(self):
        return None

    def persist(self, credentials):
        # a further option would be updating config file with latest hub name
        return None
    
class IoTDeviceField():
    def __init__(self, name: str, schema: str, min_value: float, max_value: float, decimal_places: int):
        self.name = name
        self.schema = schema
        self.min_value = min_value
        self.max_value = max_value
        self.decimal_places = decimal_places

    def generate_data(self):
        if self.schema == 'double':
            return round(random.uniform(self.min_value, self.max_value), self.decimal_places)
        elif self.schema == 'integer':
            return random.randint(int(self.min_value),int(self.max_value))
        else:
            raise("Unsupported schema option")

class IoTDevice():
    def __init__(self, device_model_id: str, device_id: str, device_scope: str, device_key: str, device_fields):
        self.device_model_id = device_model_id
        self.device_id = device_id
        self.device_scope = device_scope
        self.device_key = device_key
        self.device_fields = device_fields

    def generate_iot_message(self):
        iot_message = {}
        for field in self.device_fields:
            iot_message[field.name] = field.generate_data()
        return iot_message

async def loadIoTDevices():
    iot_devices = []
    with open('iotc-data-dtdls.json') as f:
        devices = json.load(f)
        for device in devices:
            fields = []
            for field in device['contents']:
                fields.append(IoTDeviceField(field['name'], field['schema'], float(field['minValue']), float(field['maxValue']), int(field['decimalPlaces'])))
            
            iot_devices.append(IoTDevice(device['@id'], device['custom_device_id'], device['custom_device_scope'], device['custom_device_key'], fields))
    return iot_devices

async def connectDeviceToIoTCentral(iot_device: IoTDevice):
    iotc = IoTCClient(iot_device.device_id, iot_device.device_scope, IOTCConnectType.IOTC_CONNECT_DEVICE_KEY, iot_device.device_key, storage=MemStorage())
    iotc.set_log_level(IOTCLogLevel.IOTC_LOGGING_ALL)
    iotc.set_model_id(iot_device.device_model_id)

    await iotc.connect()
    retry = 0 # stop reconnection attempts
    while not iotc.terminated():
        if iotc.is_connected(): 
            for i in range(0, number_of_messages):
                await iotc.send_telemetry(iot_device.generate_iot_message())
            await iotc.disconnect()
        else:
            if retry == 10:
                print("Connection with IoT Central failed.")
            retry += 1
            await iotc.connect()

async def main():
    iot_devices = await loadIoTDevices()
    for iot_device in iot_devices:
        await connectDeviceToIoTCentral(iot_device)

asyncio.run(main())
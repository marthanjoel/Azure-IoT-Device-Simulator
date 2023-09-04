# How to use
1. Install Python 3.7 or higher 
2. Execute 'python3 -m pip install iotc' (or generate an environment if you are a 'advanced' python user and do it on there)
3. Edit the 'number_of_messages' variable in 'iotc-data-importer.py' to set the number of telemetry messages sent per IoT Devices.
4. Create or edit the file called 'iotc-data-dtdls.json' which contains an array of DTDL's. There's 3 custom fields to be added (see last section for a full example):
- custom_device_scope: The IoT Central device scope
- custom_device_id: The IoT Central device id
- custom_device_key: The IoT Central primary or secondary key
4. Run the python file using the command 'python3 iotc-data-importer.py'
5. (Optional) Run the script on an azure function or something alike to set it up on a time interval.

# Limitations
Currently only the double and integer telemetry fields are supported. Any others will fail. You can easily extend this in the 'generate_data' method on the 'IoTDeviceField' class.

# Sample iotc-data-dtdls.json file
```
[{
    "custom_device_scope": "0ne00AD32A9",
    "custom_device_id": "27y100t1y2c",
    "custom_device_key": "nJbjlInYNyDrQ2CFldfB+GFOt0tqL52pMdJSdm7VIsk=",
    "@id": "dtmi:iotcFactsDevWeu001:SuperTrackSection_2zd;1",
    "@type": "Interface",
    "contents": [
        {
            "@id": "dtmi:iotcFactsDevWeu001:SuperTrackSection_2zd:ShuttleCycleTime;1",
            "@type": [
                "Telemetry",
                "NumberValue"
            ],
            "displayName": {
                "en": "Shuttle Cycle Time"
            },
            "name": "ShuttleCycleTime",
            "schema": "double",
            "decimalPlaces": 2,
            "displayUnit": {
                "en": "seconds"
            },
            "maxValue": 3,
            "minValue": 1
        },
        {
            "@id": "dtmi:iotcFactsDevWeu001:SuperTrackSection_2zd:ShuttleCycleRate;1",
            "@type": [
                "Telemetry",
                "NumberValue"
            ],
            "displayName": {
                "en": "Shuttle Cycle Rate"
            },
            "name": "ShuttleCycleRate",
            "schema": "double",
            "decimalPlaces": 2,
            "displayUnit": {
                "en": "per minute"
            },
            "maxValue": 30,
            "minValue": 15
        },
        {
            "@id": "dtmi:iotcFactsDevWeu001:SuperTrackSection_2zd:AverageTimeBetweenCycles;1",
            "@type": [
                "Telemetry",
                "NumberValue"
            ],
            "displayName": {
                "en": "Average Time Between Cycles"
            },
            "name": "AverageTimeBetweenCycles",
            "schema": "integer",
            "decimalPlaces": 0,
            "displayUnit": {
                "en": "milliseconds"
            },
            "maxValue": 2000,
            "minValue": 0
        },
        {
            "@id": "dtmi:iotcFactsDevWeu001:SuperTrackSection_2zd:AverageTotalOffsetMoveTime;1",
            "@type": [
                "Telemetry",
                "NumberValue"
            ],
            "displayName": {
                "en": "Average Total Offset Move Time"
            },
            "name": "AverageTotalOffsetMoveTime",
            "schema": "integer",
            "decimalPlaces": 0,
            "displayUnit": {
                "en": "milliseconds"
            },
            "maxValue": 2000,
            "minValue": 0
        },
        {
            "@id": "dtmi:iotcFactsDevWeu001:SuperTrackSection_2zd:AverageSettlingTime;1",
            "@type": [
                "Telemetry",
                "NumberValue"
            ],
            "displayName": {
                "en": "Average Settling Time"
            },
            "name": "AverageSettlingTime",
            "schema": "integer",
            "decimalPlaces": 0,
            "displayUnit": {
                "en": "milliseconds"
            },
            "maxValue": 50,
            "minValue": 0
        },
        {
            "@id": "dtmi:iotcFactsDevWeu001:SuperTrackSection_2zd:AverageMoveTimeFromLastTarget;1",
            "@type": [
                "Telemetry",
                "NumberValue"
            ],
            "displayName": {
                "en": "Average Move Time From Last Target"
            },
            "name": "AverageMoveTimeFromLastTarget",
            "schema": "integer",
            "decimalPlaces": 0,
            "displayUnit": {
                "en": "milliseconds"
            },
            "maxValue": 1500,
            "minValue": 100
        },
        {
            "@id": "dtmi:iotcFactsDevWeu001:SuperTrackSection_2zd:LastShuffleID;1",
            "@type": [
                "Telemetry",
                "NumberValue"
            ],
            "displayName": {
                "en": "Last Shuffle ID"
            },
            "name": "LastShuffleID",
            "schema": "integer",
            "decimalPlaces": 0,
            "maxValue": 9,
            "minValue": 1
        },
        {
            "@id": "dtmi:iotcFactsDevWeu001:SuperTrackSection_2zd:LastTimeBetweenShuttles;1",
            "@type": [
                "Telemetry",
                "NumberValue"
            ],
            "displayName": {
                "en": "Last Time Between Shuttles"
            },
            "name": "LastTimeBetweenShuttles",
            "schema": "integer",
            "decimalPlaces": 0,
            "displayUnit": {
                "en": "milliseconds"
            },
            "maxValue": 2500,
            "minValue": 200
        },
        {
            "@id": "dtmi:iotcFactsDevWeu001:SuperTrackSection_2zd:LastTotalOffsetMoveTime;1",
            "@type": [
                "Telemetry",
                "NumberValue"
            ],
            "displayName": {
                "en": "Last Total Offset Move Time"
            },
            "name": "LastTotalOffsetMoveTime",
            "schema": "integer",
            "decimalPlaces": 0,
            "displayUnit": {
                "en": "milliseconds"
            },
            "maxValue": 2000,
            "minValue": 200
        },
        {
            "@id": "dtmi:iotcFactsDevWeu001:SuperTrackSection_2zd:LastTotalDwellTime;1",
            "@type": [
                "Telemetry",
                "NumberValue"
            ],
            "displayName": {
                "en": "Last Total Dwell Time"
            },
            "name": "LastTotalDwellTime",
            "schema": "integer",
            "decimalPlaces": 0,
            "displayUnit": {
                "en": "milliseconds"
            },
            "maxValue": 2000,
            "minValue": 1
        },
        {
            "@id": "dtmi:iotcFactsDevWeu001:SuperTrackSection_2zd:LastSettlingTime;1",
            "@type": [
                "Telemetry",
                "NumberValue"
            ],
            "displayName": {
                "en": "Last Settling Time"
            },
            "name": "LastSettlingTime",
            "schema": "integer",
            "decimalPlaces": 0,
            "displayUnit": {
                "en": "milliseconds"
            },
            "maxValue": 50,
            "minValue": 1
        },
        {
            "@id": "dtmi:iotcFactsDevWeu001:SuperTrackSection_2zd:LastMoveTimeFromLastTarget;1",
            "@type": [
                "Telemetry",
                "NumberValue"
            ],
            "displayName": {
                "en": "Last Move Time From Last Target"
            },
            "name": "LastMoveTimeFromLastTarget",
            "schema": "integer",
            "decimalPlaces": 0,
            "displayUnit": {
                "en": "milliseconds"
            },
            "maxValue": 2500,
            "minValue": 200
        },
        {
            "@id": "dtmi:iotcFactsDevWeu001:SuperTrackSection_2zd:PeakPowerSupplyLoad;1",
            "@type": [
                "Telemetry",
                "NumberValue"
            ],
            "displayName": {
                "en": "Peak Power Supply Load"
            },
            "name": "PeakPowerSupplyLoad",
            "schema": "integer",
            "decimalPlaces": 0,
            "displayUnit": {
                "en": "Watt"
            },
            "maxValue": 800,
            "minValue": 200
        },
        {
            "@id": "dtmi:iotcFactsDevWeu001:SuperTrackSection_2zd:AveragePower;1",
            "@type": [
                "Telemetry",
                "NumberValue"
            ],
            "displayName": {
                "en": "Average Power"
            },
            "name": "AveragePower",
            "schema": "integer",
            "decimalPlaces": 0,
            "displayUnit": {
                "en": "Watt"
            },
            "maxValue": 800,
            "minValue": 200
        }
    ],
    "displayName": {
        "en": "SuperTrack Section "
    },
    "@context": [
        "dtmi:iotcentral:context;2",
        "dtmi:dtdl:context;2"
    ]
}]
```
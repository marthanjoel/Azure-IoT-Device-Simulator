# Project Title: Azure IoT  Device Simulator

## Objective
This project simulates multiple IoT devices sending telemetry data to Azure IoT Central. It allows testing dashboards, alerts, and device behavior without needing physical devices.

---

## Tools & Technologies

- **Language**: Python 3.7+
- **Frameworks / Libraries**: iotc (Azure IoT Central Python SDK), Tkinter (for GUI simulation)
- **Simulator**: Custom Python script generating telemetry
- **Dependencies**: Listed in `requirements.txt` (optional: `iotc` package)

---

## Setup Instructions

### 1. Clone the Repository
git clone https://github.com/marthanjoel/Azure-IoT-Central-Device-Simulator.git
cd Azure-IoT-Central-Device-Simulator
2. Create Virtual Environment (Optional)
bash
Copy code
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
bash
Copy code
python3 -m pip install iotc
4. Configure Devices
Edit iotc-data-dtdls.json to include your IoT Central devices:

json
Copy code
[
  {
    "custom_device_scope": "YourDeviceScope",
    "custom_device_id": "Device01",
    "custom_device_key": "YourDeviceKey",
    "@id": "dtmi:yourDevice;1",
    "@type": "Interface",
    "contents": [
      {
        "@id": "dtmi:yourDevice:Temperature;1",
        "@type": ["Telemetry","NumberValue"],
        "name": "Temperature",
        "schema": "double",
        "minValue": 20,
        "maxValue": 30,
        "decimalPlaces": 2,
        "displayName": {"en": "Temperature"}
      }
    ]
  }
]
5. Run the Simulator
bash
Copy code
python3 iotc-data-importer.py
(Optional) Run simulator_gui.py for a Tkinter-based GUI to visualize telemetry messages.

Simulation Details
Sensor Emulated: Temperature, Humidity, Pressure (configurable)

Logic: Random telemetry generated within min/max ranges

Device Count: Multiple devices supported via JSON configuration


--
##Screenshots
Screenshot 1: <img width="1255" height="731" alt="Screenshot from 2025-09-18 09-30-20" src="https://github.com/user-attachments/assets/3ce16975-c4be-4b2f-8f4c-7397b791a14f" />

Screenshot 2: <img width="1255" height="731" alt="Screenshot from 2025-09-18 09-31-21" src="https://github.com/user-attachments/assets/af51b9a5-86e6-44a5-b5da-55d3df2f8097" />


--
##Observations
Simulator generates realistic telemetry for testing dashboards

GUI allows manual and batch telemetry sending

Supports multiple devices and multiple telemetry fields


--


##Future Improvements
Add support for string and Boolean telemetry types

Enable real-time IoT Central telemetry updates from GUI

Add authentication, error handling, and logging features

Extend to Azure Functions for scheduled telemetry generation


----

##Files & Structure
bash
Copy code
Azure-IoT-Central-Device-Simulator/
├── iotc-data-importer.py    
├── iotc-data-dtdls.json     
├── simulator_gui.py         ├── requirements.txt         # Python dependencies
└── README.md                # Project documentation

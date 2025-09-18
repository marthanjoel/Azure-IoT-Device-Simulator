import tkinter as tk
from tkinter import messagebox
import random
import json
import time
# Optional: import your IoT device sending logic here
# from iotc_data_importer import send_telemetry

# -------------------------
# Helper function to generate telemetry
# -------------------------
def generate_telemetry():
    return {
        "Temperature": round(random.uniform(20, 30), 2),
        "Humidity": round(random.uniform(30, 70), 2),
        "Pressure": round(random.uniform(950, 1050), 2)
    }

def send_data():
    data = generate_telemetry()
    # Here you would normally send to Azure IoT Central
    # send_telemetry(data)
    log_text.insert(tk.END, f"Sent telemetry: {data}\n")
    log_text.see(tk.END)

def simulate_multiple(n=5, interval=1):
    for _ in range(n):
        send_data()
        root.update()
        time.sleep(interval)

# -------------------------
# Tkinter GUI Setup
# -------------------------
root = tk.Tk()
root.title("IoT Central Device Simulator")
root.geometry("500x400")

# Title
title_label = tk.Label(root, text="IoT Device Simulator", font=("Arial", 16))
title_label.pack(pady=10)

# Buttons
send_button = tk.Button(root, text="Send Telemetry", command=send_data)
send_button.pack(pady=5)

simulate_button = tk.Button(root, text="Simulate 5 Messages", command=lambda: simulate_multiple(5))
simulate_button.pack(pady=5)

# Log box
log_text = tk.Text(root, height=15, width=60)
log_text.pack(pady=10)

# Exit button
exit_button = tk.Button(root, text="Exit", command=root.destroy)
exit_button.pack(pady=5)

root.mainloop()

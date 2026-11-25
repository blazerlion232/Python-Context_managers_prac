import pandas as pd
import csv

faults = []

with open('test2.csv', 'r') as f:
    reader = csv.DictReader(f)
    headers = reader.fieldnames
    for row in reader:
        temperature = float(row["temperature_c"])
        voltage = float(row["voltage_v"])
        fan_speed = int(row["fan_speed_rpm"])

        if temperature > 80:
            faults.append(row)
        if voltage > 0.8: 
            faults.append(row)
        if fan_speed > 800:
            faults.append(row)

with open('test3.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        temperature = float(row["temperature_c"])
        voltage = float(row["voltage_v"])
        fan_speed = int(row["fan_speed_rpm"])

        if temperature > 80:
            faults.append(row)
        if voltage > 0.8: 
            faults.append(row)
        if fan_speed > 800:
            faults.append(row)

with open("faults.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=headers)

    writer.writeheader()
    writer.writerows(faults)

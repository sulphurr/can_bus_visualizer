# 🚗 CAN Bus Visualizer

A fun and interactive Python-based simulator that mimics real-time data streaming over a car’s **CAN (Controller Area Network) bus** — built with `tkinter`, `matplotlib`, and a sprinkle of engineering drama. 😌

## 🧠 What It Does

This dashboard simulates a car’s core metrics:

- 🌀 **RPM** (Engine speed)
- 🚀 **Vehicle speed**
- 🌡️ **Engine temperature**
- ⚙️ **Gear shifts**
- 🛑 Realistic **mode transitions** like idle, acceleration, braking, and stop

It also visualizes **RPM vs Time** in real-time 📈 and shows status alerts if temperature crosses safe thresholds.

---
##💡 Why This Project?
CAN Bus is the nervous system of a vehicle, enabling microcontrollers to communicate. This project helps visualize how that works — perfect for beginners learning embedded systems, vehicle diagnostics, or just Python with GUI flair!
---

## 🎮 Controls

| Button       | What It Does                     |
|--------------|----------------------------------|
| `Accelerate` | Increases RPM & shifts gears     |
| `Brake`      | Slows the car down               |
| `Stop`       | Drops speed to zero and sets gear to Neutral |
| _(Auto Idle)_| Engine pulses gently in neutral  |

---

## 🛠️ Tech Stack

- `Python 3`
- `Tkinter` for GUI
- `Matplotlib` for real-time RPM chart
- `Threading` to keep UI buttery smooth
- A custom data generator simulating ECU logic and gear ratios

---

## 📸 Demo
<img width="495" height="572" alt="image" src="https://github.com/user-attachments/assets/4189aa88-bb4b-4e7a-bc70-341aee279c94" />
<h6> idle mode </h6>
<p align="center">
  <!-- Add GIF or image link here -->
  <img src="demo.gif" width="600"/>
</p>
<img width="495" height="565" alt="image" src="https://github.com/user-attachments/assets/c283df1c-bde8-4088-b0c7-67d56de8596f" />
<h6> accelerate! </h6>
<img width="492" height="573" alt="image" src="https://github.com/user-attachments/assets/97999df6-fb7c-415a-98e1-235933f2fd4a" />
<h6> hold thy horses </h6>
<img width="493" height="567" alt="image" src="https://github.com/user-attachments/assets/365c1975-ca6d-4e4e-9f26-d5dca47366c5" />
<h6> stop </h6>
---

## 🔧 Setup

```bash
git clone https://github.com/sulphurr/can_bus_visualizer.git
cd can_bus_visualizer
pip install matplotlib
python main.py


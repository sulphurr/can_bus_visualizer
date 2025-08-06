# CAN Bus Visualizer

**CAN Bus Visualizer** is an interactive Python-based simulator that mimics real-time data streaming over a vehicle's Controller Area Network (CAN) bus. Designed with a user-friendly interface using `Tkinter` and real-time plotting with `Matplotlib`, it offers a hands-on introduction to automotive telemetry and data communication.

Ideal for learners and developers interested in embedded systems, vehicle diagnostics, or Python GUI development.

---

## Features

This visual dashboard replicates key automotive signals, including:

- Engine RPM (Revolutions Per Minute)
- Vehicle Speed
- Engine Temperature
- Gear Shifts
- Driving Modes: Idle, Acceleration, Braking, and Stop

Additional capabilities include:

- Real-time plotting of RPM vs Time using Matplotlib
- Warning alerts when temperature exceeds safety thresholds
- Smooth and responsive UI using multi-threading

---

## Project Motivation

In modern vehicles, the CAN bus acts as the internal communication network that allows microcontrollers and devices to exchange data. This project visualizes how such communication translates into meaningful metrics and user actions.

Use cases:

- Educational tool for understanding automotive data flow
- Practice ground for threading and GUI handling in Python
- Lightweight simulation platform for demonstrating vehicle behavior logic

---

## Control Panel

| Button       | Functionality                                     |
|--------------|---------------------------------------------------|
| Accelerate   | Increases RPM and shifts to higher gears          |
| Brake        | Reduces speed and adjusts gear accordingly        |
| Stop         | Halts motion, sets speed to zero, gear to neutral |
| (Auto Idle)  | Simulates a neutral engine pulse without input    |

---

## Tech Stack

- Python 3.x
- Tkinter for the graphical user interface
- Matplotlib for real-time RPM charting
- Python `threading` for asynchronous UI responsiveness
- Custom ECU (Electronic Control Unit) logic simulator for RPM, gear ratio, and temperature dynamics

---

## Demo Screenshots

### Idle Mode
<img width="495" height="572" alt="Idle Mode" src="https://github.com/user-attachments/assets/4189aa88-bb4b-4e7a-bc70-341aee279c94" />

### Acceleration
<img width="495" height="565" alt="Accelerate" src="https://github.com/user-attachments/assets/c283df1c-bde8-4088-b0c7-67d56de8596f" />

### Braking
<img width="492" height="573" alt="Braking" src="https://github.com/user-attachments/assets/97999df6-fb7c-415a-98e1-235933f2fd4a" />

### Stop
<img width="493" height="567" alt="Stop" src="https://github.com/user-attachments/assets/365c1975-ca6d-4e4e-9f26-d5dca47366c5" />

---

## Real-Time Simulation Preview

<p align="center">
  <img src="demo.gif" width="600" alt="Live simulation demo"/>
</p>

---

## Getting Started

To run the simulator locally, follow these steps:

```bash
git clone https://github.com/sulphurr/can_bus_visualizer.git
cd can_bus_visualizer
pip install matplotlib
python main.py

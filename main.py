import threading
import time
import tkinter as tk
from packet_generator import generate_packet
from visualizer_gui import CANVisualizer
from packet_generator import set_drive_mode

def update_data(gui):
    while True:
        packet= generate_packet()
        gui.update_labels(packet)
        time.sleep(1)

root= tk.Tk()
gui= CANVisualizer(root)

control_frame = tk.Frame(root)
control_frame.pack(pady=10)

tk.Button(control_frame, text="Accelerate", width=12, command=lambda: set_drive_mode("accelerate")).pack(side="left", padx=5)
tk.Button(control_frame, text="Brake", width=12, command=lambda: set_drive_mode("brake")).pack(side="left", padx=5)
tk.Button(control_frame, text="Stop", width=12, command=lambda: set_drive_mode("stop")).pack(side="left", padx=5)


thread= threading.Thread(target=update_data, args=(gui,))
thread.daemon= True
thread.start()

root.mainloop()

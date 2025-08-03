import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class CANVisualizer:
    def __init__(self, root):
        self.root= root
        root.title("can bus")

        self.rpm= tk.Label(root, text="RPM: 0", font=("Arial", 17))
        self.rpm.pack()

        self.speed= tk.Label(root, text="Speed: 0 km/h", font=("Arial", 17))
        self.speed.pack()

        self.temp= tk.Label(root, text="Temp: 0 °C", font=("Arial", 17))
        self.temp.pack()

        self.gear= tk.Label(root, text="Gear: --", font=("Arial", 15))
        self.gear.pack()
        self.mode_status = tk.Label(root, text="Mode: Idle", font=("Arial", 12))
        self.mode_status.pack()

        self.status= tk.Label(root, text="Status: Normal", font=("Arial", 14), fg="green")
        self.status.pack(pady=5)

        self.rpm_data= []
        self.time_data= []
        self.time_counter= 0

        self.fig= Figure(figsize=(5, 3), dpi=100)
        self.ax= self.fig.add_subplot(111)
        self.line,=self.ax.plot([], [], label="RPM", color="blue")
        self.ax.set_title("RPM over time")
        self.ax.set_ylabel("RPM")
        self.ax.set_xlabel("time (s)")
        self.ax.set_ylim(0, 7000)
        self.ax.legend()

        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack()


    def update_labels(self, packet):
        rpm= packet['rpm']
        speed= packet['speed']
        tempval= packet['temp']
        mode = packet.get("mode", "idle")
        self.mode_status.config(text=f"Mode: {mode.capitalize()}")

        self.rpm.config(text=f"RPM: {rpm}")
        self.speed.config(text=f"Speed: {speed} km/h")
        self.temp.config(text=f"Temp: {tempval} °C")
        gear= packet.get("gear", "--")
        gear_text= "N" if gear== 0 else str(gear)
        self.gear.config(text=f"Gear: {gear_text}")


        if tempval>100:
            self.temp.config(fg="red")
            self.status.config(text="Status: Overheat", fg="red")
        else:
            self.temp.config(fg="black")
            self.status.config(text="Status: Normal", fg="green")

        
        self.time_counter+= 1
        self.time_data.append(self.time_counter)
        self.rpm_data.append(rpm)

        self.time_data= self.time_data[-20:]
        self.rpm_data= self.rpm_data[-20:]
        
        self.line.set_data(self.time_data, self.rpm_data)
        self.ax.set_xlim(max(0, self.time_counter-20), self.time_counter)
        self.canvas.draw()
#/


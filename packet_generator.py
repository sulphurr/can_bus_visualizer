import random

class CANPacketGenerator:
    def __init__(self):
        self.rpm= 800  #idle rpm
        self.speed= 0
        self.temp= 80
        self.gear= 0  #neutral;)
        self.gear_ratios= [3.5, 2.2, 1.4, 1.0, 0.8]
        self.mode= "idle" 

    def set_mode(self, mode):
        self.mode= mode

    def update(self):
        if self.mode== "accelerate":
            self.rpm= min(6000, self.rpm+random.randint(100, 300))
        elif self.mode== "brake":
            self.rpm= max(800, self.rpm-random.randint(100, 300))
            self.speed= max(0, self.speed-random.randint(5, 10))  # Slows down properly
            if self.speed== 0:
                self.gear= 0

        elif self.mode== "stop":
            self.rpm= max(700, min(1000, self.rpm+random.choice([-50, 0, 50])))
            self.speed= 0
            self.gear= 0
            self.temp= 80+int(self.rpm/1000*random.uniform(1.0, 1.5))
            return {
                "id": "0x120",
                "rpm": self.rpm,
                "speed": self.speed,
                "temp": self.temp,
                "gear": self.gear,
                "mode": self.mode
            }  #n
        else:  #idle rpm
            self.rpm= max(900, min(1000, self.rpm+random.choice([-30, 0, 30])))

        ratio= self.gear_ratios[self.gear - 1] if self.gear>0 else self.gear_ratios[0] 
        #gear0 speed error fix
        
        if self.mode in ["accelerate", "idle"]:
            self.speed = max(0, int((self.rpm / ratio) * 0.05))

        #shifts
        if self.speed<20:
            self.gear=1
        elif self.speed<40:
            self.gear=2
        elif self.speed<60:
            self.gear=3
        elif self.speed<80:
            self.gear=4
        else:
            self.gear=5

        
        self.temp=80+int(self.rpm/1000*random.uniform(1.0, 1.5))
        return{
            "id": "0x120",
            "rpm": self.rpm,
            "speed": self.speed,
            "temp": self.temp,
            "gear": self.gear,
            "mode": self.mode
        }

generator= CANPacketGenerator()

def generate_packet():
    return generator.update()

def set_drive_mode(mode):
    generator.set_mode(mode)

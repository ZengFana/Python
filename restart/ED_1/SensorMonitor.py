class SensorMonitor:
    def __init__(self,name,temp,mode):
        self.name = name
        self.temp = temp
        self.mode = mode
    def check_hardware(self):
        if self.mode == "Sleep":
            print([self.name],"休息中")
        elif self.mode == "Active" and self.temp < 80.0:
            print([self.name],[self.temp],"過熱")
        else:
            print([self.name],[self.temp],"正常")

sensor_logs = [
    {"name": "TX-Antenna", "temp": 85.5, "mode": "Active"},
    {"name": "RX-Antenna", "temp": 60.2, "mode": "Active"},
    {"name": "Power-Unit", "temp": 0.0,  "mode": "Sleep"}
]
for data in sensor_logs:
    name = data["name"]
    temp = data["temp"]
    mode = data["mode"]

    SM = SensorMonitor(name,temp,mode)
    SM.check_hardware()
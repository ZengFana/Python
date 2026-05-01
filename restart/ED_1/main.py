from serial import PortManager

# 這是你要貼在 main.py 裡的原始資料
port_logs = [
    {"port_name": "COM3", "baudrate": 115200, "status": "Connected"},
    {"port_name": "COM4", "baudrate": 9600,   "status": "Connected"},
    {"port_name": "COM5", "baudrate": 115200, "status": "Error"}
]
for data in port_logs:
    pn = data["port_name"]
    br = data["baudrate"]
    st = data["status"]
    pm = PortManager(pn,br,st)
    pm.test_port()
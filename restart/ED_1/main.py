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

pm1 = PortManager("COM6", 115200, "Connected")
pm2 = PortManager("COM7", 9600, "Error")
pm1.test_port(),pm2.test_port()
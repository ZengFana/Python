class PortManager:
    def __init__(self,port_name,baudrate,status):
        self.pn = port_name
        self.br = baudrate
        self.st = status
        return

    def test_port(self):
        if self.st == 'Error':
            print(f"錯誤{self.pn}")
        elif self.br != 115200 and self.st == 'Connected':
            print(f"警告{self.pn}的包率{self.br}錯誤")
        else:
            print(f'正常{self.pn},{self.br},{self.st}')
        return

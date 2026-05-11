from PySide6 import QtWidgets
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Test1.1')
        self.resize(400,400)
        self.ui()

    def ui(self):
        self.Btn1 = QtWidgets.QPushButton(self)
        self.Btn1.setGeometry(20,20,20,10)
        self.Btn1.setText('Button')

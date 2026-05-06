from PyQt6 import QtWidgets
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('add Number')
        self.resize(400, 300)
        self.a = 0
        self.ui()

    def ui(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText('0')
        self.label.setStyleSheet('font-size:20px;')
        self.label.setGeometry(50, 30, 100, 30)

        self.btn1 = QtWidgets.QPushButton(self)
        self.btn1.setText('+1')
        self.btn1.setGeometry(50, 60, 100, 30)
        self.btn1.clicked.connect(self.showNum)

        self.btn2 = QtWidgets.QPushButton(self)
        self.btn2.setText('Res')
        self.btn2.setGeometry(150, 60, 100, 30)
        self.btn2.clicked.connect(self.showRes)

    def showNum(self):
        self.a = self.a + 1
        self.label.setText(str(self.a))

    def showRes(self):
        self.a = 0
        self.label.setText(str(self.a))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())
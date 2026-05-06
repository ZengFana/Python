from PyQt6 import QtWidgets
import sys


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Select Str')
        self.resize(400, 300)
        self.ui()

    def ui(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText('A')
        self.label.setGeometry(50, 30, 100, 30)

        self.btn1 = QtWidgets.QPushButton(self)
        self.btn1.setText('A')
        self.btn1.setGeometry(50, 60, 50, 30)
        self.btn1.clicked.connect(lambda:self.showText('A'))

        self.btn2 = QtWidgets.QPushButton(self)
        self.btn2.setText('B')
        self.btn2.setGeometry(110, 60, 50, 30)
        self.btn2.clicked.connect(lambda:self.showText('B'))

    def showText(self, text):
        self.label.setText(text)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

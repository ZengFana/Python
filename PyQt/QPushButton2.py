from PyQt6 import QtWidgets
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QPushButton")
        self.resize(800, 600)
        self.ui()

    def ui(self):
        self.btn1 = QtWidgets.QPushButton(self)
        self.btn1.setText('Button 1')
        self.btn1.move(50, 50)

        self.btn2 = QtWidgets.QPushButton(self)
        self.btn2.setText('Button 2')
        self.btn2.setGeometry(50, 100, 100, 50)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())
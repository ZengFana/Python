from PyQt6 import QtWidgets
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('XOSIW')
        self.resize(400, 300)
        self.ui()

    def ui(self):
        self.rb_a = QtWidgets.QRadioButton(self)
        self.rb_a.setGeometry(100, 100, 100, 100)
        self.rb_a.setText('A')

        self.rb_b = QtWidgets.QRadioButton(self)
        self.rb_b.setText('B')
        self.rb_b.setGeometry(100, 150, 100, 100)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())
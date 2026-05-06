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
        self.btn1.setGeometry(50,50,100,50)
        self.btn1.setStyleSheet('''
            QPushButton {
                font-size: 20px;
                color: #f00;
                background: #ff0;
                border: 2px solid #000;
            }
            QPushButton:hover {
                color: #ff0;
                background: #f00;
            }
        ''')
        self.btn2 = QtWidgets.QPushButton(self)
        self.btn2.setText('Button 2')
        self.btn2.setGeometry(50, 100, 100, 50)
        self.btn2.setStyleSheet('''
            background:#ff0;
            color:#f00;
            font-size:20px;
            border:2px solid #000;
        ''')
        self.btn3 = QtWidgets.QPushButton(self)
        self.btn3.setText('Button 3')
        self.btn3.setGeometry(50, 150, 100, 50)
        self.btn3.setDisabled(True)
        self.btn4 = QtWidgets.QPushButton(self)
        self.btn4.setText('Button 4')
        self.btn4.setGeometry(50, 200, 100, 50)
        self.btn4.setStyleSheet('''
            QPushButton {
                font-size: 20px;
                color: #f00;
                background: #ff0;
                border: 2px solid #000;
            }
            QPushButton:disabled{
                color: #fff;
                background: #ccc;
                border: 2px solid #aaa;
            }
        ''')
        self.btn4.setDisabled(True)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())
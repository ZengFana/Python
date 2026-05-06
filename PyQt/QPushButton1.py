from PyQt6 import QtWidgets
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QPushButton')
        self.resize(800, 600)
        self.ui()

    def ui(self):
        self.btn = QtWidgets.QPushButton(self) #for Form add QPushButton
        self.btn.setText('我是按鈕')            #Button Text

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())
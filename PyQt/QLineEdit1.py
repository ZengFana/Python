from PySide6 import QtWidgets
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QLineEdit1')
        self.resize(800, 600)
        self.ui()

    def ui(self):
        self.input_1 = QtWidgets.QLineEdit(self)
        self.input_1.setGeometry(20,20,100,20)
        self.input_1.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.input_1.setText('12345')
        self.input_1.setMaxLength(5)

        self.input_2 = QtWidgets.QLineEdit(self)
        self.input_2.setGeometry(20,50,100,20)
        self.input_2.setFocus()

        self.Btn1 = QtWidgets.QPushButton(self)
        self.Btn1.setGeometry(40,150,100,20)
        self.Btn1.setText('按按鈕顯示')
        self.Btn1.clicked.connect(self.showNP)

        self.Label1 = QtWidgets.QLabel(self)
        self.Label1.setGeometry(40,180,100,20)

    def showNP(self):
        self.Label1.setText(str(self.input_1.text()))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
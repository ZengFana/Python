from PyQt6 import QtWidgets
import sys
#
# app = QtWidgets.QApplication(sys.argv)
#
# Form = QtWidgets.QWidget()
# Form.setWindowTitle('XZSW.studio')
# Form.resize(320,240)
#
# label = QtWidgets.QLabel(Form)
# label.setText('Hello World')
#
# Form.show()
# sys.exit(app.exec())

class MyWidet(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WWSS.Widet")
        self.resize(400, 300)
        self.ui()

    def ui(self):
        self.label = QtWidgets.QLabel(self)  # 在Form裡 加入標籤
        self.label.setText("Test")           # 設定標籤文字

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidet()
    Form.show()
    sys.exit(app.exec())
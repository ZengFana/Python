from PyQt6 import QtWidgets
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(320, 240)
        self.setStyleSheet('background:#fcc;')
        self.ui()

    def ui(self):
        self.label = QtWidgets.QLabel(self)          # 在 Form 裡加入 label
        self.label.move(50,50)                       # 移動到 (50, 50) 的位置
        self.label.setText('hello world')            # 寫入文字
        self.label.setStyleSheet('font-size:30px; color:#00c')  # 設定樣式

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())
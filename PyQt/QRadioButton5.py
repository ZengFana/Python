from PyQt6 import QtWidgets
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QRadioButton5')
        self.resize(400, 300)
        self.ui()

    def ui(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(30,30,100,20)

        self.rb_a = QtWidgets.QRadioButton(self)
        self.rb_a.setGeometry(30,60,100,20)
        self.rb_a.setText('A')
        self.rb_b = QtWidgets.QRadioButton(self)
        self.rb_b.setGeometry(150,60,100,20)
        self.rb_b.setText('B')

        self.group = QtWidgets.QButtonGroup(self)   #建立一個群
        self.group.addButton(self.rb_a,1)       #在這個群內加入A,ID設為1
        self.group.addButton(self.rb_b,2)       #在這個群內加入B,ID設為2
        self.group.buttonClicked.connect(self.showId)

    def showId(self):
        self.label.setText(str(self.group.checkedId())) #設定label顯示在按鈕群組中勾選的按鈕的ID

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
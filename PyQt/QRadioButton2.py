from PyQt6 import QtWidgets
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Radio Button 2')
        self.resize(400, 300)
        self.ui()

    def ui(self):
        self.rb_a = QtWidgets.QRadioButton(self)
        self.rb_a.setGeometry(50, 50, 100, 50)
        self.rb_a.setText('A')

        self.rb_b = QtWidgets.QRadioButton(self)
        self.rb_b.setGeometry(100, 50, 100, 50)
        self.rb_b.setText('B')
        self.rb_b.setDisabled(True)     #預設隱藏

        self.group1 = QtWidgets.QButtonGroup(self)
        self.group1.addButton(self.rb_a)
        self.group1.addButton(self.rb_b)

        self.rb_c = QtWidgets.QRadioButton(self)
        self.rb_c.setGeometry(50, 100, 100, 50)
        self.rb_c.setText('C')
        self.rb_c.setChecked(True)          #預設勾選

        self.rb_d = QtWidgets.QRadioButton(self)
        self.rb_d.setGeometry(100, 100, 100, 50)
        self.rb_d.setText('D')

        self.group2 = QtWidgets.QButtonGroup(self)   #把C,D設為同一個群 這樣只能選擇其一
        self.group2.addButton(self.rb_c)
        self.group2.addButton(self.rb_d)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())
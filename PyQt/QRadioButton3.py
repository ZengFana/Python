from PyQt6 import QtWidgets
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Radio Button Color')
        self.resize(400, 300)
        self.ui()

    def ui(self):
        self.rb_a = QtWidgets.QRadioButton(self)
        self.rb_a.setGeometry(100,100,50,30)
        self.rb_a.setText('A')
        self.rb_a.setStyleSheet('''
            QRadioButton{
                color:#00f;
            }
            QRadioButton:hover{
                color:#f00;
            }
        ''')

        self.rb_b = QtWidgets.QRadioButton(self)
        self.rb_b.setGeometry(150,100,50,30)
        self.rb_b.setText('B')
        self.rb_b.setStyleSheet('''
            QRadioButton{
                color:#00f;}
            QRadioButton:hover{
                color:#f00;}
            QRadioButton:checked{        #這邊就是選擇了後的樣子
                color:#0f0;}
        ''')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())
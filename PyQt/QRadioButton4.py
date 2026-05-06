from PyQt6 import QtWidgets
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QRadioButton4')
        self.resize(400, 300)
        self.ui()

    def ui(self):
        self.rb_a = QtWidgets.QRadioButton(self)
        self.rb_a.setText('A')
        self.rb_a.setGeometry(50,50,50,50)
        self.rb_a.setStyleSheet('''
            QRadioButton{
            color: #00f;}
            QRadioButton:hover{
            color: #f00;}
        ''')

        self.rb_b = QtWidgets.QRadioButton(self)
        self.rb_b.setText('B')
        self.rb_b.setGeometry(50,100,50,50)
        self.rb_b.setStyleSheet('''
            QRadioButton{
            color: #00f;}
            QRadioButton:hover{
            color: #f00;}
            QRadioButton:disabled{
            color: #123;}
        ''')
        self.rb_b.setDisabled(True)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())
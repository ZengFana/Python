from PyQt6 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('XX')
Form.resize(320,240)
Form.setStyleSheet('background:#fcc;')

print(Form.width())
print(Form.height())

Form.show()
sys.exit(app.exec())

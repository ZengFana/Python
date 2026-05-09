import sys
from PySide6 import QtWidgets

# 1. 必須先建立 QApplication，這是所有 GUI 程式的起點
app = QtWidgets.QApplication(sys.argv)

# 2. 建立視窗本體，應使用 QWidget 而非直接呼叫 QtWidgets 模組
Form = QtWidgets.QWidget()
Form.setWindowTitle('oxox.studio')
Form.resize(400, 200)

# 建立標籤
label1 = QtWidgets.QLabel(Form)
label1.setText('Hello World')
label1.move(50, 50)

label2 = QtWidgets.QLabel(Form)
label2.setText('Hello World, L2')
label2.setGeometry(50, 80, 100, 100)

# 3. 顯示視窗並進入程式主迴圈
Form.show()
sys.exit(app.exec())
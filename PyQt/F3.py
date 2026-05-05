from PyQt6 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv) # 視窗程式開始

Form = QtWidgets.QWidget() # 建立基底元件
Form.setWindowTitle('oxox.studio')
Form.resize(400, 200)

label1 = QtWidgets.QLabel(Form)
label1.setText('Hello World')
label1.move(50, 50)             # (x,y) 設定 QLabel 在擺放的父元件的x,y 座標 x往右為正,y往下為正,尺寸根據內容自動延伸

label2 = QtWidgets.QLabel(Form)
label2.setText('Hello World,L2')
label2.setGeometry(50, 80, 100, 100) #(x,y,w,h) 設定x,y 座標和長寬尺寸如果超過長寬尺寸 預設會被裁切無法顯示

Form.show() #顯示基底元件
sys.exit(app.exec())
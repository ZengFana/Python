#沒有tools Bar 只專注於左邊控制
from PySide6 import QtWidgets
from PySide6.QtWidgets import (
    QCheckBox,
    QComboBox,
    QDoubleSpinBox,
    QFormLayout,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QScrollArea,
    QSpinBox,
    QStatusBar,
    QVBoxLayout,
    QWidget,
)
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QGround")
        # self.resize(400, 300)
        self.ui1()

    def ui1(self):
        root = QWidget(self)
        self.setCentralWidget(root)

        root_layout = QHBoxLayout(root)
        root_layout.setSpacing(10)

        left = self.blp()
        right = self.BRP()
        thee = self.TRP()
        root_layout.addWidget(left, 0)
        root_layout.addWidget(right,1)
        root_layout.addWidget(thee,2)

    def blp(self):
        scroll = QScrollArea(self)
        scroll.setWidgetResizable(True)
        scroll.setMinimumWidth(400) #限制(設定)最小視窗像素(寬度)
        scroll.setMaximumWidth(500) #限制(設定)最大視窗像素(寬度)
        scroll.setMaximumHeight(300) #同上 最大(高度)
        panel = QWidget()
        scroll.setWidget(panel)
        layout = QVBoxLayout(panel)
        layout.setSpacing(10)

        layout.addWidget(self.Serial())
        layout.addWidget(self.CFG())
        # layout.addWidget(self.Sensor())
        # layout.addWidget(self.Zone())
        return scroll

    def Serial(self):
        group = QGroupBox("Serial")
        layout = QGridLayout(group)
        self.comboCP = QComboBox() #這是下拉式選單
        self.comboCP.setEditable(True)  #能在選單中打字
        self.comboDP = QComboBox()
        self.comboDP.setEditable(True)

        self.spinCB = QSpinBox() #數值調整元件
        self.spinCB.setRange(9600,300000)
        self.spinCB.setSingleStep(1)
        layout.addWidget(QLabel("CD"),0,0)
        layout.addWidget(self.comboCP,0,1)
        layout.addWidget(QLabel("CB"),1,0)
        layout.addWidget(self.spinCB,1,1)
        return group

    def CFG(self):
        group = QGroupBox("CFG")
        layout = QGridLayout(group)

        self.editCP = QLineEdit()
        self.btn_BW = QPushButton("BW..")

        layout.addWidget(QLabel("CFG路徑"),0,0)
        layout.addWidget(self.editCP,0,1)
        layout.addWidget(self.btn_BW,0,2)
        return group

    def BRP(self):
        panel = QWidget()
        layout = QGridLayout(panel)
        layout.setSpacing(10)
        panel.setMinimumWidth(200)
        panel.setMaximumWidth(300)

        layout.addWidget(self.RT1())
        layout.addWidget(self.RT2())
        return panel

    def RT1(self):
        group = QGroupBox("RT1")
        layout = QGridLayout(group)

        self.labelCP = QLabel("2")
        # self.labelCP.setText("CP")
        self.lineCP = QLineEdit()
        self.editCP = QLineEdit()
        layout.addWidget(self.labelCP,0,0)
        layout.addWidget(self.lineCP,0,1)
        layout.addWidget(self.editCP,0,2)
        return group
    def RT2(self):
        RT2 = QGroupBox("RT2")
        layout = QGridLayout(RT2)

        self.Q = QLabel("Q")
        layout.addWidget(self.Q,0,0)
        return RT2
    def TRP(self):
        TG = QGroupBox("TRP")
        layout = QGridLayout(TG)

        layout.addWidget(self.TT1())
        return TG

    def TT1(self):
        TT1 = QGroupBox("TT1")
        layout = QGridLayout(TT1)

        self.Q = QLabel("1")
        self.chackQ = QCheckBox("5")
        self.DoubQ = QDoubleSpinBox()
        self.DoubQ.setRange(1,1000)
        layout.addWidget(self.Q,0,0)
        layout.addWidget(self.chackQ,0,1)
        layout.addWidget(self.DoubQ,0,2)
        return TT1

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

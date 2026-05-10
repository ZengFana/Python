#沒有tools Bar 只專注於左邊控制
from PySide6 import QtWidgets
from PySide6.QtWidgets import (
    # QCheckBox,
    QComboBox,
    # QDoubleSpinBox,
    # QFormLayout,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QScrollArea,
    QSpinBox,
    # QStatusBar,
    QVBoxLayout,
    QWidget,
)
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QGround")
        self.resize(400, 300)
        self.ui1()

    def ui1(self):
        root = QWidget(self)
        self.setCentralWidget(root)

        root_layout = QHBoxLayout(root)
        root_layout.setSpacing(10)

        left = self.blp()
        root_layout.addWidget(left, 0)

    def blp(self):
        scroll = QScrollArea(self)
        scroll.setWidgetResizable(True)
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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

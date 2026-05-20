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
    QSlider,
)
from PySide6.QtCore import Qt
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NyWindow")
        self.UIG1()

    def UIG1(self):
        user = QWidget(self)
        self.setCentralWidget(user)

        user_layout = QHBoxLayout(user)
        user_layout.setSpacing(10)

        left = self.BLP()
        min = self.TRP()
        user_layout.addWidget(left,0)
        user_layout.addWidget(min,1)

    def BLP(self):
        scroll = QScrollArea(self)
        scroll.setWidgetResizable(True)
        scroll.setMaximumSize(300,300)
        scroll.setMinimumSize(200,200)
        panel = QWidget()
        scroll.setWidget(panel)
        layout = QVBoxLayout(panel)
        layout.setSpacing(10)

        layout.addWidget(self.CGG())
        layout.addWidget(self.Serial1())
        layout.addWidget(self.select())
        return scroll

    def CGG(self):
        group = QGroupBox('CGG')
        layout = QGridLayout(group)
        self.comboCP = QComboBox()
        self.comboCP.setEditable(True)
        self.comboDP = QComboBox()
        self.comboDP.setEditable(True)

        self.spinCB = QSpinBox()
        self.spinCB.setRange(100,3000)
        self.spinCB.setSingleStep(100)
        layout.addWidget(QLabel('CP'),0,0)
        layout.addWidget(self.comboCP,0,1)
        layout.addWidget(QLabel('DP'),1,0)
        layout.addWidget(self.comboDP,1,1)
        layout.addWidget(QLabel('CB'),2,0)
        layout.addWidget(self.spinCB,2,1)
        return group

    def TRP(self):
        pen = QWidget()
        # scroll.setWidget(pen)
        layout = QVBoxLayout(pen)


        # self.QLabel = QLabel('QLabel')
        # self.QLabel.setText('QLabel')

        layout.addWidget(self.Serial())
        layout.addWidget(self.CGG())
        # layout.addWidget(self.Serial,0,1)
        return pen

    def Serial(self):
        group = QGroupBox('Serial')
        layout = QGridLayout(group)
        self.QLabel = QLabel('w')
        self.QLabel.setText('Serial1')

        layout.addWidget(self.QLabel,0,0)
        return group
    def Serial1(self):
        group = QGroupBox('Serial')
        layout = QGridLayout(group)
        self.QLabel = QLabel('w')
        self.QLabel.setText('Serial2')
        return group
    def select(self):
        group = QGroupBox('Select')
        slider = QSlider(Qt.Horizontal)
        slider.setRange(0,100)
        slider.setTickPosition(QSlider.TicksBelow)
        slider.setTickInterval(1)
        layout = QGridLayout(group)

        self.selCP = QSpinBox()
        self.sliderCP = QSlider(Qt.Horizontal)
        self.label1 = QLabel('w')
        # self.label1.setText(f'{slider.value}')
        # sliderCP.valueChanged.connect()
        # self.selCP = QLineEdit()
        # self.selCP.setRange(100,3000)
        layout.addWidget(self.label1,0,0)
        layout.addWidget(self.sliderCP,0,1)


        return group

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
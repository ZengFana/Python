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
    QPlainTextEdit,
)
from PySide6.QtCore import Qt
import sys
from datetime import datetime

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
        wgp = self.show_window()
        user_layout.addWidget(left,0)
        user_layout.addWidget(min,1)
        user_layout.addWidget(wgp,2)


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
        self.comboCP.addItems(['0','1','2','3','4','5'])
        self.comboDP = QComboBox()
        self.comboDP.setEditable(True)
        self.comboDP.addItems(['0','1','2','3','4','5'])

        self.labelCP = QLabel('')
        self.labelDP = QLabel('')
        def handle_charge():
            current_val = self.comboCP.currentText()
            self.labelCP.setText(current_val)
            self.add_log(f"CGG 設定更新為: {current_val}")
        self.comboCP.activated.connect(handle_charge)

        self.spinCB = QSpinBox()
        self.spinCB.setRange(100,3000)
        self.spinCB.setSingleStep(100)
        layout.addWidget(QLabel('CP'),0,0)
        layout.addWidget(self.comboCP,0,1)
        layout.addWidget(self.labelCP,0,2)
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
        # layout.addWidget(self.CGG())
        # layout.addWidget(self.Serial,0,1)
        return pen

    def Serial(self):
        group = QGroupBox('Serial')
        layout = QGridLayout(group)
        self.QLabel = QLabel('w')
        self.QLabel.setText('Serial1')
        self.sliderCP.sliderReleased.connect(
            lambda: self.add_log(f"Slider 數值已調整至: {self.sliderCP.value()}")
        )

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
        slider.setTickInterval(10)
        layout = QGridLayout(group)

        self.selCP = QSpinBox()
        self.sliderCP = QSlider(Qt.Horizontal)
        self.label1 = QLineEdit('0')
        self.label1.setFixedWidth(50)
        self.sliderCP.valueChanged.connect(lambda v: self.label1.setText(str(v)))
        self.label1.textChanged.connect(self.update_silder)
        # self.label1.setText(f'{slider.value}')
        # sliderCP.valueChanged.connect()
        # self.selCP = QLineEdit()
        # self.selCP.setRange(100,3000)
        layout.addWidget(self.label1,0,0)
        layout.addWidget(self.sliderCP,0,1)


        return group
    def update_silder(self):
        text = self.label1.text()
        if text.isdigit():
            value = int(text)
            if 0 <= value <= 100:
                self.sliderCP.blockSignals(True)
                self.sliderCP.setValue(value)
                self.sliderCP.blockSignals(False)
                self.add_log(f"手動輸入數值: {value}")

    def show_window(self):
        group = QGroupBox('系統日誌')
        layout = QVBoxLayout(group)

        self.log_output = QPlainTextEdit()
        self.log_output.setReadOnly(True)
        self.log_output.setPlaceholderText('系統操作紀錄..')

        clear_but = QPushButton('清除')
        clear_but.clicked.connect(self.log_output.clear)
        layout.addWidget(self.log_output)
        layout.addWidget(clear_but)
        return group
    def add_log(self, message):
        current_time = datetime.now().strftime('%H:%M:%S')
        self.log_output.appendPlainText(f'[{current_time}] {message}')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
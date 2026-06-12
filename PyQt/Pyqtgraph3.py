import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, \
    QLineEdit
from PySide6.QtCore import Qt
import pyqtgraph as pg


class RadarRangeSettingApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("雷達自定義範圍設定練習")
        self.resize(800, 600)
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        # 1. 主畫布與頂層垂直排版
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        self.top_level_layout = QVBoxLayout(main_widget)

        # =======================================================
        # 2. 新增：自定義範圍的文字輸入列 (使用水平排版 QHBoxLayout)
        # =======================================================
        range_layout = QHBoxLayout()

        # X 軸設定元件
        range_layout.addWidget(QLabel("X軸 最小值:"))
        self.input_x_min = QLineEdit("-5.0")  # 括號內填寫預設顯示的文字
        self.input_x_min.setFixedWidth(60)  # 固定輸入框的寬度，讓排版更美觀
        range_layout.addWidget(self.input_x_min)

        range_layout.addWidget(QLabel("X軸 最大值:"))
        self.input_x_max = QLineEdit("5.0")
        self.input_x_max.setFixedWidth(60)
        range_layout.addWidget(self.input_x_max)

        # Y 軸設定元件 (雷達前方距離)
        range_layout.addWidget(QLabel("Y軸 最小值:"))
        self.input_y_min = QLineEdit("0.0")
        self.input_y_min.setFixedWidth(60)
        range_layout.addWidget(self.input_y_min)

        range_layout.addWidget(QLabel("Y軸 最大值:"))
        self.input_y_max = QLineEdit("10.0")
        self.input_y_max.setFixedWidth(60)
        range_layout.addWidget(self.input_y_max)

        # 套用設定的按鈕
        self.btn_apply = QPushButton("🎯 套用新範圍")
        # 利用 Signal-Slot 綁定點擊事件
        self.btn_apply.clicked.connect(self.apply_custom_range)
        range_layout.addWidget(self.btn_apply)

        # 將這一整排自定義範圍的格子，塞進最上方的垂直排版中
        self.top_level_layout.addLayout(range_layout)

        # =======================================================
        # 3. 繪圖區域 (維持原樣)
        # =======================================================
        self.plot2d = pg.PlotWidget()
        self.plot2d.showGrid(x=True, y=True)

        # 先初始化一個預設範圍
        self.plot2d.setXRange(-5.0, 5.0)
        self.plot2d.setYRange(0.0, 10.0)

        self.top_level_layout.addWidget(self.plot2d)

    # =======================================================
    # 4. 核心功能：讀取輸入框內容，並改動畫布部位
    # =======================================================
    def apply_custom_range(self):
        """ 當使用者按下按鈕時，讀取文字框，動態改變畫布觀測範圍 """
        try:
            # 透過 .text() 撈出使用者在輸入框打的文字，並轉成 float 數字
            x_min = float(self.input_x_min.text())
            x_max = float(self.input_x_max.text())
            y_min = float(self.input_y_min.text())
            y_max = float(self.input_y_max.text())

            print(f"Log: 收到使用者自定義範圍 -> X:({x_min} ~ {x_max}), Y:({y_min} ~ {y_max})")

            # 【改動部位】動態改變 PlotWidget 畫布的內部數學座標軸刻度
            self.plot2d.setXRange(x_min, x_max)
            self.plot2d.setYRange(y_min, y_max)

            # 強迫視窗重繪，確保刻度數字立即刷新
            self.plot2d.update()

        except ValueError:
            # 防呆機制：如果使用者不小心輸入了英文或空白，導致 float() 轉換失敗，程式不會崩潰
            print("Error: 輸入格式錯誤！請確保輸入框內填寫的是正確的數字。")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RadarRangeSettingApp()
    window.show()
    sys.exit(app.exec())
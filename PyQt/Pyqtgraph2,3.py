import sys
import numpy as np
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, \
    QLineEdit
from PySide6.QtCore import QThread, Signal, Qt
import pyqtgraph as pg
import pyqtgraph.opengl as gl


# =====================================================================
# 1. 背景執行緒：模擬雷達即時數據生成器 (Thread)
# =====================================================================
class RealTimeRadarThread(QThread):
    data_signal = Signal(np.ndarray)

    def __init__(self):
        super().__init__()
        self.running = True

    def run(self):
        t = 0.0
        while self.running:
            # 模擬一個當前移動的目標點 (X, Y, Z)
            current_x = 1.5 * np.sin(t)
            current_y = 1.0 + t * 0.5  # 目標逐漸遠離雷達
            current_z = 0.8 + 0.1 * np.cos(t * 3)

            # 如果走太遠就重頭來
            if current_y > 9.0:
                t = 0.0
                continue

            current_target = np.array([[current_x, current_y, current_z]])
            self.data_signal.emit(current_target)
            self.msleep(100)  # 10Hz 更新率
            t += 0.1

    def stop(self):
        self.running = False
        self.wait()


# =====================================================================
# 2. 前端主視窗：結合「自定義範圍」與「資料庫比對」
# =====================================================================
class IntegratedRadarConsole(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("毫米波雷達終端控制台 - 完整功能整合版")
        self.resize(1200, 750)

        # 奪回視窗鍵盤焦點，確保系統操作暢通
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        # -------------------------------------------------------------
        # 模擬資料庫 (Database Mock)
        # 預存一條歷史安全路徑，點擊按鈕後會撈出這條資訊並打在畫布上
        # -------------------------------------------------------------
        self.mock_database_trajectory = np.array([
            [0.0, 1.0, 0.8], [0.2, 2.0, 0.8], [0.0, 3.0, 0.8],
            [-0.3, 4.0, 0.8], [0.0, 5.0, 0.8], [0.3, 6.0, 0.8],
            [0.0, 7.0, 0.8], [-0.2, 8.0, 0.8], [0.0, 9.0, 0.8]
        ])

        # 主配置畫布與頂層垂直排版
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        self.top_level_layout = QVBoxLayout(main_widget)

        # =============================================================
        # 功能一組裝：自定義範圍輸入列 (QLineEdit + Layout)
        # =============================================================
        range_layout = QHBoxLayout()
        range_layout.addWidget(QLabel("<b>[畫布範圍設定]</b>"))

        range_layout.addWidget(QLabel("X Min:"))
        self.input_x_min = QLineEdit("-5.0")
        self.input_x_min.setFixedWidth(50)
        range_layout.addWidget(self.input_x_min)

        range_layout.addWidget(QLabel("X Max:"))
        self.input_x_max = QLineEdit("5.0")
        self.input_x_max.setFixedWidth(50)
        range_layout.addWidget(self.input_x_max)

        range_layout.addWidget(QLabel("Y Min:"))
        self.input_y_min = QLineEdit("0.0")
        self.input_y_min.setFixedWidth(50)
        range_layout.addWidget(self.input_y_min)

        range_layout.addWidget(QLabel("Y Max:"))
        self.input_y_max = QLineEdit("10.0")
        self.input_y_max.setFixedWidth(50)
        range_layout.addWidget(self.input_y_max)

        self.btn_apply_range = QPushButton("🎯 套用新範圍")
        self.btn_apply_range.clicked.connect(self.apply_custom_range)
        range_layout.addWidget(self.btn_apply_range)

        # 將第一排控制列塞入大排版
        self.top_level_layout.addLayout(range_layout)

        # =============================================================
        # 功能二組裝：資料庫控制與分析結果列 (Database Control)
        # =============================================================
        db_layout = QHBoxLayout()
        db_layout.addWidget(QLabel("<b>[資料庫數據流]</b>"))

        self.btn_load_db = QPushButton("📊 撈取資料庫歷史軌跡")
        self.btn_load_db.clicked.connect(self.load_database_trajectory)
        db_layout.addWidget(self.btn_load_db)

        self.lbl_analysis_status = QLabel("分析狀態：等待載入資料庫路徑...")
        self.lbl_analysis_status.setStyleSheet(
            "color: yellow; background-color: #222; padding: 5px; border-radius: 3px;")
        db_layout.addWidget(self.lbl_analysis_status, stretch=1)

        # 將第二排控制列塞入大排版
        self.top_level_layout.addLayout(db_layout)

        # =============================================================
        # 繪圖區域組裝：2D 與 3D 多畫布疊加設定 (PlotWidget & GLViewWidget)
        # =============================================================
        charts_layout = QHBoxLayout()

        # ---- 左邊：2D 畫布內容設定 ----
        self.plot2d = pg.PlotWidget()
        self.plot2d.showGrid(x=True, y=True)
        self.plot2d.addLegend()

        # 疊加物件 A：即時雷達目標點 (綠色圓點)
        self.scatter2d_rt = pg.ScatterPlotItem(size=12, brush=pg.mkBrush(0, 255, 0), name="即時目標 (Radar)")
        self.plot2d.addItem(self.scatter2d_rt)

        # 疊加物件 B：資料庫歷史軌跡線 (紅色虛線)
        self.line2d_db = pg.PlotDataItem(pen=pg.mkPen('r', width=2, style=Qt.PenStyle.DashLine),
                                         name="資料庫歷史軌跡 (DB)")
        self.plot2d.addItem(self.line2d_db)

        charts_layout.addWidget(self.plot2d)

        # ---- 右邊：3D 畫布內容設定 ----
        self.plot3d = gl.GLViewWidget()
        self.plot3d.setCameraPosition(distance=12, elevation=25, azimuth=45)
        self.plot3d.addItem(gl.GLGridItem())  # 3D 地面網格

        # 疊加物件 C：3D 即時雷達點 (藍綠色立方點)
        self.scatter3d_rt = gl.GLScatterPlotItem(size=10, color=(0.0, 1.0, 1.0, 1.0))
        self.plot3d.addItem(self.scatter3d_rt)

        # 疊加物件 D：3D 資料庫歷史軌跡線 (紅色立體線段)
        self.line3d_db = gl.GLLinePlotItem(width=3, color=(1.0, 0.0, 0.0, 1.0), mode='line_strip')
        self.plot3d.addItem(self.line3d_db)

        charts_layout.addWidget(self.plot3d)

        # 將圖表區加入大排版
        self.top_level_layout.addLayout(charts_layout)

        # -------------------------------------------------------------
        # 啟動背景資料執行緒
        # -------------------------------------------------------------
        self.radar_thread = RealTimeRadarThread()
        self.radar_thread.data_signal.connect(self.handle_incoming_data)
        self.radar_thread.start()

        # 儲存最新的即時點座標，用於分析比對
        self.latest_point = np.array([0.0, 0.0, 0.0])

    # =============================================================
    # 功能一的實作：動態調整畫布範圍 (setXRange / setYRange)
    # =============================================================
    def apply_custom_range(self):
        """ 讀取 QLineEdit 的文字，改動 2D 畫布的刻度範圍 """
        try:
            x_min = float(self.input_x_min.text())
            x_max = float(self.input_x_max.text())
            y_min = float(self.input_y_min.text())
            y_max = float(self.input_y_max.text())

            # 改動部位：2D 畫布的數學座標軸範圍
            self.plot2d.setXRange(x_min, x_max)
            self.plot2d.setYRange(y_min, y_max)
            self.plot2d.update()
            print(f"Log: 成功改動 2D 畫布視界範圍為 X:({x_min}~{x_max}), Y:({y_min}~{y_max})")
        except ValueError:
            print("Error: 請輸入正確的數字格式！")

    # =============================================================
    # 功能二的實作：載入資料庫數據並打在畫布上
    # =============================================================
    def load_database_trajectory(self):
        """ 從模擬資料庫撈出軌跡，塞入 2D/3D 的 Line 物件中顯示 """
        print("Log: 正在從資料庫提取歷史特徵數據...")

        # 提取資料庫數據並打在 2D 軌跡線上
        db_x = self.mock_database_trajectory[:, 0]
        db_y = self.mock_database_trajectory[:, 1]
        self.line2d_db.setData(x=db_x, y=db_y)

        # 塞入 3D 軌跡線
        self.line3d_db.setData(pos=self.mock_database_trajectory)

        self.lbl_analysis_status.setText("分析狀態：資料庫軌跡載入成功！開始與即時雷達進行軌跡誤差分析...")

    # =============================================================
    # 數據流神經中樞：接收即時點雲 ➔ 刷新畫布 ➔ 觸發比對分析
    # =============================================================
    def handle_incoming_data(self, point):
        self.latest_point = point[0]

        # 1. 刷新 2D 與 3D 畫布上的「即時雷達點」內容
        self.scatter2d_rt.setData(x=[self.latest_point[0]], y=[self.latest_point[1]])
        self.scatter3d_rt.setData(pos=point)
        self.plot3d.update()  # 強制刷新 3D 畫面防止偏移

        # 2. 如果資料庫資料已經被打在畫布上了，就啟動即時分析演算法
        if self.line2d_db.xData is not None:
            self.perform_trajectory_analysis()

    def perform_trajectory_analysis(self):
        """ 分析演算法：計算雷達即時點與資料庫歷史軌跡的最小歐氏距離 """
        rt_xy = self.latest_point[:2]
        db_xy = self.mock_database_trajectory[:, :2]

        # 矩陣運算計算距離
        distances = np.linalg.norm(db_xy - rt_xy, axis=1)
        min_dist = np.min(distances)

        # 依據分析結果改動 UI 文字與顏色
        if min_dist < 0.6:
            self.lbl_analysis_status.setText(f"✅ 軌跡正常 (與資料庫特徵誤差: {min_dist:.2f} 米)")
            self.lbl_analysis_status.setStyleSheet("color: lightgreen; background-color: #222; padding: 5px;")
        else:
            self.lbl_analysis_status.setText(f"⚠️ 警告！目標偏離安全歷史軌跡！(偏差: {min_dist:.2f} 米)")
            self.lbl_analysis_status.setStyleSheet(
                "color: red; background-color: #222; padding: 5px; font-weight: bold;")

    def closeEvent(self, event):
        self.radar_thread.stop()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = IntegratedRadarConsole()
    window.show()
    sys.exit(app.exec())
import sys
import numpy as np
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel
from PySide6.QtCore import QThread, Signal
import pyqtgraph as pg
import pyqtgraph.opengl as gl


# ==========================================
# 1. 背景執行緒：模擬數據生成器 (代替 Serial)
# ==========================================
class SimulatedRadarThread(QThread):
    # 定義一個信號，每次發送一個包含多個 (X, Y, Z) 座標的 numpy 陣列
    data_signal = Signal(np.ndarray)

    def __init__(self):
        super().__init__()
        self.running = True

    def run(self):
        # 模擬雷達不斷轉動、物體移動的軌跡
        angle = 0.0
        while self.running:
            # 模擬生成 50 個點的隨機點雲（雜訊）
            num_points = 50
            noise = np.random.normal(0, 0.1, (num_points, 3))

            # 模擬一個主要移動目標（例如一個人在走動，繞圓圈並上下起伏）
            target_x = 2.0 * np.cos(angle)
            target_y = 3.0 + 1.0 * np.sin(angle)
            target_z = 0.5 + 0.2 * np.sin(angle * 2)
            target_point = np.array([[target_x, target_y, target_z]])

            # 合併目標與雜訊數據
            all_points = noise + np.array([0, 3.0, 0])  # 讓雜訊集中在前方
            all_points = np.vstack([all_points, target_point])

            # 射出信號發送給主執行緒
            self.data_signal.emit(all_points)

            # 模擬雷達更新率（例如每秒更新 10 次 = 10Hz）
            self.msleep(100)
            angle += 0.05

    def stop(self):
        self.running = False
        self.wait()


# ==========================================
# 2. 前端主視窗：佈局與 2D/3D 繪圖
# ==========================================
class RadarMonitorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("毫米波雷達 2D/3D 點雲模擬練習")
        self.resize(1000, 600)

        # 建立主畫布 Widget 與水平佈局
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QHBoxLayout(main_widget)

        # ---- 左半邊：2D 繪圖區域 ----
        left_container = QWidget()
        left_layout = QVBoxLayout(left_container)
        left_layout.addWidget(QLabel("<b>2D Top-Down View (X-Y 平面)</b>"))

        self.plot2d = pg.PlotWidget()
        self.plot2d.setXRange(-5, 5)
        self.plot2d.setYRange(0, 10)
        self.plot2d.setLabel('bottom', 'X 座標 (米)')
        self.plot2d.setLabel('left', 'Y 座標 (米)')
        # 建立 2D 散點圖項目
        self.scatter2d = pg.ScatterPlotItem(size=8, pen=pg.mkPen(None), brush=pg.mkBrush(0, 255, 0, 200))
        self.plot2d.addItem(self.scatter2d)
        left_layout.addWidget(self.plot2d)

        # ---- 右半邊：3D 繪圖區域 ----
        right_container = QWidget()
        right_layout = QVBoxLayout(right_container)
        right_layout.addWidget(QLabel("<b>3D Point Cloud View (X-Y-Z 空間)</b>"))

        self.plot3d = gl.GLViewWidget()
        self.plot3d.setCameraPosition(distance=12, elevation=30, azimuth=45)
        # 加入 3D 網格
        grid = gl.GLGridItem()
        grid.setSize(10, 10, 1)
        grid.setSpacing(1, 1, 1)
        self.plot3d.addItem(grid)
        # 建立 3D 散點圖項目
        self.scatter3d = gl.GLScatterPlotItem(size=5, color=(0.0, 1.0, 1.0, 0.8), pxMode=True)
        self.plot3d.addItem(self.scatter3d)
        right_layout.addWidget(self.plot3d)

        # 將左右兩個容器加入主配置
        main_layout.addWidget(left_container, stretch=1)
        main_layout.addWidget(right_container, stretch=1)

        # ---- 啟動背景模擬執行緒 ----
        self.radar_thread = SimulatedRadarThread()
        # 連接信號到更新畫面的 Slot 函式
        self.radar_thread.data_signal.connect(self.update_plots)
        self.radar_thread.start()

    def update_plots(self, points):
        """ 當收到新數據時，同步更新 2D 與 3D 畫面 """
        # 1. 更新 2D 散點圖 (只需取 X 和 Y 兩欄)
        x_data = points[:, 0]
        y_data = points[:, 1]
        self.scatter2d.setData(x=x_data, y=y_data)

        # 2. 更新 3D 點雲
        self.scatter3d.setData(pos=points)

        # 關鍵：強制通知 3D 視窗重繪，防止切換全螢幕時可能產生的黑畫面 Bug
        self.plot3d.update()

    def closeEvent(self, event):
        """ 當視窗關閉時，安全停止執行緒 """
        self.radar_thread.stop()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RadarMonitorApp()
    window.show()
    sys.exit(app.exec())
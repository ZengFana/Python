import sys
import numpy as np
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, \
    QComboBox
from PySide6.QtCore import QThread, Signal, Qt
import pyqtgraph as pg
import pyqtgraph.opengl as gl


# ==========================================
# 1. 背景執行緒：模擬數據生成器 (維持不變)
# ==========================================
class SimulatedRadarThread(QThread):
    data_signal = Signal(np.ndarray)

    def __init__(self):
        super().__init__()
        self.running = True

    def run(self):
        angle = 0.0
        while self.running:
            num_points = 60
            noise = np.random.normal(0, 0.15, (num_points, 3))

            # 模擬雷達前方的主移動目標
            target_x = 2.5 * np.cos(angle)
            target_y = 4.0 + 1.0 * np.sin(angle)
            target_z = 0.5 + 0.3 * np.sin(angle * 2)
            target_point = np.array([[target_x, target_y, target_z]])

            all_points = noise + np.array([0, 4.0, 0])
            all_points = np.vstack([all_points, target_point])

            self.data_signal.emit(all_points)
            self.msleep(100)  # 10Hz 更新率
            angle += 0.05

    def stop(self):
        self.running = False
        self.wait()


# ==========================================
# 2. 前端主視窗：支援選單、全螢幕、Esc退出與防偏移
# ==========================================
class AdvancedRadarApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("雷達控制台 - 2D/3D 切換與全螢幕優化練習")
        self.resize(1100, 700)
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        # 基礎狀態變數
        self.is_fullscreen_mode = False

        # --- 主畫布與主要排版 ---
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        # 頂層採用垂直排版：上方放控制列，下方放繪圖區
        self.top_level_layout = QVBoxLayout(main_widget)

        # ==========================================
        # 控制列設置 (下拉選單與全螢幕按鈕)
        # ==========================================
        control_layout = QHBoxLayout()

        control_layout.addWidget(QLabel("<b>顯示模式選擇：</b>"))
        self.mode_combo = QComboBox()
        self.mode_combo.addItems(["同時顯示 (2D + 3D)", "僅顯示 2D 視窗", "僅顯示 3D 視窗"])
        self.mode_combo.currentIndexChanged.connect(self.handle_view_mode_change)
        control_layout.addWidget(self.mode_combo)

        self.btn_fullscreen = QPushButton("進入當前視窗全螢幕 (或按 Esc 退出)")
        self.btn_fullscreen.clicked.connect(self.toggle_fullscreen_view)
        control_layout.addWidget(self.btn_fullscreen)

        # 將控制列加入最上方
        self.top_level_layout.addLayout(control_layout)

        # ==========================================
        # 繪圖區域設置 (2D 與 3D 容器)
        # ==========================================
        # 建立一個水平佈局用來放左右兩個繪圖區
        self.charts_layout = QHBoxLayout()

        # ---- 左配置：2D 視窗容器 ----
        self.container_2d = QWidget()
        layout_2d = QVBoxLayout(self.container_2d)
        layout_2d.addWidget(QLabel("<b>2D Top-Down View</b>"))
        self.plot2d = pg.PlotWidget()
        self.plot2d.setXRange(-5, 5)
        self.plot2d.setYRange(0, 10)
        self.scatter2d = pg.ScatterPlotItem(size=8, brush=pg.mkBrush(0, 255, 0, 200))
        self.plot2d.addItem(self.scatter2d)
        layout_2d.addWidget(self.plot2d)
        #
        # self.plot2d = pg.PlotWidget()  # 1. 買一塊 2D 畫布（Widget）
        # self.scatter2d = pg.ScatterPlotItem(size=8)  # 2. 買一盒「專門畫散點圖」的彩色筆
        # self.plot2d.addItem(self.scatter2d)  # 3. 把彩色筆放進畫布裡，準備開畫

        # ---- 右配置：3D 視窗容器 ----
        self.container_3d = QWidget()
        layout_3d = QVBoxLayout(self.container_3d)
        layout_3d.addWidget(QLabel("<b>3D Point Cloud View</b>")) #以上是視窗的內容
        self.plot3d = gl.GLViewWidget() #這便開始就是跑3D資料的地方
        # 初始化 3D 相機位置 (距離=12, 仰角=30, 方位角=45)
        self.plot3d.setCameraPosition(distance=12, elevation=30, azimuth=45)
        grid = gl.GLGridItem()
        grid.setSize(10, 10, 1)
        grid.setSpacing(1, 1, 1)
        self.plot3d.addItem(grid)
        self.scatter3d = gl.GLScatterPlotItem(size=5, color=(0.0, 1.0, 1.0, 0.8))
        self.plot3d.addItem(self.scatter3d)
        layout_3d.addWidget(self.plot3d)
        #
        # self.plot3d = gl.GLViewWidget()  # 1. 買一塊立體 3D 畫布
        # self.plot3d.setCameraPosition(distance=12, elevation=30, azimuth=45)  # 2. 設定你的眼睛（攝影機）要從多遠、什麼角度看過去
        #
        # grid = gl.GLGridItem()  # 3. 做出一個 3D 的空間網格（像地平面一樣）
        # self.plot3d.addItem(grid)  # 4. 把網格放進 3D 畫布
        #
        # self.scatter3d = gl.GLScatterPlotItem(size=5)  # 5. 買一盒 3D 的立體彩色筆（用來畫 X, Y, Z）
        # self.plot3d.addItem(self.scatter3d)  # 6. 把立體彩色筆放入畫布

        # 將 2D 與 3D 容器放入圖表排版中
        self.charts_layout.addWidget(self.container_2d, stretch=1)  #這邊是2D的圖
        self.charts_layout.addWidget(self.container_3d, stretch=1)  #這邊是3D的圖

        # 將圖表排版加入頂層排版
        self.top_level_layout.addLayout(self.charts_layout)

        # ---- 啟動數據執行緒 ----
        self.radar_thread = SimulatedRadarThread()
        self.radar_thread.data_signal.connect(self.update_plots)
        self.radar_thread.start()

    # ==========================================
    # 核心邏輯：控制顯示模式 (2D / 3D / 全部)
    # ==========================================
    def handle_view_mode_change(self, index):
        """ 根據下拉選單的選擇，隱藏或顯示對應的 Widget """
        if index == 0:  # 同時顯示
            self.container_2d.show()
            self.container_3d.show()
        elif index == 1:  # 僅 2D
            self.container_2d.show()
            self.container_3d.hide()
        elif index == 2:  # 僅 3D
            self.container_2d.hide()
            self.container_3d.show()

        # 每次隱藏或顯示後，必須重新校正視角以防扭曲
        self.reset_chart_geometry()

    # ==========================================
    # 核心邏輯：全螢幕切換與防相位偏移控制
    # ==========================================
    def toggle_fullscreen_view(self):
        """ 切換全螢幕模式 """
        if not self.is_fullscreen_mode:
            self.showFullScreen()
            self.is_fullscreen_mode = True
            self.btn_fullscreen.setText("退出全螢幕 (或按 Esc 鍵)")
        else:
            self.showNormal()
            self.is_fullscreen_mode = False
            self.btn_fullscreen.setText("進入當前視窗全螢幕 (或按 Esc 鍵)")

        # 處理防偏移
        self.reset_chart_geometry()

        # 【關鍵新增】強迫主視窗把鍵盤焦點抓回來！這樣 Esc 鍵才有效
        self.setFocus()

    def reset_chart_geometry(self):
        """
        用於解決你提到的：視窗大小、大小方位不同時，導致的 3D 渲染視角或「相位偏移」問題。
        當視窗大小改變，OpenGL 的 Aspect Ratio (長寬比) 會失真，必須主動通知並重繪。
        """
        # 1. 確保 Qt 佈局管理器立即重新計算所有 Widget 的邊界尺寸
        self.top_level_layout.activate()

        # 2. 如果 3D 視窗目前是顯示狀態，重新更新它的投影矩陣與相機
        if self.container_3d.isVisible():
            # 強制 3D 視窗去讀取當前最新的像素寬高，並通知 OpenGL 底層重新配置 Viewport
            self.plot3d.update()

            # 【重要提示】若真實雷達專案中全螢幕會黑掉或位置歪掉，可在這裡手動鎖定相機中心點：
            # opts = self.plot3d.opts
            # self.plot3d.setCameraPosition(center=opts['center'], distance=opts['distance'])

    # ==========================================
    # 核心邏輯：監聽鍵盤事件 (Esc 鍵退出)
    # ==========================================
    def keyPressEvent(self, event):
        """ 覆寫 QMainWindow 的鍵盤事件，捕捉 Esc 鍵 """
        if event.key() == Qt.Key.Key_Escape:
            if self.is_fullscreen_mode:
                print("Log: 偵測到按下 Esc 鍵，正在退出全螢幕...")
                self.toggle_fullscreen_view()  # 調用切換功能恢復原狀
            else:
                print("Log: 目前非全螢幕模式，忽略 Esc 鍵")
        else:
            # 如果是其他按鍵，交還給原本的系統處理
            super().keyPressEvent(event)

    # ==========================================
    # 數據繪圖更新 (維持不變)
    # ==========================================
    def update_plots(self, points):
        if self.container_2d.isVisible():
            self.scatter2d.setData(x=points[:, 0], y=points[:, 1])

        if self.container_3d.isVisible():
            self.scatter3d.setData(pos=points)
            self.plot3d.update()

    def closeEvent(self, event):
        self.radar_thread.stop()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AdvancedRadarApp()
    window.show()
    sys.exit(app.exec())
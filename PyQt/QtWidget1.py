import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout
from PySide6.QtCore import Qt


class MyPracticeWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 1. 設定主視窗標題與初始大小
        self.setWindowTitle("PySide6 基礎練習")
        self.resize(400, 300)

        # 2. 建立一個「空白畫布」作為主視窗的核心元件 (Central Widget)
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        # 3. 建立我們想要的 UI 元件 (Widgets)
        self.label = QLabel("哈囉！這是你的 PySide6 練習視窗")
        # 讓文字居中對齊
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.button = QPushButton("點擊我！")

        # 4. 建立一個垂直版面配置 (Layout)，並把元件塞進去
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        # 5. 把這個配置圖套用到我們的空白畫布上
        main_widget.setLayout(layout)

        # 6. 利用信號與槽機制（Signal & Slot），綁定按鈕點擊事件
        self.button.clicked.connect(self.on_button_click)

        # 計數器變數
        self.click_count = 0

    def on_button_click(self):
        """當按鈕被點擊時，會觸發這個方法"""
        self.click_count += 1
        self.label.setText(f"按鈕已被點擊了 {self.click_count} 次！")
        print(f"Log: 按鈕點擊次數 = {self.click_count}")


if __name__ == "__main__":
    # 每個 PySide6 程式都必須有一個 QApplication 實例
    app = QApplication(sys.argv)

    # 實例化我們的視窗物件（蓋房子）
    window = MyPracticeWindow()
    window.show()  # 顯示視窗

    # 進入程式主迴圈
    sys.exit(app.exec())
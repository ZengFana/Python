from PySide6 import QtWidgets
import sys
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QCheckBox,
    QComboBox,
    QDoubleSpinBox,
    QFileDialog,
    QFormLayout,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QPlainTextEdit,
    QScrollArea,
    QSpinBox,
    QStatusBar,
    QToolBar,
    QVBoxLayout,
    QWidget,
)



# class MyWindow(QtWidgets.QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('QGroud1')
#         # self.resize(400, 300)
#         self._build_left_panel()
#
#     def ui(self):
#         self.toolbar1 = QtWidgets.QToolBar()
#         self.toolbar1.setObjectName("toolbar1")
#
#         self.scroll1 = QtWidgets.QScrollArea()
#         self.scroll1.setWidgetResizable(True)
#         self.scroll1.setMinimumWidth(400)
#         self.scroll1.setMaximumWidth(500)
#     def _build_left_panel(self) -> QWidget:
#         scroll = QScrollArea()
#         scroll.setWidgetResizable(True)
#         scroll.setMinimumWidth(200)
#         scroll.setMaximumWidth(600)
#
#         panel = QWidget()
#         scroll.setWidget(panel)
#
#         layout = QVBoxLayout(panel)
#         layout.setSpacing(10)
#
#         layout.addWidget(self._create_serial_group())
#         # layout.addWidget(self._create_cfg_group())
#         # layout.addWidget(self._create_sensor_group())
#         # layout.addWidget(self._create_zone_group())
#         # layout.addWidget(self._create_run_group())
#         # layout.addWidget(self._create_unity_group())
#         # layout.addWidget(self._create_replay_group())
#         # layout.addStretch(1)
#         return scroll
#
#     def _create_serial_group(self) -> QGroupBox:
#         group = QGroupBox("COM / Serial Settings")
#         layout = QGridLayout(group)
#
#         self.combo_cli_port = QComboBox()
#         self.combo_cli_port.setEditable(True)
#         self.combo_data_port = QComboBox()
#         self.combo_data_port.setEditable(True)
#
#         self.spin_cli_baud = QSpinBox()
#         self.spin_cli_baud.setRange(9600, 3000000)
#         self.spin_cli_baud.setSingleStep(115200)
#
#         self.spin_data_baud = QSpinBox()
#         self.spin_data_baud.setRange(9600, 3000000)
#         self.spin_data_baud.setSingleStep(115200)
#
#         self.btn_refresh_ports = QPushButton("Refresh Ports")
#         self.btn_test_connection = QPushButton("Test Connection")
#
#         layout.addWidget(QLabel("CLI Port"), 0, 0)
#         layout.addWidget(self.combo_cli_port, 0, 1)
#         layout.addWidget(QLabel("DATA Port"), 1, 0)
#         layout.addWidget(self.combo_data_port, 1, 1)
#         layout.addWidget(QLabel("CLI Baud"), 2, 0)
#         layout.addWidget(self.spin_cli_baud, 2, 1)
#         layout.addWidget(QLabel("DATA Baud"), 3, 0)
#         layout.addWidget(self.spin_data_baud, 3, 1)
#         layout.addWidget(self.btn_refresh_ports, 4, 0)
#         layout.addWidget(self.btn_test_connection, 4, 1)
#         return group

class MyWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()

        # self.config = RuntimeConfig()
        # self.worker: Optional[RadarWorker] = None
        # self.playback_worker: Optional[PlaybackWorker] = None
        # self._last_parser_warning_signature = ""
        # self._unity_socket: Optional[socket.socket] = None
        # self._loading_defaults = False

        self.setWindowTitle("Area Scanner Python Visualizer")
        self.resize(1550, 900)

        # self._build_actions()
        self._build_toolbar()
        # self._build_status_bar()
        self._build_central_ui()
        # self._connect_signals()
        # self._apply_default_values()
        # self.refresh_ports()
        # self._apply_viewer_config()
        #
        # self.append_log("[系統] GUI 已建立。")

    # ------------------------------------------------------
    # A. 基本 UI 建立
    # ------------------------------------------------------
    def _build_actions(self) -> None:
        self.action_open_cfg = QAction("載入 CFG", self)
        self.action_start = QAction("開始", self)
        self.action_stop = QAction("停止", self)
        self.action_stop.setEnabled(False)
        self.action_refresh_ports = QAction("重新整理 COM", self)
        self.action_exhibition_mode = QAction("展覽模式", self)
        self.action_clear = QAction("清空畫面", self)
        self.action_about = QAction("關於", self)

    def _build_toolbar(self) -> None:
        toolbar = QToolBar("Main Toolbar", self)
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        toolbar.addAction(self.action_open_cfg)
        toolbar.addSeparator()
        toolbar.addAction(self.action_refresh_ports)
        toolbar.addSeparator()
        toolbar.addAction(self.action_start)
        toolbar.addAction(self.action_stop)
        toolbar.addSeparator()
        toolbar.addAction(self.action_exhibition_mode)
        toolbar.addSeparator()
        toolbar.addAction(self.action_clear)
        toolbar.addAction(self.action_about)

    # def _build_status_bar(self) -> None:
    #     bar = QStatusBar(self)
    #     self.setStatusBar(bar)
    #     self.status_label = QLabel("就緒")
    #     bar.addPermanentWidget(self.status_label)

    def _build_central_ui(self) -> None:
        root = QWidget(self)
        self.setCentralWidget(root)

        root_layout = QHBoxLayout(root)
        root_layout.setContentsMargins(10, 10, 10, 10)
        root_layout.setSpacing(10)

        left = self._build_left_panel()
        # right = self._build_right_panel()

        root_layout.addWidget(left, 0)
        # root_layout.addWidget(right, 1)

    # ------------------------------------------------------
    # B. 左側控制面板
    # ------------------------------------------------------
    def _build_left_panel(self) -> QWidget:
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setMinimumWidth(420)
        scroll.setMaximumWidth(540)

        panel = QWidget()
        scroll.setWidget(panel)

        layout = QVBoxLayout(panel)
        layout.setSpacing(10)

        layout.addWidget(self._create_serial_group())
        layout.addWidget(self._create_cfg_group())
        layout.addWidget(self._create_sensor_group())
        layout.addWidget(self._create_zone_group())
        layout.addWidget(self._create_run_group())
        layout.addWidget(self._create_unity_group())
        layout.addWidget(self._create_replay_group())
        layout.addStretch(1)
        return scroll

    def _create_serial_group(self) -> QGroupBox:
        group = QGroupBox("COM / Serial Settings")
        layout = QGridLayout(group)

        self.combo_cli_port = QComboBox()
        self.combo_cli_port.setEditable(True)
        self.combo_data_port = QComboBox()
        self.combo_data_port.setEditable(True)

        self.spin_cli_baud = QSpinBox()
        self.spin_cli_baud.setRange(9600, 3000000)
        self.spin_cli_baud.setSingleStep(115200)

        self.spin_data_baud = QSpinBox()
        self.spin_data_baud.setRange(9600, 3000000)
        self.spin_data_baud.setSingleStep(115200)

        self.btn_refresh_ports = QPushButton("Refresh Ports")
        self.btn_test_connection = QPushButton("Test Connection")

        layout.addWidget(QLabel("CLI Port"), 0, 0)
        layout.addWidget(self.combo_cli_port, 0, 1)
        layout.addWidget(QLabel("DATA Port"), 1, 0)
        layout.addWidget(self.combo_data_port, 1, 1)
        layout.addWidget(QLabel("CLI Baud"), 2, 0)
        layout.addWidget(self.spin_cli_baud, 2, 1)
        layout.addWidget(QLabel("DATA Baud"), 3, 0)
        layout.addWidget(self.spin_data_baud, 3, 1)
        layout.addWidget(self.btn_refresh_ports, 4, 0)
        layout.addWidget(self.btn_test_connection, 4, 1)
        return group

    def _create_cfg_group(self) -> QGroupBox:
        group = QGroupBox("CFG File")
        layout = QGridLayout(group)

        self.edit_cfg_path = QLineEdit()
        self.btn_browse_cfg = QPushButton("Browse...")

        layout.addWidget(QLabel("CFG 路徑"), 0, 0)
        layout.addWidget(self.edit_cfg_path, 0, 1)
        layout.addWidget(self.btn_browse_cfg, 0, 2)
        return group

    def _create_sensor_group(self) -> QGroupBox:
        group = QGroupBox("Sensor Information")
        layout = QFormLayout(group)

        self.spin_mounting_height = QDoubleSpinBox()
        self.spin_mounting_height.setRange(0.0, 20.0)
        self.spin_mounting_height.setDecimals(2)
        self.spin_mounting_height.setSingleStep(0.1)

        self.spin_elevation_tilt = QDoubleSpinBox()
        self.spin_elevation_tilt.setRange(-90.0, 90.0)
        self.spin_elevation_tilt.setDecimals(2)
        self.spin_elevation_tilt.setSingleStep(0.5)

        self.spin_yaw_offset = QDoubleSpinBox()
        self.spin_yaw_offset.setRange(-180.0, 180.0)
        self.spin_yaw_offset.setDecimals(2)
        self.spin_yaw_offset.setSingleStep(0.5)

        self.spin_x_offset = QDoubleSpinBox()
        self.spin_x_offset.setRange(-20.0, 20.0)
        self.spin_x_offset.setDecimals(2)
        self.spin_x_offset.setSingleStep(0.05)

        self.spin_y_offset = QDoubleSpinBox()
        self.spin_y_offset.setRange(-20.0, 20.0)
        self.spin_y_offset.setDecimals(2)
        self.spin_y_offset.setSingleStep(0.05)

        self.spin_smoothing = QDoubleSpinBox()
        self.spin_smoothing.setRange(0.05, 1.0)
        self.spin_smoothing.setDecimals(2)
        self.spin_smoothing.setSingleStep(0.05)

        self.spin_max_jump = QDoubleSpinBox()
        self.spin_max_jump.setRange(0.2, 10.0)
        self.spin_max_jump.setDecimals(2)
        self.spin_max_jump.setSingleStep(0.1)

        layout.addRow("Mounting Height (m)", self.spin_mounting_height)
        layout.addRow("Elevation Tilt (deg)", self.spin_elevation_tilt)
        layout.addRow("Yaw Offset (deg)", self.spin_yaw_offset)
        layout.addRow("X Offset (m)", self.spin_x_offset)
        layout.addRow("Y Offset (m)", self.spin_y_offset)
        layout.addRow("Smoothing", self.spin_smoothing)
        layout.addRow("Max Jump (m)", self.spin_max_jump)
        return group

    def _create_zone_group(self) -> QGroupBox:
        group = QGroupBox("Viewer / Zones")
        layout = QFormLayout(group)

        self.combo_view_mode = QComboBox()
        self.combo_view_mode.addItems(["X-Y View", "3D View"])

        self.check_enable_zone = QCheckBox("Enable Zones")

        self.spin_critical_start = QDoubleSpinBox()
        self.spin_critical_start.setRange(0.0, 100.0)
        self.spin_critical_start.setDecimals(2)

        self.spin_critical_end = QDoubleSpinBox()
        self.spin_critical_end.setRange(0.0, 100.0)
        self.spin_critical_end.setDecimals(2)

        self.spin_warn_start = QDoubleSpinBox()
        self.spin_warn_start.setRange(0.0, 100.0)
        self.spin_warn_start.setDecimals(2)

        self.spin_warn_end = QDoubleSpinBox()
        self.spin_warn_end.setRange(0.0, 100.0)
        self.spin_warn_end.setDecimals(2)

        self.spin_projection_time = QDoubleSpinBox()
        self.spin_projection_time.setRange(0.0, 20.0)
        self.spin_projection_time.setDecimals(2)

        layout.addRow("View Mode", self.combo_view_mode)
        layout.addRow(self.check_enable_zone)
        layout.addRow("Critical Start (m)", self.spin_critical_start)
        layout.addRow("Critical End (m)", self.spin_critical_end)
        layout.addRow("Warn Start (m)", self.spin_warn_start)
        layout.addRow("Warn End (m)", self.spin_warn_end)
        layout.addRow("Projection Time (s)", self.spin_projection_time)
        return group

    def _create_run_group(self) -> QGroupBox:
        group = QGroupBox("Run Control")
        layout = QVBoxLayout(group)

        # 新增：讓使用者可以在 GUI 上打勾決定要不要存 .bin
        self.check_record_bin = QCheckBox("同步儲存 raw data (.bin)")
        self.check_record_csv = QCheckBox("同步記錄軌跡資料 (.csv)")
        self.check_show_trajectory = QCheckBox("顯示即時追蹤軌跡")
        self.check_show_trajectory.setChecked(True)

        self.btn_exhibition_mode = QPushButton("套用展覽模式")
        self.btn_start = QPushButton("Start")
        self.btn_stop = QPushButton("Stop")
        self.btn_stop.setEnabled(False)

        layout.addWidget(self.check_record_bin)
        layout.addWidget(self.check_record_csv)
        layout.addWidget(self.check_show_trajectory)
        layout.addWidget(self.btn_exhibition_mode)
        layout.addWidget(self.btn_start)
        layout.addWidget(self.btn_stop)
        return group

    def _create_unity_group(self) -> QGroupBox:
        group = QGroupBox("Unity Output")
        layout = QFormLayout(group)

        self.check_send_unity = QCheckBox("Send targets to Unity")
        self.edit_unity_host = QLineEdit()
        self.spin_unity_port = QSpinBox()
        self.spin_unity_port.setRange(1, 65535)

        layout.addRow(self.check_send_unity)
        layout.addRow("Host", self.edit_unity_host)
        layout.addRow("UDP Port", self.spin_unity_port)
        return group

    def _create_replay_group(self) -> QGroupBox:
        group = QGroupBox("Replay")
        layout = QVBoxLayout(group)

        file_layout = QHBoxLayout()
        self.edit_replay_file = QLineEdit()
        self.edit_replay_file.setPlaceholderText("選擇 .bin 或 .csv 檔案...")
        self.btn_browse_replay = QPushButton("Browse...")
        file_layout.addWidget(self.edit_replay_file)
        file_layout.addWidget(self.btn_browse_replay)

        self.btn_start_replay = QPushButton("Start Replay")
        layout.addLayout(file_layout)
        layout.addWidget(self.btn_start_replay)
        return group

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
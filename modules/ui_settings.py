try:
    import modules.ui_main
    import modules.configuration
    from PySide6 import QtCore
    from PySide6.QtCore import (QPoint, QSize)
    from PySide6.QtGui import (QScreen, QPixmap, QIcon, QFont)
    from PySide6.QtWidgets import (QApplication, QFileDialog, QDialog, QGroupBox, QLabel, QPushButton, QRadioButton, QComboBox, QScrollArea, QWidget)
except ImportError as import_error:
    print(
        'An error has occurred when importing modules!\n\n' + 
        f'>>> {import_error}'
    )

    exit()
except Exception as unknown_error:
    print(
        'An unknown error has occurred!\n\n' + 
        f'>>> {unknown_error}'
    )

    exit()
else:
    pass


ui_config_write = modules.configuration.write

class SettingsWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.interface()

        return None
    
    def interface(self):
        game_name, game_exe, game_exe_path, game_index, screen_width, screen_height, background_image, honkai_path, genshin_path = global_variables()
        del game_exe, game_exe_path, background_image

        # ==================== Window Properties ==================== #
        self.setWindowTitle('Launcher')
        self.setWindowIcon(QIcon('resources/icons/app_icon.png'))
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setFixedSize(QSize(820, 525))
        screen_size = QScreen.availableGeometry(QApplication.primaryScreen())
        position_x = (screen_size.width() - self.width()) / 2
        position_y = (screen_size.height() - self.height()) / 2
        self.move(position_x, position_y)

        # ==================== Labels ==================== #
        self.lbl_window_title = QLabel(parent=self, text='✦Settings', objectName='lbl_window_title')

        # ==================== Buttons ==================== #
        self.btn_close = QPushButton(parent=self, text=None, objectName='btn_close', flat=True)
        self.btn_close.clicked.connect(self.close)

        self.btn_menu_1 = QPushButton(parent=self, text='General', objectName='btn_menu_1', flat=True)
        self.btn_menu_1.clicked.connect(self.btn_menu_1_event)

        self.btn_menu_2 = QPushButton(parent=self, text='Screen resolution', objectName='btn_menu_2', flat=True)
        self.btn_menu_2.clicked.connect(self.btn_menu_2_event)

        self.btn_menu_3 = QPushButton(parent=self, text='About', objectName='btn_menu_3', flat=True)
        self.btn_menu_3.clicked.connect(self.btn_menu_3_event)

        self.btn_cancel = QPushButton(parent=self, text='Cancel', objectName='btn_cancel', flat=True)
        self.btn_cancel.clicked.connect(self.close)

        self.btn_confirm = QPushButton(parent=self, text='Confirm', objectName='btn_confirm', flat=True)
        self.btn_confirm.clicked.connect(self.btn_confirm_event)

        #
        # Defines below any items to be put inside the scroll area
        #
        # ==================== Scroll Area & Container ==================== #
        self.scroll_area = QScrollArea(parent=self, objectName='scroll_area')
        self.scroll_container = QWidget(parent=self, objectName='scroll_container')
        self.scroll_area.setWidget(self.scroll_container)

        # ==================== Labels ==================== #
        self.lbl_default_game = QLabel(parent=self.scroll_container, text='Default game', objectName='lbl_default_game')
        self.lbl_game_paths = QLabel(parent=self.scroll_container, text='Game paths', objectName='lbl_game_paths')
        self.lbl_current_paths = QLabel(parent=self.scroll_container, text='Current paths are set to', objectName='lbl_current_paths')
        self.lbl_path_honkai = QLabel(parent=self.scroll_container, text=str(honkai_path), objectName='lbl_path_honkai')
        self.lbl_path_genshin = QLabel(parent=self.scroll_container, text=str(genshin_path), objectName='lbl_path_genshin')
        self.lbl_screen_resolution = QLabel(parent=self.scroll_container, text='Screen resolution', objectName='lbl_screen_resolution')
        self.lbl_launcher_version = QLabel(parent=self.scroll_container, text='Launcher version', objectName='lbl_launcher_version')
        self.lbl_current_version = QLabel(parent=self.scroll_container, text='Current version: 1.0.0', objectName='lbl_current_version')
        self.lbl_about = QLabel(parent=self.scroll_container, text='About', objectName='lbl_about')
        source_code_url = '<a href="http://github.com/kleqing/HoyoLauncher" style="text-decoration: none; color: rgb(220, 188, 96); font: 13pt "Segoe UI";">View source code</a>'
        self.lbl_source_code = QLabel(parent=self.scroll_container, text=source_code_url, objectName='lbl_source_code')
        self.lbl_source_code.setOpenExternalLinks(True)

        # ==================== Buttons ==================== #
        self.btn_locate_honkai_path = QPushButton(parent=self.scroll_container, text='Locate game files (Honkai)', objectName='btn_locate_honkai_path')
        self.btn_locate_honkai_path.clicked.connect(self.btn_locate_honkai_path_event)

        self.btn_locate_genshin_path = QPushButton(parent=self.scroll_container, text='Locate game files (Genshin)', objectName='btn_locate_genshin_path')
        self.btn_locate_genshin_path.clicked.connect(self.btn_locate_genshin_path_event)

        # ==================== Game List ==================== #
        self.game_list = QComboBox(parent=self.scroll_container, objectName='game_list')
        self.game_list.addItem('Honkai Impact 3rd')
        self.game_list.addItem('Genshin Impact')
        self.game_list.setCurrentIndex(game_index)

        # ==================== Group Boxes & Its Items ==================== #
        self.screen_resolution_container = QGroupBox(parent=self.scroll_container, title=' 16 : 9  |  4 : 3 ', objectName='screen_resolution_container')
        font = QFont()
        font.setPointSize(10)
        self.screen_resolution_container.setFont(font)

        self.screen_resolution_1 = QRadioButton(parent=self.screen_resolution_container, text=' 7680  x  4320 ', objectName='screen_resolution_1')
        self.screen_resolution_2 = QRadioButton(parent=self.screen_resolution_container, text=' 6400  x  4800 ', objectName='screen_resolution_2')
        self.screen_resolution_3 = QRadioButton(parent=self.screen_resolution_container, text=' 4096  x  3072 ', objectName='screen_resolution_3')
        self.screen_resolution_4 = QRadioButton(parent=self.screen_resolution_container, text=' 3840  x  2160 ', objectName='screen_resolution_4')
        self.screen_resolution_5 = QRadioButton(parent=self.screen_resolution_container, text=' 3200  x  2400 ', objectName='screen_resolution_5')
        self.screen_resolution_6 = QRadioButton(parent=self.screen_resolution_container, text=' 2560  x  1440 ', objectName='screen_resolution_6')
        self.screen_resolution_7 = QRadioButton(parent=self.screen_resolution_container, text=' 2048  x  1536 ', objectName='screen_resolution_7')
        self.screen_resolution_8 = QRadioButton(parent=self.screen_resolution_container, text=' 1920  x  1080 ', objectName='screen_resolution_8')
        self.screen_resolution_9 = QRadioButton(parent=self.screen_resolution_container, text=' 1600  x  900', objectName='screen_resolution_9')
        self.screen_resolution_10 = QRadioButton(parent=self.screen_resolution_container, text=' 1440  x  900 ', objectName='screen_resolution_10')
        self.screen_resolution_11 = QRadioButton(parent=self.screen_resolution_container, text=' 1366  x  768 ', objectName='screen_resolution_11')
        self.screen_resolution_12 = QRadioButton(parent=self.screen_resolution_container, text=' 1280  x  800 ', objectName='screen_resolution_12')
        self.screen_resolution_13 = QRadioButton(parent=self.screen_resolution_container, text=' 1280  x  600 ', objectName='screen_resolution_13')
        self.screen_resolution_14 = QRadioButton(parent=self.screen_resolution_container, text=' 1024  x  768 ', objectName='screen_resolution_14')
        self.screen_resolution_15 = QRadioButton(parent=self.screen_resolution_container, text=' 1024  x  640 ', objectName='screen_resolution_15')
        self.screen_resolution_16 = QRadioButton(parent=self.screen_resolution_container, text=' 960  x  540 ', objectName='screen_resolution_16')
        self.screen_resolution_17 = QRadioButton(parent=self.screen_resolution_container, text=' 800  x  600', objectName='screen_resolution_17')
        self.screen_resolution_18 = QRadioButton(parent=self.screen_resolution_container, text=' 640  x  480', objectName='screen_resolution_18')
        self.lbl_attention = QLabel(parent=self.screen_resolution_container, text='*Attention: Game will started at windowed mode, not fullscreen or borderless mode', objectName='screen_resolution_20')

        self.screen_resolution_group = [
            self.screen_resolution_1, self.screen_resolution_2, self.screen_resolution_3,
            self.screen_resolution_4, self.screen_resolution_5, self.screen_resolution_6,
            self.screen_resolution_7, self.screen_resolution_8, self.screen_resolution_9,
            self.screen_resolution_10, self.screen_resolution_11, self.screen_resolution_12,
            self.screen_resolution_13, self.screen_resolution_14, self.screen_resolution_15,
            self.screen_resolution_16, self.screen_resolution_17, self.screen_resolution_18
        ]

        for radio_button in self.screen_resolution_group:
            radio_button.setChecked(False)

        match screen_width, screen_height:
            case 7680, 4320:
                self.screen_resolution_group[0].setChecked(True)
            case 6400, 4800:
                self.screen_resolution_group[1].setChecked(True)
            case 4096, 3072:
                self.screen_resolution_group[2].setChecked(True)
            case 3840, 2160:
                self.screen_resolution_group[3].setChecked(True)
            case 3200, 2400:
                self.screen_resolution_group[4].setChecked(True)
            case 2560, 1440:
                self.screen_resolution_group[5].setChecked(True)
            case 2048, 1536:
                self.screen_resolution_group[6].setChecked(True)
            case 1920, 1080:
                self.screen_resolution_group[7].setChecked(True)
            case 1600, 900:
                self.screen_resolution_group[8].setChecked(True)
            case 1440, 900:
                self.screen_resolution_group[9].setChecked(True)
            case 1366, 768:
                self.screen_resolution_group[10].setChecked(True)
            case 1280, 800:
                self.screen_resolution_group[11].setChecked(True)
            case 1280, 600:
                self.screen_resolution_group[12].setChecked(True)
            case 1024, 768:
                self.screen_resolution_group[13].setChecked(True)
            case 1024, 640:
                self.screen_resolution_group[14].setChecked(True)
            case 960, 540:
                self.screen_resolution_group[15].setChecked(True)
            case 800, 600:
                self.screen_resolution_group[16].setChecked(True)
            case 640, 480:
                self.screen_resolution_group[17].setChecked(True)
            case _:
                self.screen_resolution_group[12].setChecked(True)
        

        # ==================== Set Style ==================== #
        match game_name:
            case 'honkai':
                self.style_genshin()
            case _:
                self.style_genshin()

        self.exec()

        return None

    def style_honkai(self):
        pass

    def style_genshin(self):
        game_name, game_exe, game_exe_path, game_index, screen_width, screen_height, background_image, honkai_path, genshin_path  = global_variables()
        del game_name, game_exe, game_exe_path, game_index, screen_width, screen_height, honkai_path, genshin_path

        # ==================== Launcher Background ==================== #
        self.background_image = QLabel(parent=self, text=None, objectName='background_image')
        self.background_image.setFixedSize(QSize(820, 525))
        self.background_image.setScaledContents(True)
        self.background_image.setPixmap(QPixmap(background_image))

        # ==================== Labels ==================== #
        self.lbl_window_title.setFixedSize(QSize(150, 50))
        self.lbl_window_title.move(32, 18)
        self.lbl_window_title.setStyleSheet(
            """
                QLabel#lbl_window_title {
                    color: rgb(57, 59, 64);
                    font: 20pt "Segoe UI";
                }
            """
        )
        self.lbl_window_title.raise_()

        # ==================== Buttons ==================== #
        self.btn_close.setFixedSize(QSize(20, 20))
        self.btn_close.move(765, 35)
        self.btn_close.setStyleSheet(
            """
                QPushButton#btn_close, QPushButton#btn_close:hover, QPushButton#btn_close:pressed {
                    border: 0px solid rgba(0, 0, 0, 0);
                    border-radius: 0px;
                }
                QPushButton#btn_close {
                    background-image: url(resources/icons/btn_close/default.png);
                }
                QPushButton#btn_close:hover, QPushButton#btn_close:pressed {
                    background-image: url(resources/icons/btn_close/hovered.png);
                }
            """
        )
        self.btn_close.raise_()

        self.btn_menu_1.setFixedSize(QSize(216, 50))
        self.btn_menu_1.move(9, 87)
        self.btn_menu_1.setDown(True)
        self.btn_menu_1.setStyleSheet(
            """
                QPushButton#btn_menu_1, QPushButton#btn_menu_1:hover, QPushButton#btn_menu_1:pressed {
                    border-radius: 0px;
                    font: 13pt "Segoe UI";
                    padding-right: 97px;
                }
                QPushButton#btn_menu_1 {
                    color: rgb(117, 118, 121);
                }
                QPushButton#btn_menu_1:hover, QPushButton#btn_menu_1:pressed {
                    color: rgb(57, 59, 63);
                }
                QPushButton#btn_menu_1:pressed {
                    background-color: rgb(233, 233, 233);
                }
            """
        )
        self.btn_menu_1.raise_()

        self.btn_menu_2.setFixedSize(QSize(216, 50))
        self.btn_menu_2.move(9, 137)
        self.btn_menu_2.setDown(False)
        self.btn_menu_2.setStyleSheet(
            """
                QPushButton#btn_menu_2, QPushButton#btn_menu_2:hover, QPushButton#btn_menu_2:pressed {
                    border-radius: 0px;
                    font: 13pt "Segoe UI";
                    padding-right: 24px;
                }
                QPushButton#btn_menu_2 {
                    color: rgb(117, 118, 121);
                }
                QPushButton#btn_menu_2:hover, QPushButton#btn_menu_2:pressed {
                    color: rgb(57, 59, 63);
                }
                QPushButton#btn_menu_2:pressed {
                    background-color: rgb(233, 233, 233);
                }
            """
        )
        self.btn_menu_2.raise_()

        self.btn_menu_3.setFixedSize(QSize(216, 50))
        self.btn_menu_3.move(9, 187)
        self.btn_menu_3.setDown(False)
        self.btn_menu_3.setStyleSheet(
            """
                QPushButton#btn_menu_3, QPushButton#btn_menu_3:hover, QPushButton#btn_menu_3:pressed {
                    border-radius: 0px;
                    font: 13pt "Segoe UI";
                    padding-right: 107px;
                }
                QPushButton#btn_menu_3 {
                    color: rgb(117, 118, 121);
                }
                QPushButton#btn_menu_3:hover, QPushButton#btn_menu_3:pressed {
                    color: rgb(57, 59, 63);
                }
                QPushButton#btn_menu_3:pressed {
                    background-color: rgb(233, 233, 233);
                }
            """
        )
        self.btn_menu_3.raise_()

        self.btn_cancel.setFixedSize(QSize(190, 48))
        self.btn_cancel.move(394, 450)
        self.btn_cancel.setStyleSheet(
            """
                QPushButton#btn_cancel, QPushButton#btn_cancel:hover, QPushButton#btn_cancel:pressed {
                    border: 1px solid rgb(204, 204, 204);
                    border-radius: 5px;
                    color: rgb(220, 188, 96);
                    font: 15pt "Segoe UI";
                    text-align: center;
                }
                QPushButton#btn_cancel {
                    background-color: rgb(255, 255, 255);
                }
                QPushButton#btn_cancel:hover {
                    background-color: rgb(251, 248, 239);
                }
                QPushButton#btn_cancel:pressed {
                    background-color: rgb(236, 233, 225);
                }
            """
        )
        self.btn_cancel.raise_()

        self.btn_confirm.setFixedSize(QSize(190, 48))
        self.btn_confirm.move(596, 450)
        self.btn_confirm.setStyleSheet(
            """
                QPushButton#btn_confirm, QPushButton#btn_confirm:hover, QPushButton#btn_confirm:pressed {
                    border-radius: 5px;
                    color: rgb(244, 216, 168);
                    font: 14pt "Segoe UI";
                    text-align: center;
                }
                QPushButton#btn_confirm {
                    background-color: rgb(57, 59, 64);
                }
                QPushButton#btn_confirm:hover {
                    background-color: rgb(77, 79, 83);
                }
                QPushButton#btn_confirm:pressed {
                    background-color: rgb(51, 53, 57);
                }
            """
        )
        self.btn_confirm.raise_()

        #
        # Define styling for items in the scroll area
        #
        # ==================== Scroll Area & Container ==================== #
        self.scroll_area.setFixedSize(QSize(582, 350))
        self.scroll_area.move(225, 75)
        self.scroll_area.setStyleSheet(
            """
                QScrollArea#scroll_area {
                    border: 0px;
                }
                QScrollBar::vertical {
                    border: none;
                    background-color: #FFFFFF;
                    width: 6px;
                }
                QScrollBar::handle:vertical {
                    border-radius: 3px;
                    background-color: #E9ECF0;
                }
                QScrollBar::handle:vertical:hover, QScrollBar::handle:vertical:pressed {
                    background-color: #D2D5D8;
                }
            """
        )
        self.scroll_area.raise_()

        self.scroll_container.setFixedSize(QSize(576, 920))
        self.scroll_container.move(0, 0)
        self.scroll_container.setStyleSheet(
            """
                QWidget#scroll_container {
                    background-color: #FFFFFF
                }
            """
        )

        # ==================== Labels ==================== #
        self.lbl_default_game.setFixedSize(QSize(170, 30))
        self.lbl_default_game.move(35, 10)
        self.lbl_default_game.setStyleSheet(
            """
                QLabel#lbl_default_game {
                    color: rgb(57, 59, 64);
                    font: 15pt  "Segoe UI";
                }
            """
        )

        self.lbl_game_paths.setFixedSize(QSize(150, 30))
        self.lbl_game_paths.move(35, 120)
        self.lbl_game_paths.setStyleSheet(
            """
                QLabel#lbl_game_paths {
                    color: rgb(57, 59, 64);
                    font: 15pt "Segoe UI";
                }
            """
        )

        self.lbl_current_paths.move(35, 215)
        self.lbl_current_paths.setStyleSheet(
            """
                QLabel#lbl_current_paths {
                    color: rgb(148, 150, 153);
                    font: 13pt "Segoe UI";
                }
            """
        )
        self.lbl_current_paths.raise_()

        self.lbl_path_honkai.setFixedSize(QSize(500, 35))
        self.lbl_path_honkai.move(35, 250)
        self.lbl_path_honkai.setStyleSheet(
            """
                QLabel#lbl_path_honkai {
                    color: rgb(148, 150, 153);
                    font: 12pt "Segoe UI";
                    background-color: rgb(246, 245, 243);
                }
            """
        )

        self.lbl_path_genshin.setFixedSize(QSize(500, 35))
        self.lbl_path_genshin.move(35, 290)
        self.lbl_path_genshin.setStyleSheet(
            """
                QLabel#lbl_path_genshin {
                    color: rgb(148, 150, 153);
                    font: 12pt "Segoe UI";
                    background-color: rgb(246, 245, 243);
                }
            """
        )

        self.lbl_screen_resolution.setFixedSize(QSize(150, 30))
        self.lbl_screen_resolution.move(35, 360)
        self.lbl_screen_resolution.setStyleSheet(
            """
                QLabel#lbl_screen_resolution {
                    color: rgb(57, 59, 64);
                    font: 15pt  "Segoe UI";
                }
            """
        )

        self.lbl_launcher_version.setFixedSize(QSize(150, 30))
        self.lbl_launcher_version.move(35, 745)
        self.lbl_launcher_version.setStyleSheet(
            """
                QLabel#lbl_launcher_version {
                    color: rgb(57, 59, 64);
                    font: 15pt "Segoe UI";
                }
            """
        )

        self.lbl_current_version.setFixedSize(QSize(165, 30))
        self.lbl_current_version.move(35, 780)
        self.lbl_current_version.setStyleSheet(
            """
                QLabel#lbl_current_version {
                    color: rgb(117, 118, 121);
                    font: 13pt "Segoe UI";
                }
            """
        )

        self.lbl_about.setFixedSize(QSize(60, 30))
        self.lbl_about.move(35, 840)
        self.lbl_about.setStyleSheet(
            """
                QLabel#lbl_about {
                    color: rgb(57, 59, 64);
                    font: 15pt "Segoe UI";
                }
            """
        )

        self.lbl_source_code.setFixedSize(QSize(140, 30))
        self.lbl_source_code.move(35, 870)
        self.lbl_source_code.setStyleSheet(
            """
                QLabel#lbl_source_code {
                    color: rgb(220, 188, 96);
                    font: 13pt "Segoe UI";
                }
            """
        )

        # ==================== Buttons ==================== #
        self.game_list.setFixedSize(QSize(170, 30))
        self.game_list.move(35, 50)
        self.game_list.setStyleSheet(
            """
                QComboBox#game_list {
                    font: 13pt "Segoe UI";
                }
            """
        )

        self.btn_locate_honkai_path.setFixedSize(QSize(240, 40))
        self.btn_locate_honkai_path.move(35, 160)
        self.btn_locate_honkai_path.setStyleSheet(
            """
                QPushButton#btn_locate_honkai_path, QPushButton#btn_locate_honkai_path:hover, QPushButton#btn_locate_honkai_path:pressed {
                    border: 1px solid rgb(204, 204, 204);
                    border-radius: 5px;
                    color: rgb(220, 188, 96);
                    font: 13pt "Segoe UI";
                }
                QPushButton#btn_locate_honkai_path {
                    background-color: rgb(255, 255, 255);
                }
                QPushButton#btn_locate_honkai_path:hover {
                    background-color: rgb(251, 248, 239);
                }
                QPushButton#btn_locate_honkai_path:pressed {
                    background-color: rgb(236, 233, 225);
                }
            """
        )

        self.btn_locate_genshin_path.setFixedSize(QSize(240, 40))
        self.btn_locate_genshin_path.move(300, 160)
        self.btn_locate_genshin_path.setStyleSheet(
            """
                QPushButton#btn_locate_genshin_path, QPushButton#btn_locate_genshin_path:hover, QPushButton#btn_locate_genshin_path:pressed {
                    border: 1px solid rgb(204, 204, 204);
                    border-radius: 5px;
                    color: rgb(220, 188, 96);
                    font: 13pt "Segoe UI";
                }
                QPushButton#btn_locate_genshin_path {
                    background-color: rgb(255, 255, 255);
                }
                QPushButton#btn_locate_genshin_path:hover {
                    background-color: rgb(251, 248, 239);
                }
                QPushButton#btn_locate_genshin_path:pressed {
                    background-color: rgb(236, 233, 225);
                }
            """
        )

        # ==================== Group Boxes & Its Items ==================== #
        self.screen_resolution_container.setFixedSize(QSize(520, 310))
        self.screen_resolution_container.move(35, 400)

        self.screen_resolution_1.setFixedSize(QSize(130, 20))
        self.screen_resolution_1.move(15, 30)
        self.screen_resolution_1.setStyleSheet(
            """
                QRadioButton#screen_resolution_1 {
                    font: 13pt "Segoe UI";
                }
            """
        )
        self.screen_resolution_2.setFixedSize(QSize(130, 20))
        self.screen_resolution_2.move(15, 70)
        self.screen_resolution_2.setStyleSheet(
            """
                QRadioButton#screen_resolution_2 {
                    font: 13pt "Segoe UI";
                }
            """
        )
        self.screen_resolution_3.setFixedSize(QSize(130, 20))
        self.screen_resolution_3.move(15, 110)
        self.screen_resolution_3.setStyleSheet(
            """
                QRadioButton#screen_resolution_3 {
                    font: 13pt "Segoe UI";
                }
            """
        )
        self.screen_resolution_4.setFixedSize(QSize(130, 20))
        self.screen_resolution_4.move(205, 30)
        self.screen_resolution_4.setStyleSheet(
            """
                QRadioButton#screen_resolution_4 {
                    font: 13pt "Segoe UI";
                }
            """
        )
        self.screen_resolution_5.setFixedSize(QSize(125, 20))
        self.screen_resolution_5.move(205, 70)
        self.screen_resolution_5.setStyleSheet(
            """
                QRadioButton#screen_resolution_5 {
                    font: 13pt "Segoe UI";
                }
            """
        )
        self.screen_resolution_6.setFixedSize(QSize(125, 20))
        self.screen_resolution_6.move(205, 110)
        self.screen_resolution_6.setStyleSheet(
            """
                QRadioButton#screen_resolution_6 {
                    font: 13pt "Segoe UI";
                }
            """
        )
        self.screen_resolution_7.setFixedSize(QSize(125, 20))
        self.screen_resolution_7.move(385, 30)
        self.screen_resolution_7.setStyleSheet(
            """
                QRadioButton#screen_resolution_7 {
                    font: 13pt "Segoe UI";
                }
            """
        )
        self.screen_resolution_8.setFixedSize(QSize(125, 20))
        self.screen_resolution_8.move(385, 70)
        self.screen_resolution_8.setStyleSheet(
            """
                QRadioButton#screen_resolution_8 {
                    font: 13pt "Segoe UI";
                }
            """
        )
        self.screen_resolution_9.setFixedSize(QSize(115, 20))
        self.screen_resolution_9.move(385, 110)
        self.screen_resolution_9.setStyleSheet(
            """
                QRadioButton#screen_resolution_9 {
                    font: 13pt "Segoe UI";
                }
            """
        )

        self.screen_resolution_10.setFixedSize(QSize(130, 20))
        self.screen_resolution_10.move(15, 180)
        self.screen_resolution_10.setStyleSheet(
            """
                QRadioButton#screen_resolution_10 {
                    font: 13pt "Segoe UI";
                }
            """
        )
        self.screen_resolution_11.setFixedSize(QSize(130, 20))
        self.screen_resolution_11.move(15, 220)
        self.screen_resolution_11.setStyleSheet(
            """
                QRadioButton#screen_resolution_11 {
                    font: 13pt "Segoe UI";
                }
            """
        )
        self.screen_resolution_12.setFixedSize(QSize(130, 20))
        self.screen_resolution_12.move(15, 260)
        self.screen_resolution_12.setStyleSheet(
            """
                QRadioButton#screen_resolution_12 {
                    font: 13pt "Segoe UI";
                }
            """
        )
        self.screen_resolution_13.setFixedSize(QSize(130, 20))
        self.screen_resolution_13.move(205, 180)
        self.screen_resolution_13.setStyleSheet(
            """
                QRadioButton#screen_resolution_13 {
                    font: 13pt "Segoe UI";
                }
            """
        )
        self.screen_resolution_14.setFixedSize(QSize(125, 20))
        self.screen_resolution_14.move(205, 220)
        self.screen_resolution_14.setStyleSheet(
            """
                QRadioButton#screen_resolution_14 {
                    font: 13pt "Segoe UI";
                }
            """
        )
        self.screen_resolution_15.setFixedSize(QSize(120, 20))
        self.screen_resolution_15.move(205, 260)
        self.screen_resolution_15.setStyleSheet(
            """
                QRadioButton#screen_resolution_15 {
                    font: 13pt "Segoe UI";
                }
            """
        )
        self.screen_resolution_16.setFixedSize(QSize(120, 20))
        self.screen_resolution_16.move(385, 180)
        self.screen_resolution_16.setStyleSheet(
            """
                QRadioButton#screen_resolution_16 {
                    font: 13pt "Segoe UI";
                }
            """
        )
        self.screen_resolution_17.setFixedSize(QSize(110, 20))
        self.screen_resolution_17.move(385, 220)
        self.screen_resolution_17.setStyleSheet(
            """
                QRadioButton#screen_resolution_17 {
                    font: 13pt "Segoe UI";
                }
            """
        )
        self.screen_resolution_18.setFixedSize(QSize(110, 20))
        self.screen_resolution_18.move(385, 260)
        self.screen_resolution_18.setStyleSheet(
            """
                QRadioButton#screen_resolution_18 {
                    font: 13pt "Segoe UI";
                }
            """
        )
        self.lbl_attention.setFixedSize(QSize(500, 20))
        self.lbl_attention.move(40, 285)
        self.lbl_attention.setStyleSheet(
            """
                QRadioButton#lbl_attention {
                    font: 13pt "Segoe UI";
                    algin: center;
                }
            """
        )

        return None

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

        return None

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

        return None

    def btn_menu_1_event(self):
        self.btn_menu_1.setDown(True)
        self.btn_menu_2.setDown(False)
        self.btn_menu_3.setDown(False)

        self.scroll_area.verticalScrollBar().setValue(10)
        
        return None

    def btn_menu_2_event(self):
        self.btn_menu_1.setDown(False)
        self.btn_menu_2.setDown(True)
        self.btn_menu_3.setDown(False)

        self.scroll_area.verticalScrollBar().setValue(360)
    
        return None
    
    def btn_menu_3_event(self):
        self.btn_menu_1.setDown(False)
        self.btn_menu_2.setDown(False)
        self.btn_menu_3.setDown(True)

        self.scroll_area.verticalScrollBar().setValue(745)

        return None

    def btn_locate_honkai_path_event(self):
        self.new_honkai_path = QFileDialog.getExistingDirectory(self.scroll_container, 'Select Honkai Impact 3rd installation folder')

        match self.new_honkai_path:
            case '' | None:
                pass
            case _:
                self.lbl_path_honkai.setText(self.new_honkai_path)
                ui_config_write('PATHS', 'honkai_impact', self.new_honkai_path)

        return None
    
    def btn_locate_genshin_path_event(self):
        self.new_genshin_path = QFileDialog.getExistingDirectory(self.scroll_container, 'Select Genshin Impact installation folder')

        match self.new_genshin_path:
            case '' | None:
                pass
            case _:
                self.lbl_path_genshin.setText(self.new_genshin_path)
                ui_config_write('PATHS', 'genshin_impact', self.new_genshin_path)

        return None

    def btn_confirm_event(self):
        match self.game_list.currentIndex():
            case 0:
                game = 'honkai'
            case 1:
                game = 'genshin'
            case _:
                game = ''

        ui_config_write('LAUNCHER', 'game', game)

        for radio_button in self.screen_resolution_group:
            match radio_button.isChecked():
                case True:
                    match radio_button.objectName():
                        case 'screen_resolution_1':
                            ui_config_write('OPTIONS', 'screen_width', '7680')
                            ui_config_write('OPTIONS', 'screen_height', '4320')
                        case 'screen_resolution_2':
                            ui_config_write('OPTIONS', 'screen_width', '6400')
                            ui_config_write('OPTIONS', 'screen_height', '4800')
                        case 'screen_resolution_3':
                            ui_config_write('OPTIONS', 'screen_width', '4096')
                            ui_config_write('OPTIONS', 'screen_height', '3072')
                        case 'screen_resolution_4':
                            ui_config_write('OPTIONS', 'screen_width', '3840')
                            ui_config_write('OPTIONS', 'screen_height', '2160')
                        case 'screen_resolution_5':
                            ui_config_write('OPTIONS', 'screen_width', '3200')
                            ui_config_write('OPTIONS', 'screen_height', '2400')
                        case 'screen_resolution_6':
                            ui_config_write('OPTIONS', 'screen_width', '2560')
                            ui_config_write('OPTIONS', 'screen_height', '1440')
                        case 'screen_resolution_7':
                            ui_config_write('OPTIONS', 'screen_width', '2048')
                            ui_config_write('OPTIONS', 'screen_height', '1536')
                        case 'screen_resolution_8':
                            ui_config_write('OPTIONS', 'screen_width', '1920')
                            ui_config_write('OPTIONS', 'screen_height', '1080')
                        case 'screen_resolution_9':
                            ui_config_write('OPTIONS', 'screen_width', '1600')
                            ui_config_write('OPTIONS', 'screen_height', '900')
                        case 'screen_resolution_10':
                            ui_config_write('OPTIONS', 'screen_width', '1440')
                            ui_config_write('OPTIONS', 'screen_height', '900')
                        case 'screen_resolution_11':
                            ui_config_write('OPTIONS', 'screen_width', '1366')
                            ui_config_write('OPTIONS', 'screen_height', '768')
                        case 'screen_resolution_12':
                            ui_config_write('OPTIONS', 'screen_width', '1280')
                            ui_config_write('OPTIONS', 'screen_height', '800')
                        case 'screen_resolution_13':
                            ui_config_write('OPTIONS', 'screen_width', '1280')
                            ui_config_write('OPTIONS', 'screen_height', '600')
                        case 'screen_resolution_14':
                            ui_config_write('OPTIONS', 'screen_width', '1024')
                            ui_config_write('OPTIONS', 'screen_height', '768')
                        case 'screen_resolution_15':
                            ui_config_write('OPTIONS', 'screen_width', '1024')
                            ui_config_write('OPTIONS', 'screen_height', '640')
                        case 'screen_resolution_16':
                            ui_config_write('OPTIONS', 'screen_width', '960')
                            ui_config_write('OPTIONS', 'screen_height', '540')
                        case 'screen_resolution_17':
                            ui_config_write('OPTIONS', 'screen_width', '800')
                            ui_config_write('OPTIONS', 'screen_height', '600')
                        case 'screen_resolution_18':
                            ui_config_write('OPTIONS', 'screen_width', '640')
                            ui_config_write('OPTIONS', 'screen_height', '480')
                        case _:
                            ui_config_write('OPTIONS', 'screen_width', '1280')
                            ui_config_write('OPTIONS', 'screen_height', '600')
                case _:
                    pass

        self.close()

        return None

def global_variables():
    game_name, honkai_path, genshin_path, screen_width, screen_height = modules.configuration.read()

    match game_name:
        case 'honkai':
            game_exe = 'BH3.exe'
            game_exe_path = honkai_path.joinpath(game_exe)
            game_index = 0
            background_image = 'resources/backgrounds/settings_genshin.png'
        case 'genshin':
            game_exe = 'GenshinImpact.exe'
            game_exe_path = genshin_path.joinpath(game_exe)
            game_index = 1
            background_image = 'resources/backgrounds/settings_genshin.png'
        case _:
            game_exe = ''
            game_exe_path = ''
            game_index = 0
            background_image = ''
    
    return game_name, game_exe, game_exe_path, game_index, screen_width, screen_height, background_image, honkai_path, genshin_path

if __name__ == '__main__':
    pass


try:
    import pathlib
    import subprocess
    import sys
    import webbrowser
    import modules.ui_settings
    import modules.ui_message_box
    import modules.configuration
    import modules.resources
    from PySide6 import QtCore
    from PySide6.QtCore import (QPoint, QSize)
    from PySide6.QtGui import (QCursor, QScreen, QPixmap, QIcon)
    from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton)
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


ui_settings = modules.ui_settings.SettingsWindow
ui_message_box = modules.ui_message_box.message_box

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.interface()

        return None

    def interface(self):
        game_name, game_exe, game_exe_path, game_index, screen_width, screen_height, background_image_path, launcher_image, honkai_path, genshin_path, url_list = global_variables()
        del game_name, game_exe, game_exe_path, game_index, screen_width, screen_height, background_image_path, honkai_path, genshin_path, url_list

        self.central_widget = QMainWindow()
        self.setCentralWidget(self.central_widget)

        # ==================== Window Properties ==================== #
        self.setWindowTitle('miHoYo Launcher')
        self.setWindowIcon(QIcon(':/resources/icons/app_icon.png'))
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setFixedSize(QSize(1155, 650))
        screen_size = QScreen.availableGeometry(QApplication.primaryScreen())
        position_x = (screen_size.width() - self.width()) / 2
        position_y = (screen_size.height() - self.height()) / 2
        self.move(position_x, position_y)

        self.background_image = QLabel(self, objectName='background_image')
        self.background_image.setFixedSize(QSize(1155, 650))
        self.background_image.setPixmap(QPixmap(launcher_image))
        self.background_image.setScaledContents(True)

        # ======================================== Top Bar ======================================== #
        self.top_bar = QLabel(self, text=None, objectName='top_bar')
        self.top_bar.setFixedSize(QSize(1155, 30))
        self.top_bar.setStyleSheet(
            """
                QLabel#top_bar {
                    background-color: rgb(20, 20, 20);
                }
            """
        )

        self.app_title = QLabel(self, text='miHoYo Launcher', objectName='app_title')
        self.app_title.setFixedSize(QSize(150, 30))
        self.app_title.move(12, 0)
        self.app_title.setStyleSheet(
            """
                QLabel#app_title {
                    color: #FFFFFF;
                    font: 9pt "Segoe UI";
                    text-align: center;
                }
            """
        )

        self.app_version = QLabel(self, text='1.0.0', objectName='app_version')
        self.app_version.setFixedSize(QSize(40, 30))
        self.app_version.move(130, 0)
        self.app_version.setStyleSheet(
            """
                QLabel#app_version {
                    color: rgb(67, 67, 67);
                    font: 9pt "Segoe UI";
                }
            """
        )

        self.btn_close = QPushButton(self, text=None, objectName='btn_close', flat=True)
        self.btn_close.setFixedSize(QSize(30, 30))
        self.btn_close.move(1125, 0)
        self.btn_close.setStyleSheet(
            """
                QPushButton#btn_close, QPushButton#btn_close:hover, QPushButton#btn_close:pressed {
                    border-radius: 0px;
                    background-repeat: no-repeat;
                    background-position: center;
                }

                QPushButton#btn_close {
                    background-image: url(:/resources/icons/top_bar/close/default.png);
                }

                QPushButton#btn_close:hover {
                    background-image: url(:/resources/icons/top_bar/close/hovered.png);
                }

                QPushButton#btn_close:pressed {
                    background-image: url(:/resources/icons/top_bar/close/pressed.png);
                }
            """
        )
        self.btn_close.clicked.connect(self.close)

        self.btn_minimize = QPushButton(self, text=None, objectName='btn_minimize', flat=True)
        self.btn_minimize.setFixedSize(QSize(30, 30))
        self.btn_minimize.move(1090, 0)
        self.btn_minimize.setStyleSheet(
            """
                QPushButton#btn_minimize, QPushButton#btn_minimize:hover, QPushButton#btn_minimize:pressed {
                    border-radius: 0px;
                    background-repeat: no-repeat;
                    background-position: center;
                }

                QPushButton#btn_minimize {
                    background-image: url(:/resources/icons/top_bar/minimize/default.png);
                }

                QPushButton#btn_minimize:hover {
                    background-image: url(:/resources/icons/top_bar/minimize/hovered.png);
                }

                QPushButton#btn_minimize:pressed {
                    background-image: url(:/resources/icons/top_bar/minimize/pressed.png);
                }
            """
        )
        self.btn_minimize.clicked.connect(self.showMinimized)

        self.btn_settings = QPushButton(self, text=None, objectName='btn_settings', flat=True)
        self.btn_settings.setFixedSize(QSize(30, 30))
        self.btn_settings.move(1055, 0)
        self.btn_settings.setStyleSheet(
            """
                QPushButton#btn_settings, QPushButton#btn_settings:hover, QPushButton#btn_settings:pressed {
                    border-radius: 0px;
                    background-repeat: no-repeat;
                    background-position: center;
                }

                QPushButton#btn_settings {
                    background-image: url(:/resources/icons/top_bar/settings/default.png);
                }

                QPushButton#btn_settings:hover {
                    background-image: url(:/resources/icons/top_bar/settings/hovered.png);
                }

                QPushButton#btn_settings:pressed {
                    background-image: url(:/resources/icons/top_bar/settings/pressed.png);
                }
            """
        )
        self.btn_settings.clicked.connect(self.btn_settings_event)

        # ======================================== Right Bar ======================================== #
        self.right_bar = QLabel(self, text=None, objectName='right_bar')
        self.right_bar.setFixedSize(QSize(75, 620))
        self.right_bar.move(1080, 30)
        self.right_bar.setStyleSheet(
            """
                QLabel#right_bar {
                    background-color: rgba(0, 0, 0, 0.3)
                }
            """
        )        

        self.btn_url_home = QPushButton(self, text=None, objectName='btn_url_home', flat=True)
        self.btn_url_home.setFixedSize(QSize(40, 40))
        self.btn_url_home.move(1100, 60)
        self.btn_url_home.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_url_home.setStyleSheet(
            """
                QPushButton#btn_url_home, QPushButton#btn_url_home:hover, QPushButton#btn_url_home:pressed {
                    border-radius: 20px;
                    background-repeat: no-repeat;
                    background-position: center;
                }

                QPushButton#btn_url_home:hover, QPushButton#btn_url_home:pressed {
                    background-color: rgba(20, 20, 20, 0.9);
                }

                QPushButton#btn_url_home {
                    border: 2px solid rgba(255, 255, 255, 0);
                    background-image: url(:/resources/icons/right_bar/home/default.png);
                    background-color: rgba(20, 20, 20, 0.6);
                }

                QPushButton#btn_url_home:hover {
                    border: 2px solid rgb(255, 225, 145);
                    background-image: url(:/resources/icons/right_bar/home/hovered.png);
                }

                QPushButton#btn_url_home:pressed {
                    border: 2px solid rgb(255, 205, 125);
                    background-image: url(:/resources/icons/right_bar/home/pressed.png);
                }
            """
        )
        self.btn_url_home.clicked.connect(lambda: self.btn_url_event('home'))

        self.btn_url_facebook = QPushButton(self, text=None, objectName='btn_url_facebook', flat=True)
        self.btn_url_facebook.setFixedSize(QSize(40, 40))
        self.btn_url_facebook.move(1100, 130)
        self.btn_url_facebook.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_url_facebook.setStyleSheet(
            """
                QPushButton#btn_url_facebook, QPushButton#btn_url_facebook:hover, QPushButton#btn_url_facebook:pressed {
                    border-radius: 20px;
                    background-repeat: no-repeat;
                    background-position: center;
                }

                QPushButton#btn_url_facebook:hover, QPushButton#btn_url_facebook:pressed {
                    background-color: rgba(20, 20, 20, 0.9);
                }

                QPushButton#btn_url_facebook {
                    border: 2px solid rgba(255, 255, 255, 0);
                    background-image: url(:/resources/icons/right_bar/facebook/default.png);
                    background-color: rgba(20, 20, 20, 0.6);
                }

                QPushButton#btn_url_facebook:hover {
                    border: 2px solid rgb(255, 225, 145);
                    background-image: url(:/resources/icons/right_bar/facebook/hovered.png);
                }

                QPushButton#btn_url_facebook:pressed {
                    border: 2px solid rgb(255, 205, 125);
                    background-image: url(:/resources/icons/right_bar/facebook/pressed.png);
                }
            """
        )
        self.btn_url_facebook.clicked.connect(lambda: self.btn_url_event('facebook'))

        self.btn_url_twitter = QPushButton(self, text=None, objectName='btn_url_twitter', flat=True)
        self.btn_url_twitter.setFixedSize(QSize(40, 40))
        self.btn_url_twitter.move(1100, 200)
        self.btn_url_twitter.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_url_twitter.setStyleSheet(
            """
                QPushButton#btn_url_twitter, QPushButton#btn_url_twitter:hover, QPushButton#btn_url_twitter:pressed {
                    border-radius: 20px;
                    background-repeat: no-repeat;
                    background-position: center;
                }

                QPushButton#btn_url_twitter:hover, QPushButton#btn_url_twitter:pressed {
                    background-color: rgba(20, 20, 20, 0.9);
                }

                QPushButton#btn_url_twitter {
                    border: 2px solid rgba(255, 255, 255, 0);
                    background-image: url(:/resources/icons/right_bar/twitter/default.png);
                    background-color: rgba(20, 20, 20, 0.6);
                }

                QPushButton#btn_url_twitter:hover {
                    border: 2px solid rgb(255, 225, 145);
                    background-image: url(:/resources/icons/right_bar/twitter/hovered.png);
                }

                QPushButton#btn_url_twitter:pressed {
                    border: 2px solid rgb(255, 205, 125);
                    background-image: url(:/resources/icons/right_bar/twitter/pressed.png);
                }
            """
        )
        self.btn_url_twitter.clicked.connect(lambda: self.btn_url_event('twitter'))

        self.btn_url_instagram = QPushButton(self, text=None, objectName='btn_url_instagram', flat=True)
        self.btn_url_instagram.setFixedSize(QSize(40, 40))
        self.btn_url_instagram.move(1100, 270)
        self.btn_url_instagram.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_url_instagram.setStyleSheet(
            """
                QPushButton#btn_url_instagram, QPushButton#btn_url_instagram:hover, QPushButton#btn_url_instagram:pressed {
                    border-radius: 20px;
                    background-repeat: no-repeat;
                    background-position: center;
                }

                QPushButton#btn_url_instagram:hover, QPushButton#btn_url_instagram:pressed {
                    background-color: rgba(20, 20, 20, 0.9);
                }

                QPushButton#btn_url_instagram {
                    border: 2px solid rgba(255, 255, 255, 0);
                    background-image: url(:/resources/icons/right_bar/instagram/default.png);
                    background-color: rgba(20, 20, 20, 0.6);
                }

                QPushButton#btn_url_instagram:hover {
                    border: 2px solid rgb(255, 225, 145);
                    background-image: url(:/resources/icons/right_bar/instagram/hovered.png);
                }

                QPushButton#btn_url_instagram:pressed {
                    border: 2px solid rgb(255, 205, 125);
                    background-image: url(:/resources/icons/right_bar/instagram/pressed.png);
                }
            """
        )
        self.btn_url_instagram.clicked.connect(lambda: self.btn_url_event('instagram'))

        self.btn_url_youtube = QPushButton(self, text=None, objectName='btn_url_youtube', flat=True)
        self.btn_url_youtube.setFixedSize(QSize(40, 40))
        self.btn_url_youtube.move(1100, 340)
        self.btn_url_youtube.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_url_youtube.setStyleSheet(
            """
                QPushButton#btn_url_youtube, QPushButton#btn_url_youtube:hover, QPushButton#btn_url_youtube:pressed {
                    border-radius: 20px;
                    background-repeat: no-repeat;
                    background-position: center;
                }

                QPushButton#btn_url_youtube:hover, QPushButton#btn_url_youtube:pressed {
                    background-color: rgba(20, 20, 20, 0.9);
                }

                QPushButton#btn_url_youtube {
                    border: 2px solid rgba(255, 255, 255, 0);
                    background-image: url(:/resources/icons/right_bar/youtube/default.png);
                    background-color: rgba(20, 20, 20, 0.6);
                }

                QPushButton#btn_url_youtube:hover {
                    border: 2px solid rgb(255, 225, 145);
                    background-image: url(:/resources/icons/right_bar/youtube/hovered.png);
                }

                QPushButton#btn_url_youtube:pressed {
                    border: 2px solid rgb(255, 205, 125);
                    background-image: url(:/resources/icons/right_bar/youtube/pressed.png);
                }
            """
        )
        self.btn_url_youtube.clicked.connect(lambda: self.btn_url_event('youtube'))

        self.btn_url_hoyolab = QPushButton(self, text=None, objectName='btn_url_hoyolab', flat=True)
        self.btn_url_hoyolab.setFixedSize(QSize(40, 40))
        self.btn_url_hoyolab.move(1100, 410)
        self.btn_url_hoyolab.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_url_hoyolab.setStyleSheet(
            """
                QPushButton#btn_url_hoyolab, QPushButton#btn_url_hoyolab:hover, QPushButton#btn_url_hoyolab:pressed {
                    border-radius: 20px;
                    background-repeat: no-repeat;
                    background-position: center;
                }

                QPushButton#btn_url_hoyolab:hover, QPushButton#btn_url_hoyolab:pressed {
                    background-color: rgba(20, 20, 20, 0.9);
                }

                QPushButton#btn_url_hoyolab {
                    border: 2px solid rgba(255, 255, 255, 0);
                    background-image: url(:/resources/icons/right_bar/hoyolab/default.png);
                    background-color: rgba(20, 20, 20, 0.6);
                }

                QPushButton#btn_url_hoyolab:hover {
                    border: 2px solid rgb(255, 225, 145);
                    background-image: url(:/resources/icons/right_bar/hoyolab/hovered.png);
                }

                QPushButton#btn_url_hoyolab:pressed {
                    border: 2px solid rgb(255, 205, 125);
                    background-image: url(:/resources/icons/right_bar/hoyolab/pressed.png);
                }
            """
        )
        self.btn_url_hoyolab.clicked.connect(lambda: self.btn_url_event('hoyolab'))

        self.btn_url_github = QPushButton(self, text=None, objectName='btn_url_github', flat=True)
        self.btn_url_github.setFixedSize(QSize(40, 40))
        self.btn_url_github.move(1100, 480)
        self.btn_url_github.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_url_github.setStyleSheet(
            """
                QPushButton#btn_url_github, QPushButton#btn_url_github:hover, QPushButton#btn_url_github:pressed {
                    border-radius: 20px;
                    background-repeat: no-repeat;
                    background-position: center;
                }

                QPushButton#btn_url_github:hover, QPushButton#btn_url_github:pressed {
                    background-color: rgba(20, 20, 20, 0.9);
                }

                QPushButton#btn_url_github {
                    border: 2px solid rgba(255, 255, 255, 0);
                    background-image: url(:/resources/icons/right_bar/github/default.png);
                    background-color: rgba(20, 20, 20, 0.6);
                }

                QPushButton#btn_url_github:hover {
                    border: 2px solid rgb(255, 225, 145);
                    background-image: url(:/resources/icons/right_bar/github/hovered.png);
                }

                QPushButton#btn_url_github:pressed {
                    border: 2px solid rgb(255, 205, 125);
                    background-image: url(:/resources/icons/right_bar/github/pressed.png);
                }
            """
        )
        self.btn_url_github.clicked.connect(lambda: self.btn_url_event('github'))

        # ======================================== Main Button: Launch ======================================== #
        self.btn_main_launch = QPushButton(self, text='Launch', objectName='btn_main_launch', flat=True)
        self.btn_main_launch.setFixedSize(QSize(240, 65))
        self.btn_main_launch.move(800, 555)
        self.btn_main_launch.setStyleSheet(
            """
                QPushButton#btn_main_launch, QPushButton#btn_main_launch:hover, QPushButton#btn_main_launch:pressed {
                    color: #704A16;
                    border-radius: 5px;
                    font: 18pt "Segoe UI";
                    text-align: center;
                }

                QPushButton#btn_main_launch {
                    background-color: #FFCF0D;
                }

                QPushButton#btn_main_launch:hover {
                    background-color: #FFD426;
                }

                QPushButton#btn_main_launch:pressed {
                    background-color: #E5BA0C;
                }
            """
        )
        self.btn_main_launch.clicked.connect(self.btn_launch_event)

        # ==================== Background Dim ==================== #
        self.background_dim = QLabel(self, text=None, objectName='background_dim')
        self.background_dim.setFixedSize(QSize(1155, 650))
        self.background_dim.move(0, 0)
        self.background_dim.setStyleSheet(
            """
                QLabel#background_dim {
                    background-color: rgba(0, 0, 0, 0.3)
                }
            """
        )
        self.background_dim.hide()

        self.show()

        return None

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

        return None

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

        return None

    def btn_settings_event(self):
        self.background_dim.show()
        ui_settings()

        self.close()
        MainWindow()

        return None

    def btn_url_event(self, destination):
        game_name, game_exe, game_exe_path, game_index, screen_width, screen_height, background_image_path, launcher_image, honkai_path, genshin_path, url_list = global_variables()
        del game_exe, game_exe_path, game_index, screen_width, screen_height, background_image_path, launcher_image, honkai_path, genshin_path

        match game_name:
            case 'honkai':
                match destination:
                    case 'home':
                        webbrowser.open(url_list[0], new=2)
                    case 'facebook':
                        webbrowser.open(url_list[2], new=2)
                    case 'twitter':
                        webbrowser.open(url_list[4], new=2)
                    case 'instagram':
                        webbrowser.open(url_list[6], new=2)
                    case 'youtube':
                        webbrowser.open(url_list[8], new=2)
                    case 'hoyolab':
                        webbrowser.open(url_list[10], new=2)
                    case 'github':
                        webbrowser.open(url_list[12], new=2)
                    case _:
                        pass
            case 'genshin':
                match destination:
                    case 'home':
                        webbrowser.open(url_list[1], new=2)
                    case 'facebook':
                        webbrowser.open(url_list[3], new=2)
                    case 'twitter':
                        webbrowser.open(url_list[5], new=2)
                    case 'instagram':
                        webbrowser.open(url_list[7], new=2)
                    case 'youtube':
                        webbrowser.open(url_list[9], new=2)
                    case 'hoyolab':
                        webbrowser.open(url_list[11], new=2)
                    case 'github':
                        webbrowser.open(url_list[12], new=2)
                    case _:
                        pass
            case _:
                pass
        
        return None

    def btn_launch_event(self):
        game_name, game_exe, game_exe_path, game_index, screen_width, screen_height, background_image_path, launcher_image, honkai_path, genshin_path, url_list = global_variables()
        del game_name, game_index, background_image_path, launcher_image, honkai_path, genshin_path, url_list

        launch_command = f'{game_exe_path} -screen-fullscreen 1 -screen-width {screen_width} -screen-height {screen_height}'

        try:
            subprocess.Popen(launch_command, shell=False, close_fds=True)
        except Exception as launch_error:
            ui_message_box(
                'error',
                f'Unable to launch {game_exe}!\n\n' + 
                f'{launch_error}'
            )

            return None
        else:
            sys.exit(0)

def global_variables():
    game_name, honkai_path, genshin_path, screen_width, screen_height = modules.configuration.read()
    background_image_path = pathlib.Path(__file__).parents[1].resolve().joinpath('backgrounds')

    match game_name:
        case 'honkai':
            game_exe = 'BH3.exe'
            game_exe_path = honkai_path.joinpath(game_exe)
            game_index = 0
            launcher_image = background_image_path.joinpath('honkai.png')
        case 'genshin':
            game_exe = 'GenshinImpact.exe'
            game_exe_path = genshin_path.joinpath(game_exe)
            game_index = 1
            launcher_image = background_image_path.joinpath('genshin.png')
        case _:
            game_exe = ''
            game_exe_path = ''
            game_index = 0
            launcher_image = background_image_path
    
    url_list = [
        'https://honkaiimpact3.mihoyo.com/asia', 'https://genshin.mihoyo.com',
        'https://www.facebook.com/HonkaiImpact3rd', 'https://www.facebook.com/Genshinimpact',
        'https://twitter.com/HonkaiImpact3rd', 'https://twitter.com/GenshinImpact',
        'https://www.instagram.com/honkaiimpact3rd', 'https://www.instagram.com/genshinimpact',
        'https://www.youtube.com/channel/UCko6H6LokKM__B03i5_vBQQ', 'https://www.youtube.com/c/GenshinImpact',
        'https://www.hoyolab.com/?lang=en-us&utm_source=launcher&utm_medium=game&utm_id=1', 'https://www.hoyolab.com/genshin/?lang=en-us&utm_source=launcher&utm_medium=game&utm_id=2',
        'https://github.com/shirooo39/mihoyo_launcher'
    ]
    
    return game_name, game_exe, game_exe_path, game_index, screen_width, screen_height, background_image_path, launcher_image, honkai_path, genshin_path, url_list

if __name__ == '__main__':
    pass


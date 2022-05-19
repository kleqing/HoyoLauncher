import sys
from PySide6.QtWidgets import QApplication
from modules.ui_main import MainWindow
from modules.clear_output import clear_output
import configparser
import pathlib



def main():
    clear_output()
    config_file = pathlib.Path(__file__).parents[0].resolve().joinpath('settings.ini')
    parser = configparser.ConfigParser()
    parser.read(config_file)
    default_game = parser.get('LAUNCHER', 'default')
    parser.set('LAUNCHER', 'game', default_game)
    try:
        with open(config_file, 'w') as cfg:
            parser.write(cfg)
    except Exception as unknown_error:
        pass

    app = QApplication([])
    MainWindow()
    app.exec()
    sys.exit()

    
if __name__ == '__main__':
    main()


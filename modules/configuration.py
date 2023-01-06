try:
    import configparser
    import pathlib
    import modules.ui_message_box
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


ui_message_box = modules.ui_message_box.message_box

config_file = pathlib.Path(__file__).parents[1].resolve().joinpath('settings.ini')
parser = configparser.ConfigParser()

def initialize():
    match config_file.exists() and config_file.is_file():
        case True:
            return True
        case _:
            parser['LAUNCHER'] = {
                'game': 'honkai'
            }
            parser['PATHS'] = {
                'honkai_impact': '',
                'genshin_impact': ''
            }
            parser['OPTIONS'] = {
                'screen_width': '1280',
                'screen_height': '600'
                #'enable_reshade': 'False'
            }

            try:
                with open(config_file, 'w+') as f:
                    parser.write(f)
            except Exception:
                return False
            else:
                return True

def read():
    match initialize():
        case True:
            try:
                parser.read(config_file)
            except Exception as unknonw_error:
                ui_message_box('error', str(unknonw_error))
            else:
                game_name = parser.get('LAUNCHER', 'game')
                honkai_path = pathlib.Path(parser.get('PATHS', r'honkai_impact'))
                genshin_path = pathlib.Path(parser.get('PATHS', r'genshin_impact'))
                screen_width = parser.getint('OPTIONS', 'screen_width')
                screen_height = parser.getint('OPTIONS', 'screen_height')
                #enable_reshade = parser.getboolean('OPTIONS', 'enable_reshade')

                return game_name, honkai_path, genshin_path, screen_width, screen_height #,enable_reshade
        case _:
            pass
    
    return None

def write(section, item, value):
    match initialize():
        case True:
            parser.set(section, item, value)

            try:
                with open(config_file, 'w+') as cfg:
                    parser.write(cfg)
            except Exception as unknown_error:
                ui_message_box('error', str(unknown_error))
            else:
                pass
        case _:
            pass
    
    return None

if __name__ == '__main__':
    pass
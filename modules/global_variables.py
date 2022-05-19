from cmath import nan


try:
    import pathlib
    import modules.configuration
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


def global_variables():
    game_name, honkai_path, genshin_path, screen_width, screen_height = modules.configuration.read()
    background_image_path = pathlib.Path(__file__).parents[1].resolve().joinpath('backgrounds')

    match game_name:
        case 'honkai':
            game_exe = 'BH3.exe'
            game_exe_path = honkai_path.joinpath(game_exe)
            launcher_image = background_image_path.joinpath('honkai.png')
        case 'genshin':
            game_exe = 'GenshinImpact.exe'
            game_exe_path = genshin_path.joinpath(game_exe)
            launcher_image = background_image_path.joinpath('genshin.png')
        case 'starrail':
            game_exe = ''
            game_exe_path = ''
            launcher_image = background_image_path.joinpath('starrail.png')
        case 'zenless':
            pass
        case _:
            game_exe = ''
            game_exe_path = ''
            launcher_image = background_image_path
    
    game_index = 0
    
    url_list = [
        'https://honkaiimpact3.mihoyo.com/asia', 'https://genshin.mihoyo.com',
        'https://www.facebook.com/HonkaiImpact3rd', 'https://www.facebook.com/Genshinimpact',
        'https://twitter.com/HonkaiImpact3rd', 'https://twitter.com/GenshinImpact',
        'https://www.instagram.com/honkaiimpact3rd', 'https://www.instagram.com/genshinimpact',
        'https://www.youtube.com/channel/UCko6H6LokKM__B03i5_vBQQ', 'https://www.youtube.com/c/GenshinImpact',
        'https://www.hoyolab.com/?lang=en-us&utm_source=launcher&utm_medium=game&utm_id=1', 'https://www.hoyolab.com/genshin/?lang=en-us&utm_source=launcher&utm_medium=game&utm_id=2',
        'https://github.com/shirooo39'
    ]
    
    return game_name, game_exe, game_exe_path, game_index, screen_width, screen_height, background_image_path, launcher_image, honkai_path, genshin_path, url_list

if __name__ == '__main__':
    pass


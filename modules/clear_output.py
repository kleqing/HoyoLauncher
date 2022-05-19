try:
    import subprocess
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


def clear_output():
    
    subprocess.run('cls', shell=True)

    return None

if __name__ == '__main__':
    pass


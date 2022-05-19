try:
    import modules.resources
    from PySide6.QtGui import QIcon
    from PySide6.QtWidgets import QMessageBox
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


def message_box(alert_level, text):
    dialog = QMessageBox()

    dialog.setWindowTitle("HoyoLauncher")
    dialog.setWindowIcon(QIcon(':/resources/icons/app_icon.png'))
    match alert_level:
        case 'WARNING' | 'Warning' | 'warning':
            dialog.setIcon(QMessageBox.Warning)
        case 'ERROR' | 'Error' | 'error':
            dialog.setIcon(QMessageBox.Critical)
        case _:
            dialog.setIcon(QMessageBox.Information)
    dialog.setText(str(text))

    dialog.exec()

    return None

if __name__ == '__main__':
    pass


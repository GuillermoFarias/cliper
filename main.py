""" Main server module """

import hupper
from core.app import App
from core.facades.config import config


def main():
    """ server bootstrapper """
    application = App()
    application.boot()


if __name__ == '__main__':
    app = config('app', 'config')
    ENVIRONMENT = app.get('environment')
    DEBUG = bool(app.get('debug'))
    DEBUG_PORT = int(app.get('debug_port'))
    HOT_RELOAD = bool(app.get('hot_reload'))
    NUMBER_PROCESSES = int(app.get('number_processes'))

    if ENVIRONMENT == 'development':
        if DEBUG:
            import debugpy
            debugpy.listen(("0.0.0.0", DEBUG_PORT))

        if HOT_RELOAD:
            reloader = hupper.start_reloader('main.main')

    main()

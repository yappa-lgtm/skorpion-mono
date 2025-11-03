from common.gunicorn import GunicornApplication, get_app_options
from main import main_app
from core.config import settings


def main():
    GunicornApplication(
        application=main_app,
        options=get_app_options(
            host=settings.run.host,
            port=settings.run.port,
            workers=settings.run.workers,
            timeout=settings.run.timeout,
            log_level=settings.logging.log_level,
        ),
    ).run()


if __name__ == "__main__":
    main()

from core.config import settings
from main import main_app


def main():
    if settings.env == "dev":
        import uvicorn

        uvicorn.run(
            "main:main_app",
            host=settings.run.host,
            port=settings.run.port,
            reload=True,
            log_level=settings.logging.log_level,
        )
    else:
        from common.gunicorn import GunicornApplication, get_app_options

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

FROM python:3.12.6-bookworm

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

COPY pyproject.toml uv.lock ./

COPY services/templater/pyproject.toml ./services/templater/

COPY libs/common/pyproject.toml ./libs/common/

COPY libs/common/src ./libs/common/src

COPY services/templater/app ./services/templater/app

RUN uv sync --frozen --no-dev --package templater

RUN chmod +x services/templater/app/prestart.sh || true
RUN chmod +x services/templater/app/run || true

ENTRYPOINT ["./services/templater/app/prestart.sh"]
CMD ["uv", "run", "--package", "templater", "python", "services/templater/app/run"]
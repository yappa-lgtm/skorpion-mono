FROM python:3.12.6-bookworm

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

COPY pyproject.toml uv.lock ./

COPY services/modifier/pyproject.toml ./services/modifier/

COPY libs/common/pyproject.toml ./libs/common/

COPY libs/common/src ./libs/common/src

COPY services/modifier/app ./services/modifier/app

RUN uv sync --frozen --no-dev --package modifier

RUN chmod +x services/modifier/app/prestart.sh || true
RUN chmod +x services/modifier/app/run || true

ENTRYPOINT ["./services/modifier/app/prestart.sh"]
CMD ["uv", "run", "--package", "modifier", "python", "services/modifier/app/run"]
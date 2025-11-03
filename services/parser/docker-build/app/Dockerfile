FROM python:3.12.6-bookworm

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

COPY pyproject.toml uv.lock ./

COPY services/parser/pyproject.toml ./services/parser/

COPY libs/common/pyproject.toml ./libs/common/

COPY libs/common/src ./libs/common/src

COPY services/parser/app ./services/parser/app

RUN uv sync --frozen --no-dev --package parser

RUN chmod +x services/parser/app/prestart.sh || true
RUN chmod +x services/parser/app/run || true

ENTRYPOINT ["./services/parser/app/prestart.sh"]
CMD ["uv", "run", "--package", "parser", "python", "services/parser/app/run"]
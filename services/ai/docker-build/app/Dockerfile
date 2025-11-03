FROM python:3.12.6-bookworm

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

COPY pyproject.toml uv.lock ./

COPY services/ai/pyproject.toml ./services/ai/

COPY libs/common/pyproject.toml ./libs/common/

COPY libs/common/src ./libs/common/src

COPY services/ai/app ./services/ai/app

RUN uv sync --frozen --no-dev --package ai

RUN chmod +x services/ai/app/prestart.sh || true
RUN chmod +x services/ai/app/run || true

ENTRYPOINT ["./services/ai/app/prestart.sh"]
CMD ["uv", "run", "--package", "ai", "python", "services/ai/app/run"]
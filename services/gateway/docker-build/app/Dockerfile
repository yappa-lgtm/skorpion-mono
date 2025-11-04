FROM python:3.12.6-bookworm

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /mono

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

COPY pyproject.toml uv.lock ./
COPY services/gateway/pyproject.toml ./services/gateway/
COPY services/gateway/routes.yml ./services/gateway/
COPY libs/common/pyproject.toml ./libs/common/

RUN uv sync --frozen --package gateway

COPY libs/common/src ./libs/common/src
COPY services/gateway/app ./services/gateway/app

RUN chmod +x services/gateway/app/prestart.sh || true
RUN chmod +x services/gateway/app/run || true

ENTRYPOINT ["./services/gateway/app/prestart.sh"]
CMD ["uv", "run", "--package", "gateway", "python", "services/gateway/app/run"]
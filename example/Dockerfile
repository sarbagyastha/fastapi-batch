FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS builder

ENV PYDEVD_DISABLE_FILE_VALIDATION=1 UV_LINK_MODE=copy

WORKDIR /app/example
ADD . /app
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=/example/uv.lock,target=uv.lock \
    --mount=type=bind,source=/example/pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-editable

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-editable

FROM python:3.12-slim-bookworm
COPY --from=builder --chown=app:app /app/example/.venv /app/example/.venv
COPY /example /app

WORKDIR /app
ENTRYPOINT [ "/app/example/.venv/bin/fastapi" ]
CMD ["run", "--host", "0.0.0.0", "--port", "8000"]
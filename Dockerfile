FROM python:3.14-slim AS builder
COPY --from=ghcr.io/astral-sh/uv:0.12.9 /uv /uvx /bin/

WORKDIR /app

# Add dependency files
COPY pyproject.toml uv.lock ./

# Sync dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked

# Copy source
COPY content/ content/
COPY _static/ _static/
COPY fig/ fig/

# Build all three books
RUN set -eux; \
    cd /app/content/en && uv run jupyter-book build . --path-output ../../english; \
    cd /app/content/es && uv run jupyter-book build . --config es_config.yml --toc es_toc.yml --path-output ../../spanish; \
    cd /app/content/fr && uv run jupyter-book build . --config fr_config.yml --toc fr_toc.yml --path-output ../../french

FROM nginx:alpine-slim
RUN echo 'absolute_redirect off;' > /etc/nginx/conf.d/redirect.conf
COPY index.html /usr/share/nginx/html/index.html
COPY --from=builder /app/english/_build/html /usr/share/nginx/html/en
COPY --from=builder /app/spanish/_build/html /usr/share/nginx/html/es
COPY --from=builder /app/french/_build/html /usr/share/nginx/html/fr

EXPOSE 80

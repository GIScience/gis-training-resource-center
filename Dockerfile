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

# Build books in parallel
FROM builder AS build-en
RUN --mount=type=cache,target=/root/.cache/uv \
    cd /app/content/en && uv run jupyter-book build . --path-output ../../english

FROM builder AS build-es
RUN --mount=type=cache,target=/root/.cache/uv \
    cd /app/content/es && uv run jupyter-book build . --config es_config.yml --toc es_toc.yml --path-output ../../spanish

FROM builder AS build-fr
RUN --mount=type=cache,target=/root/.cache/uv \
    cd /app/content/fr && uv run jupyter-book build . --config fr_config.yml --toc fr_toc.yml --path-output ../../french

FROM nginx:alpine-slim
RUN echo 'absolute_redirect off;' > /etc/nginx/conf.d/redirect.conf
COPY index.html /usr/share/nginx/html/index.html
COPY --from=build-en /app/english/_build/html /usr/share/nginx/html/en
COPY --from=build-es /app/spanish/_build/html /usr/share/nginx/html/es
COPY --from=build-fr /app/french/_build/html /usr/share/nginx/html/fr

EXPOSE 80

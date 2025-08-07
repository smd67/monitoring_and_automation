# Stage 2: Create the final image with Telegraf
FROM python:3.11-slim AS runtime

WORKDIR /backend/src

# Copy the requirements file and install dependencies
RUN pip install poetry

# Copy FastAPI application code
COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root

# Install Telegraf
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    && rm -rf /var/lib/apt/lists/* \
    && wget -qO- https://repos.influxdata.com/influxdata-archive_compat.key | gpg --dearmor | tee /etc/apt/trusted.gpg.d/influxdata.gpg > /dev/null \
    && echo "deb [signed-by=/etc/apt/trusted.gpg.d/influxdata.gpg] https://repos.influxdata.com/debian stable main" | tee /etc/apt/sources.list.d/influxdata.list \
    && apt-get update && apt-get install -y telegraf \
    && rm -rf /var/lib/apt/lists/*

COPY . .

# Expose the port FastAPI will run on
EXPOSE 8002

# Command to run both FastAPI and Telegraf
CMD ["sh", "-c", "telegraf --config /backend/src/telegraf.conf --config /etc/telegraf/telegraf.conf & poetry run uvicorn src.operations:app --host 0.0.0.0 --reload"]
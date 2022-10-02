FROM python:3.10-slim-bullseye

# Working Directory
WORKDIR /app

# Copy source code to working directory
COPY code /app/

# Install packages from requirements.txt
# hadolint ignore=DL3013
RUN pip install --no-cache-dir --upgrade pip &&\
    pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8080

ENTRYPOINT [ "python" ]

CMD ["-u", "app.py"]

# Build with
# docker build -t msaunby/ecm3440-dash:latest .
# Run with
# docker run -p 8080:8080 ecm3440-dash
# Push with
# docker push msaunby/ecm3440-dash:latest
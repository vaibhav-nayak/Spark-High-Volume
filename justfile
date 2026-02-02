download:
    bash ./scripts/download_dataset.sh

download-upload: download
    docker-compose up minio -d
    uv run ./scripts/minio-upload.py

run:
    uv run ./jobs/main.py

start-spark:
    docker-compose up spark-master spark-worker spark-history-server -d

submit-job:
    zip jobs.zip ./jobs/*.py
    docker-compose up submit-job -d

stop-all:
    docker-compose down
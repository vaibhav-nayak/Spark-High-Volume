download:
    bash download_dataset.sh

download-upload: download
    docker-compose up minio -d
    uv run minio-upload.py

run:
    uv run main.py

start-spark:
    docker-compose up spark-driver spark-executor -d

submit-job:
    zip jobs.zip config.py constants.py main.py
    docker-compose up submit-job -d

stop-all:
    docker-compose down
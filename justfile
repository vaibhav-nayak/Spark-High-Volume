download:
    bash download_dataset.sh

download-upload: download
    docker-compose up minio -d
    uv run minio-upload.py

run:
    uv run main.py
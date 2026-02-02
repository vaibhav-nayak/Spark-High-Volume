download:
    bash ./scripts/download_dataset.sh

download-upload: download
    docker-compose up minio -d
    uv run ./scripts/minio-upload.py

run:
    uv run ./jobs/main.py

package-app:
    cd jobs && zip -r ../jobs.zip *.py

stop-all:
    docker-compose down

build: package-app
    docker rmi spark-job:v1
    docker-buildx build -t spark-job:v1 .

deploy:
    kubectl run spark-job  --image=spark-job:v1

kube-setup:
    kubectl create clusterrolebinding spark-submitter-admin \
        --clusterrole=edit \
        --serviceaccount=default:default

setup:  kube-setup
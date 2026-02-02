download:
    bash ./scripts/download_dataset.sh

download-upload: download
    docker-compose up minio -d
    uv run ./scripts/minio-upload.py

package-app:
    cd jobs && zip -r ../jobs.zip *.py

build: package-app
    docker rmi spark-job:v1
    docker-buildx build -t spark-job:v1 .

deploy:
    kubectl run spark-job  --image=spark-job:v1

minio:
    docker-compose up minio

kube-setup:
    kubectl create clusterrolebinding spark-submitter-admin \
        --clusterrole=edit \
        --serviceaccount=default:default

setup:  kube-setup minio
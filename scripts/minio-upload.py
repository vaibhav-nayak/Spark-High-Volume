import os
from minio import Minio
from minio.error import S3Error

MINIO_ENDPOINT = "localhost:9000"
ACCESS_KEY = "minioadmin"
SECRET_KEY = "minioadmin"
BUCKET_NAME = "parquet-data"
LOCAL_FOLDER = "./dataset/fhv_hv_parquet/"

client = Minio(
    MINIO_ENDPOINT,
    access_key=ACCESS_KEY,
    secret_key=SECRET_KEY,
    secure=False
)

def ensure_bucket(bucket_name):
    if not client.bucket_exists(bucket_name):
        client.make_bucket(bucket_name)
        print(f"Created bucket: {bucket_name}")
    else:
        print(f"Bucket already exists: {bucket_name}")

def upload_folder(local_folder, bucket_name):
    for root, _, files in os.walk(local_folder):
        for file in files:
            local_path = os.path.join(root, file)

            object_name = os.path.relpath(local_path, local_folder)

            print(f"Uploading {object_name}...")
            client.fput_object(
                bucket_name=bucket_name,
                object_name=object_name,
                file_path=local_path,
            )

if __name__ == "__main__":
    try:
        ensure_bucket(BUCKET_NAME)
        upload_folder(LOCAL_FOLDER, BUCKET_NAME)
    except S3Error as e:
        print("There is an erro", e)

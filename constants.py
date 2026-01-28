import os

dataset_path = "./dataset/fhv_hv_parquet"


DRIVER_URL = os.getenv("DRIVER_URL", "local[3]")
MINIO_ENDPOINT = os.getenv("MINIO_ENDPOINT", "http://localhost:9000")
MINIO_ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY", "minioadmin")
MINIO_SECRET_KEY = os.getenv("MINIO_SECRET_KEY", "minioadmin")
BUCKET_NAME = os.getenv("BUCKET_NAME", "parquet-data")
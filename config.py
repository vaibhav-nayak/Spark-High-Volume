from pyspark.sql import SparkSession

MINIO_ENDPOINT = "http://localhost:9000"
MINIO_ACCESS_KEY = "minioadmin"
MINIO_SECRET_KEY = "minioadmin"
BUCKET_NAME = "parquet-data"

spark = (
    SparkSession.builder
    .appName("MinIOParquetRead")
    .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:3.3.4,com.amazonaws:aws-java-sdk-bundle:1.12.262")
    .config("spark.hadoop.fs.s3a.aws.credentials.provider", "org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider")
    .config("spark.hadoop.fs.s3a.endpoint", MINIO_ENDPOINT)
    .config("spark.hadoop.fs.s3a.access.key", MINIO_ACCESS_KEY)
    .config("spark.hadoop.fs.s3a.secret.key", MINIO_SECRET_KEY)
    .config("spark.hadoop.fs.s3a.multipart.purge.age", "86400")
    .config("spark.hadoop.fs.s3a.listing.cache.expiration", "86400000")
    .config("spark.hadoop.fs.s3a.connection.establish.timeout", "30000")
    .config("spark.hadoop.fs.s3a.connection.timeout", "60000")
    .config("spark.hadoop.fs.s3a.threads.keepalivetime", "60")
    .config("spark.hadoop.fs.s3a.path.style.access", True)
    .master("local[4]")
    .getOrCreate()
)

# spark = SparkSession.builder.master("spark://127.0.0.1:7077").appName("FHV").getOrCreate()

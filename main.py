from pyspark.sql import SparkSession
from constants import dataset_path

spark = SparkSession.builder.master("spark://127.0.0.1:7077").appName("FHV").getOrCreate()

df = spark.read.parquet(dataset_path)

df.groupby("PULocationID").count().describe().show()
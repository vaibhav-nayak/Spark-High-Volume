from pyspark.sql import SparkSession
from constants import dataset_path

spark = SparkSession.builder.master("local").appName("FHV").getOrCreate()

df = spark.read.parquet(dataset_path)

df.printSchema()
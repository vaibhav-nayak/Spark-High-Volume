from pyspark.sql import Window

from config import spark
import pyspark.sql.functions as F

from constants import BUCKET_NAME

df = (
    spark.read.parquet(f"s3a://{BUCKET_NAME}/")
    .withColumns({
        "year": F.year("pickup_datetime"),
        "month": F.month("pickup_datetime")
    })
    .filter((F.col("year") >= 2020) & (F.col("year") <= 2024))
)

yearly_trip_count = (
    df.groupBy("year", "PULocationID")
    .agg(F.count("*").alias("trip_count"))
)

yearly_thresholds = (
    yearly_trip_count
    .groupBy("year")
    .agg(F.percentile_approx("trip_count", 0.95).alias("p95"))
)

top_zones_per_year = (
    yearly_trip_count
    .join(yearly_thresholds, "year")
    .filter(F.col("trip_count") >= F.col("p95"))
    .select("year", "PULocationID")
)

w = Window.partitionBy("PULocationID").orderBy("year")

top_consecutive_zones = (
    top_zones_per_year
    .withColumn("prev_year", F.lag("year").over(w))
    .withColumn("is_consecutive", F.col("year") == F.col("prev_year") + 1)
    .filter(F.col("is_consecutive"))
    .select("PULocationID")
    .distinct()
)

top_consecutive_monthly_trips = (
    df.join(top_consecutive_zones, "PULocationID")
      .groupBy("year", "month", "PULocationID")
      .agg(F.count("*").alias("zone_month_trips"))
)


monthly_totals = (
    df.groupBy("year", "month")
      .agg(F.count("*").alias("total_month_trips"))
)

top_zones_monthly_share = (
    top_consecutive_monthly_trips
    .join(monthly_totals, ["year", "month"])
    .withColumn(
        "monthly_share",
        F.col("zone_month_trips") / F.col("total_month_trips")
    )
)

w_yoy = Window.partitionBy("PULocationID", "month").orderBy("year")

monthly_share_yoy = (
    top_zones_monthly_share
    .withColumn("prev_year_share", F.lag("monthly_share").over(w_yoy))
    .withColumn(
        "yoy_change",
        F.col("monthly_share") - F.col("prev_year_share")
    )
)

monthly_share_yoy.write.parquet(f"s3a://{BUCKET_NAME}/")

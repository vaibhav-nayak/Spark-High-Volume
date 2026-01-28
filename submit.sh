/opt/spark/bin/spark-submit  \
  --conf "spark.jars.ivy=/tmp/.ivy2" \
  --packages org.apache.hadoop:hadoop-aws:3.3.4 \
  --py-files /app/jobs.zip \
  /app/main.py

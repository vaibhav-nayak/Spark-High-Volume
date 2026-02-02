/opt/spark/bin/spark-submit \
  --master k8s://https://kubernetes.default.svc \
  --conf "spark.jars.ivy=/tmp/.ivy2" \
  --deploy-mode cluster \
  --name spark-job \
  --conf spark.kubernetes.namespace=default \
  --conf spark.kubernetes.authenticate.driver.serviceAccountName=default \
  --conf spark.executor.instances=2 \
  --conf spark.kubernetes.container.image=spark-job:v1 \
  --conf spark.kubernetes.container.image.pullPolicy=Never \
  --packages org.apache.hadoop:hadoop-aws:3.3.4 \
  --py-files local:///app/jobs.zip \
  local:///app/main.py
/opt/spark/bin/spark-submit \
  --master k8s://https://kubernetes.default.svc \
  --deploy-mode cluster \
  --name spark-job \
  --conf spark.kubernetes.namespace=default \
  --conf spark.kubernetes.authenticate.driver.serviceAccountName=default \
  --conf spark.executor.instances=2 \
  --conf spark.kubernetes.container.image=spark-job:v1 \
  --conf spark.kubernetes.container.image.pullPolicy=Never \
  --conf spark.executor.cores=2 \
  --conf spark.executor.memory=1g \
  --conf spark.driver.memory=512m \
  --conf spark.kubernetes.submission.waitAppCompletion=false \
  --py-files local:///app/jobs.zip \
  local:///app/main.py
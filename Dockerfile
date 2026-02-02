FROM apache/spark:4.0.1-python3

RUN curl -o $SPARK_HOME/jars/hadoop-aws-3.3.4.jar \
    https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.4/hadoop-aws-3.3.4.jar && \
    curl -o $SPARK_HOME/jars/aws-java-sdk-bundle-1.12.262.jar \
    https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.262/aws-java-sdk-bundle-1.12.262.jar

COPY ./jobs/main.py /app/main.py
COPY ./jobs.zip /app/jobs.zip
COPY ./scripts/submit.sh /app/submit.sh

CMD [ "bash", "/app/submit.sh" ]

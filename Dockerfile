FROM apache/spark:4.0.1-python3

COPY ./jobs/main.py /app/main.py
COPY ./jobs.zip /app/jobs.zip
COPY ./scripts/submit.sh /app/submit.sh

CMD [ "bash", "/app/submit.sh" ]

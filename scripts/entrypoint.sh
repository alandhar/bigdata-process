#!/bin/bash
set -e

airflow db upgrade

airflow users create \
    --username admin \
    --password admin \
    --firstname admin \
    --lastname admin \
    --role Admin \
    --email admin@example.com || true

airflow connections add 'spark_tgs' \
    --conn-type 'spark' \
    --conn-host "spark://${SPARK_MASTER_HOST_NAME}" \
    --conn-port "${SPARK_MASTER_PORT}" || true

exec airflow webserver

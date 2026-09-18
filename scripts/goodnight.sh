#!/bin/bash
set -e
cd "$(dirname "$0")/.."

for f in docker-compose-kafka docker-compose-airflow docker-compose-spark docker-compose-postgres docker-compose-jupyter; do
    docker-compose -f ./docker/${f}.yml --env-file .env down
done

echo 'All containers stopped.'

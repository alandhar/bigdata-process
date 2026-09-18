# bigdata-process

## Progress

- [x] Challenge 1 — Spark RDD: `spark-scripts/challenge1-rdd-revenue-by-country.py` menghitung total revenue (Quantity x UnitPrice) per Country dari `online-retail-dataset.csv`, murni pakai RDD API. Hasil teratas: United Kingdom (~8.19jt), Netherlands (~284rb), EIRE (~263rb).
  ```sh
  docker exec ${SPARK_WORKER_CONTAINER_NAME}-1 spark-submit \
    --master spark://${SPARK_MASTER_HOST_NAME}:${SPARK_MASTER_PORT} \
    /spark-scripts/challenge1-rdd-revenue-by-country.py
  ```
- [x] Challenge 2 — Spark DataFrame: `spark-scripts/challenge2-dataframe-top-products.py` — top 10 produk (StockCode) berdasarkan total revenue, murni pakai DataFrame/SQL API. Produk teratas: DOTCOM POSTAGE (~206rb), REGENCY CAKESTAND 3 TIER (~165rb), PARTY BUNTING (~98rb).
  ```sh
  docker exec ${SPARK_WORKER_CONTAINER_NAME}-1 spark-submit \
    --master spark://${SPARK_MASTER_HOST_NAME}:${SPARK_MASTER_PORT} \
    /spark-scripts/challenge2-dataframe-top-products.py
  ```
- [ ] Challenge 3 — Spark Data Cleaning ke Postgres
- [ ] Challenge 4 — Spark on Airflow
- [ ] Challenge 5 — Spark Structured Streaming

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
- [x] Challenge 3 — Spark Data Cleaning ke Postgres: `sql/schema.sql` (schema `retail` + tabel `online_retail_raw`) dan `spark-scripts/challenge3-postgres-cleaning.py` — ingest CSV ke `retail.online_retail_raw` via Spark JDBC, lalu bersihkan (hanya United Kingdom, tahun >= 2011) ke tabel baru `retail.online_retail_clean`. Diverifikasi lokal: 541.909 baris raw, 455.353 baris clean (cocok dengan hitungan manual).
  ```sh
  docker exec ${POSTGRES_CONTAINER_NAME} psql -U ${POSTGRES_USER} -d ${POSTGRES_DB} -f /sql/schema.sql
  docker exec ${SPARK_WORKER_CONTAINER_NAME}-1 spark-submit \
    --master spark://${SPARK_MASTER_HOST_NAME}:${SPARK_MASTER_PORT} \
    /spark-scripts/challenge3-postgres-cleaning.py
  ```
- [ ] Challenge 4 — Spark on Airflow
- [ ] Challenge 5 — Spark Structured Streaming

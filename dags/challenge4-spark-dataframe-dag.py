from datetime import timedelta
from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.utils.dates import days_ago

default_args = {
    "owner": "dibimbing",
    "retry_delay": timedelta(minutes=5),
}

challenge4_dag = DAG(
    dag_id="challenge4_spark_dataframe_dag",
    default_args=default_args,
    schedule_interval=None,
    dagrun_timeout=timedelta(minutes=60),
    description="Challenge 4 - submit challenge 2 dataframe job via SparkSubmitOperator",
    start_date=days_ago(1),
)

TopProductsByRevenue = SparkSubmitOperator(
    application="/spark-scripts/challenge2-dataframe-top-products.py",
    conn_id="spark_tgs",
    task_id="challenge2_dataframe_top_products",
    dag=challenge4_dag,
)

TopProductsByRevenue

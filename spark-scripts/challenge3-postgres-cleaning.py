import os
import pyspark
from dotenv import load_dotenv
from pathlib import Path
from pyspark.sql import functions as F
from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    IntegerType,
    FloatType,
)

load_dotenv(dotenv_path=Path("/opt/app/.env"))

postgres_host = os.getenv("POSTGRES_CONTAINER_NAME")
postgres_db = os.getenv("POSTGRES_DB")
postgres_user = os.getenv("POSTGRES_USER")
postgres_password = os.getenv("POSTGRES_PASSWORD")

jdbc_url = f"jdbc:postgresql://{postgres_host}:5432/{postgres_db}"
jdbc_properties = {
    "user": postgres_user,
    "password": postgres_password,
    "driver": "org.postgresql.Driver",
}

sparkcontext = pyspark.SparkContext.getOrCreate(
    conf=(pyspark.SparkConf().setAppName("Dibimbing"))
)
sparkcontext.setLogLevel("WARN")
spark = pyspark.sql.SparkSession(sparkcontext.getOrCreate())

schema = StructType(
    [
        StructField("InvoiceNo", StringType(), True),
        StructField("StockCode", StringType(), True),
        StructField("Description", StringType(), True),
        StructField("Quantity", IntegerType(), True),
        StructField("InvoiceDate", StringType(), True),
        StructField("UnitPrice", FloatType(), True),
        StructField("CustomerID", StringType(), True),
        StructField("Country", StringType(), True),
    ]
)

# table retail.online_retail_raw must already exist, see sql/schema.sql
df = (
    spark.read.option("header", True)
    .schema(schema)
    .csv("/data/online-retail-dataset.csv")
    .withColumn("InvoiceDate", F.to_date("InvoiceDate", "M/d/yyyy H:mm"))
)

df.write.jdbc(
    url=jdbc_url, table="retail.online_retail_raw", mode="append", properties=jdbc_properties
)

raw_df = spark.read.jdbc(url=jdbc_url, table="retail.online_retail_raw", properties=jdbc_properties)

# keep only United Kingdom transactions from 2011 onwards
clean_df = raw_df.filter(
    (F.year("InvoiceDate") >= 2011) & (F.col("Country") == "United Kingdom")
)

clean_df.write.jdbc(
    url=jdbc_url,
    table="retail.online_retail_clean",
    mode="overwrite",
    properties=jdbc_properties,
)

print(f"raw rows: {raw_df.count()}, clean rows: {clean_df.count()}")

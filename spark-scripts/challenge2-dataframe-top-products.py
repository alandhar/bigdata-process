import pyspark
from pyspark.sql import functions as F
from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    IntegerType,
    FloatType,
)

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

df = spark.read.option("header", True).schema(schema).csv("/data/online-retail-dataset.csv")

# top 10 products by revenue (Quantity x UnitPrice)
top_products = (
    df.withColumn("Revenue", F.col("Quantity") * F.col("UnitPrice"))
    .groupBy("StockCode", "Description")
    .agg(F.sum("Revenue").alias("TotalRevenue"), F.sum("Quantity").alias("TotalQuantity"))
    .orderBy(F.col("TotalRevenue").desc())
    .limit(10)
)

top_products.show(truncate=False)

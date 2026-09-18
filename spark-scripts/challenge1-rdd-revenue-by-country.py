import csv
import pyspark

sparkcontext = pyspark.SparkContext.getOrCreate(
    conf=(pyspark.SparkConf().setAppName("Dibimbing"))
)
sparkcontext.setLogLevel("WARN")

raw_rdd = sparkcontext.textFile("/data/online-retail-dataset.csv")
header = raw_rdd.first()

# csv.reader handles quoted commas inside the Description field
rows_rdd = raw_rdd.filter(lambda line: line != header).mapPartitions(
    lambda lines: csv.reader(lines)
)


def to_country_revenue(row):
    quantity = float(row[3])
    unit_price = float(row[5])
    country = row[7]
    return (country, quantity * unit_price)


revenue_by_country = (
    rows_rdd.filter(lambda row: len(row) == 8)
    .map(to_country_revenue)
    .reduceByKey(lambda a, b: a + b)
    .sortBy(lambda kv: -kv[1])
)

for country, revenue in revenue_by_country.collect():
    print(f"{country}: {revenue:,.2f}")

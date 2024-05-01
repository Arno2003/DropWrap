from pyspark.sql import SparkSession
import pandas as pd

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

df = spark.read.option("header", "true").csv(
    'BackEnd\\database\\processed\\Andhra Pradesh.csv')
# Displays the content of the DataFrame to stdout

df.createOrReplaceTempView("data")

sqlDF = spark.sql("SELECT * FROM data")
sqlDF.show()

# df.show()

import sys

from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.context import SparkContext
from pyspark.sql.functions import col, year, month


# Initialize Glue and Spark
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Initialize Glue Job
job = Job(glueContext)
job.init("sales-data-etl", {})


# S3 locations
input_path = "s3://serverless-data-analytics-ivanspinko-2026/raw/sales.csv"
output_path = "s3://serverless-data-analytics-ivanspinko-2026/processed/"


# Read CSV from S3
df = (
    spark.read
    .option("header", "true")
    .option("inferSchema", "true")
    .csv(input_path)
)


# Convert data types
df = df.withColumn(
    "order_date",
    col("order_date").cast("date")
)

df = df.withColumn(
    "quantity",
    col("quantity").cast("integer")
)

df = df.withColumn(
    "price",
    col("price").cast("double")
)


# Create total_amount
df = df.withColumn(
    "total_amount",
    col("quantity") * col("price")
)


# Add partition columns
df = df.withColumn(
    "year",
    year(col("order_date"))
)

df = df.withColumn(
    "month",
    month(col("order_date"))
)


# Write processed data to S3 as Parquet
(
    df.write
    .mode("overwrite")
    .partitionBy("year", "month")
    .parquet(output_path)
)


print("ETL job completed successfully.")
print(f"Input: {input_path}")
print(f"Output: {output_path}")


# Finish Glue Job
job.commit()
# Serverless Data Analytics Platform

A serverless data analytics platform built with AWS services.

## Project Overview

This project is a cloud-based data engineering pipeline that processes sales data using AWS serverless and managed services. The platform will ingest raw CSV data, process and transform it, store the processed data in Amazon S3, and make it available for analytical queries using Amazon Athena.

## Architecture

```
CSV Data
↓
Amazon S3
↓
AWS Lambda
↓
AWS Glue ETL
↓
Amazon S3 (Parquet)
↓
AWS Glue Data Catalog
↓
Amazon Athena
↓
SQL Analytics
```

## AWS Services

- **Amazon S3** — stores raw CSV data and processed Parquet data.
- **AWS Lambda** — reacts to new CSV files uploaded to the raw data location.
- **AWS Glue** — performs ETL transformations and converts CSV data to Parquet.
- **AWS Glue Data Catalog** — stores metadata about the processed dataset.
- **Amazon Athena** — performs serverless SQL analytics.
- **Amazon CloudWatch** — monitors Lambda activity and errors.
- **AWS IAM** — manages permissions for AWS services.

## Data Pipeline

### 1. Data Ingestion

Raw sales data is uploaded to Amazon S3 as a CSV file.

Example location:

```
s3://serverless-data-analytics-ivanspinko-2026/raw/sales.csv
```

### 2. Lambda Trigger

An S3 event notification triggers the `sales-data-trigger` Lambda function when a CSV file is created in the `raw/` path.

The Lambda function receives the S3 event and logs information about the uploaded file.

### 3. ETL Processing

AWS Glue processes the raw CSV data.

The ETL job:

- Reads the CSV file
- Converts columns to appropriate data types
- Calculates `total_amount`
- Extracts year and month from `order_date`
- Writes the transformed data as Parquet

The `total_amount` column is calculated as:

```
quantity × price
```

### 4. Data Partitioning

Processed data is partitioned by year and month.

Example:

```
processed/
  - year=2026/
    - month=9/
      - part-00000-....parquet
```

### 5. Data Catalog

AWS Glue Data Catalog stores metadata about the processed dataset.

- **Database:** `sales_analytics_db`
- **Table:** `processed`

### 6. Analytics

Amazon Athena is used to query the processed Parquet dataset using SQL.

Example:

```sql
SELECT country, SUM(total_amount) AS revenue
FROM "sales_analytics_db"."processed"
GROUP BY country
ORDER BY revenue DESC;
```

The project includes SQL queries for:

- Total revenue
- Revenue by country
- Revenue by product
- Number of orders by country
- Average order value

SQL queries are stored in: `sql/analytics.sql`

## Example Results

Using the included sample dataset:

| Metric              | Result  |
|---------------------|---------|
| Total Revenue       | €4,075  |
| Average Order Value | €407.50 |
| Orders              | 10      |

Revenue by country:

| Country | Revenue |
|---------|---------|
| Ireland | €2,750  |
| France  | €910    |
| Germany | €415    |

## Monitoring

Amazon CloudWatch is used to monitor the Lambda function.

The project dashboard includes:

- Lambda invocations
- Lambda errors

Dashboard: `serverless-data-analytics-dashboard`

## Technologies

AWS, Amazon S3, AWS Lambda, AWS Glue, Amazon Athena, Amazon CloudWatch, AWS IAM, Python, SQL, Apache Spark, Parquet, Git, GitHub

## Skills Demonstrated

- Cloud data ingestion
- ETL development
- Data transformation
- Data partitioning
- Columnar data formats
- Serverless analytics
- SQL data analysis
- AWS IAM
- Cloud monitoring
- Git and GitHub
- AWS data engineering architecture

## Project Status

Completed core data pipeline.

The project demonstrates an end-to-end serverless data engineering workflow from raw CSV ingestion to analytical SQL queries.

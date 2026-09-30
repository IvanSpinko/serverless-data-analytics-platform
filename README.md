\# Serverless Data Analytics Platform



A serverless data analytics platform built with AWS services.



\## Project Overview



This project is a cloud-based data engineering pipeline that processes sales data using AWS serverless and managed services.



The platform will ingest raw CSV data, process and transform it, store the processed data in Amazon S3, and make it available for analytical queries using Amazon Athena.



\## Architecture



```text

CSV Data

&#x20;  ↓

Amazon S3

&#x20;  ↓

AWS Lambda

&#x20;  ↓

AWS Glue ETL

&#x20;  ↓

Amazon S3 (Parquet)

&#x20;  ↓

AWS Glue Data Catalog

&#x20;  ↓

Amazon Athena

&#x20;  ↓

SQL Analytics


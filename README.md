# AWS Serverless Data Processing Dashboard

## 📌 Project Overview
This project demonstrates a serverless data processing pipeline using AWS services.
When a CSV file is uploaded to Amazon S3, an AWS Lambda function automatically processes the data and saves the transformed output to another S3 bucket.

## 🛠️ AWS Services Used
- Amazon S3
- AWS Lambda
- AWS IAM
- AWS Budgets (cost control)

## 🔄 Architecture
1. CSV uploaded to **Raw S3 Bucket**
2. S3 event triggers **Lambda Function**
3. Lambda processes data (totals, averages, transformations)
4. Processed CSV saved to **Processed S3 Bucket**

## 📂 Project Structure

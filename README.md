# AWS S3 + Lambda Automation (Serverless Project)

## 📌 Project Overview

This project demonstrates a real-world serverless architecture using AWS services.  
An S3 bucket is configured to trigger a Lambda function automatically whenever a file is uploaded.

The Lambda function processes the event and logs the file details in CloudWatch.

---

## 🚀 Architecture

S3 Bucket → Lambda Function → CloudWatch Logs

---

## 🛠️ Technologies Used

- AWS S3
- AWS Lambda
- AWS CloudWatch
- IAM (Identity and Access Management)
- Python

---

## ⚙️ Implementation Steps

### 1. S3 Bucket Setup
- Created S3 bucket
- Enabled event notification
- Configured trigger for object upload

### 2. Lambda Function
- Created function using Python runtime
- Wrote code to process S3 event

### 3. Permissions
- Attached IAM role with S3 access

### 4. Integration
- Connected S3 event trigger to Lambda

### 5. Testing
- Uploaded file to S3
- Verified logs in CloudWatch

---

## 💻 Lambda Code

```python
import json

def lambda_handler(event, context):

    print("File uploaded successfully!")

    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        file_name = record['s3']['object']['key']

        print(f"Bucket: {bucket}")
        print(f"File: {file_name}")

    return {
        'statusCode': 200,
        'body': json.dumps('Lambda triggered')
    }

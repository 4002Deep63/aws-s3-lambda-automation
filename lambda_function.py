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

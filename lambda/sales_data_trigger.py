import json


def lambda_handler(event, context):
    print("S3 event received:")
    print(json.dumps(event, indent=2))

    for record in event["Records"]:
        bucket_name = record["s3"]["bucket"]["name"]
        object_key = record["s3"]["object"]["key"]

        print(f"Bucket: {bucket_name}")
        print(f"File: {object_key}")

    return {
        "statusCode": 200,
        "body": "S3 event processed successfully"
    }
import boto3
import csv
import io

RAW_BUCKET = 'pramila-dashboard-raw'
PROCESSED_BUCKET = 'pramila-dashboard-processed'

s3 = boto3.client('s3')

def lambda_handler(event, context):
    file_name = event['Records'][0]['s3']['object']['key']

    obj = s3.get_object(Bucket=RAW_BUCKET, Key=file_name)
    data = obj['Body'].read().decode('utf-8').splitlines()
    reader = csv.DictReader(data)

    total = 0
    count = 0
    processed_rows = []

    for row in reader:
        sales = float(row['Sales'])
        total += sales
        count += 1
        row['Processed_Sales'] = sales * 1.1
        processed_rows.append(row)

    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=processed_rows[0].keys())
    writer.writeheader()
    writer.writerows(processed_rows)

    s3.put_object(
        Bucket=PROCESSED_BUCKET,
        Key=f"processed_{file_name}",
        Body=output.getvalue()
    )

    return {
        "statusCode": 200,
        "body": f"Processed {file_name}"
    }

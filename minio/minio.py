import boto3
from botocore.exceptions import ClientError

# Set up MinIO client
s3 = boto3.client('s3',
                  endpoint_url='http://localhost:9000',
                  aws_access_key_id='minio_admin',
                  aws_secret_access_key='minio_password')

buckets = ['raw', 'dbt']

for name in buckets:
    try:
        # Create a 'raw' bucket
        s3.create_bucket(Bucket=name)
        print(f"Bucket {name} created succesfully")

    except ClientError as e:
        print(f"Error: {e}")

## Upload a file to the bucket
#s3.upload_file('myfile.txt', 'mybucket', 'myfile.txt')

## List objects in the bucket
#response = s3.list_objects(Bucket='mybucket')
#for obj in response.get('Contents', []):
#    print(obj['Key'])
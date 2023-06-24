import boto3
import subprocess

# Configuration
aws_region = 'us-west-2'
bucket_name = 'your-bucket-name'
file_path = '/path/to/your/file.txt'
backup_key = 'backup/file.txt'

# Create an S3 client
s3_client = boto3.client('s3', region_name=aws_region)

# Generate a backup file name
backup_file_name = file_path.split('/')[-1] + '.backup'

# Create a backup using subprocess
subprocess.run(['cp', file_path, backup_file_name], check=True)

try:
    # Upload the backup file to S3
    s3_client.upload_file(backup_file_name, bucket_name, backup_key)
    print(f'Successfully backed up {file_path} to S3 bucket: {bucket_name} with key: {backup_key}')
except Exception as e:
    print(f'Error occurred while uploading backup to S3: {str(e)}')
finally:
    # Clean up the backup file
    subprocess.run(['rm', backup_file_name], check=True)

# AWS EC2 Data Backup

This Python script automates the backup of a file on an EC2 instance to an AWS S3 bucket.

## Prerequisites

- An EC2 instance with AWS CLI configured
- AWS S3 bucket created

## Usage

1. Update the script with your AWS configuration details and desired backup settings.
2. Save the script on your EC2 instance.
3. Execute the script to perform the backup.

## Configuration

- `aws_region`: The AWS region where your S3 bucket is located.
- `bucket_name`: The name of your S3 bucket.
- `file_path`: The path to the file you want to back up on your EC2 instance.
- `backup_key`: The key under which the backup file will be stored in the S3 bucket.

## Additional Enhancements

Feel free to modify or extend the script to include additional features such as backup rotation, encryption, logging, and more. 

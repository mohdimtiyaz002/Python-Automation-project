import boto3


# To check the list of buckets present in your aws account
s3 = boto3.resource('s3')

def show_buckets(s3):
    for bucket in s3.buckets.all():
        print(bucket.name)

 #To count the no of buckets
      #C = 0
      # for bucket in s3.buckets.all():
      # print(bucket.name)
      # C = c+1
      # Print (c)       

#To uplode files in the bucket
def upload_to_bucket(s3,file_name,bucket_name,key_name):
    print("Uploading file to S3")
    data = open(file_name, 'rb')
    s3.Bucket(bucket_name).put_object(Key=key_name, Body=data)
    print("File uploaded to S3")

#To downlode files from the bucket
def download_from_bucket(s3,file_name,bucket_name,key_name):
    print("Downloading file from S3")
    s3.Bucket(bucket_name).download_file(key_name, file_name)
    print("File downloaded from S3")
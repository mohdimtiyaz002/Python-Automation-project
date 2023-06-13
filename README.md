# Python-Automation-project
Python + AWS Automation using boto3 project 

In this project we learn 3 things

a) checking the total buckets present in #AWS_account with names and total count

b) downloading files from #S3_bucket to your remote machine

c) uploading files from your remote machine to #S3_bucket 


STEP 1: login to your #AWS_console 

STEP 2: Create a user

We can create as many uses as we want 

In the #IAM_console:

-Go to the Users tab , Click on Add users , Enter a username , Tick the Access key — Programmatic access field (essential),  Click Next and Attach existing policies directly. ,  Select the Administrator Access policy , Click Next and Create user , Finally, download the given CSV file of your user's credentials.



STEP 3 :  Create a bucket

Let's create a few buckets give them  names and upload some files  through console 

STEP 4: on your #Vscode download #boto3 and #AWS_CLI then configure it by entering access key and secret access key 

STEP 5: to check the total number of buckets in our AWS , the following code will give you all the names of buckets present in your  #AWS_account 

s3 = boto3.resource("s3")

# Print out bucket names

for bucket in s3.buckets.all():

    print(bucket.name)

STEP 6: to count the number of buckets in your AWS account

C = 0

for bucket in s3.buckets.all():

    print(bucket.name)

C = c+1

Print (c)

STEP 7 : Using #Python_Boto3 to download files from the S3 bucket to your pc

s3.download_file(
    Bucket="     "
    Key="   "
    Filename="   "
)

STEP 8 : now to upload the files using #python from your pc to #S3_bucket

s3.upload_file(
  Filename="   ",
    Bucket="  ",
    Key="  ",
)

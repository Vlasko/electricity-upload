# Standard Library Imports
import os
import sys

# Third Party Imports
import boto3
from botocore.exceptions import NoCredentialsError

# Local Application Imports
path_prefix = os.path.split(os.getcwd())[0]
sys.path.append(path_prefix+'/Fridge_Flex/Keys')
from AWS_keys import ACCESS_KEY, SECRET_KEY

def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False

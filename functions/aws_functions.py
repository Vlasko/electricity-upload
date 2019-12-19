# Standard Library Imports

# Third Party Imports
from boto3 import client
from botocore.exceptions import NoCredentialsError

# Local Application Imports
from keys.AWS_keys import ACCESS_KEY, SECRET_KEY

def upload_to_aws(local_file, bucket, s3_file):
    s3 = client('s3', aws_access_key_id=ACCESS_KEY,
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

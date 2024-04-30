import os
import dotenv
import pandas

from pyathena import connect

dotenv.main.load_dotenv()

aws_access_key_id = os.getenv('aws_access_key_id')
aws_secret_access_key = os.getenv('aws_secret_access_key')
region_name = os.getenv('region_name')
s3_staging_dir = os.getenv('s3_staging_dir')

conn = connect(aws_access_key_id = aws_access_key_id,aws_secret_access_key=aws_secret_access_key,s3_staging_dir=s3_staging_dir, region_name = region_name).cursor()


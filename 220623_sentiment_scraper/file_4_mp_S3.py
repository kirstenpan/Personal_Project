import os
import json
import boto3

from file_0_mp import *
if on_vm == False: os.chdir(os.path.dirname(__file__))

s3 = boto3.resource('s3')
bucket =  'civilience-data'

for filename in os.listdir('topic_files'):
    #the first argument is local filepath, second argument is S3 filepath we want inside a bucket
    s3.Bucket(bucket).upload_file(f"topic_files/{filename}", f'twitter_topic_historical/{filename}')
    os.remove(f"topic_files/{filename}")

for filename in os.listdir('json_files'):
    s3.Bucket(bucket).upload_file(f"json_files/{filename}", f'twitter_topic_historical/{filename}')
    os.remove(f"json_files/{filename}")

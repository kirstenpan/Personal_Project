import json
import boto3
import pandas as pd
import os
import sys

from file_0_mp import *
from file_1_mp_scraper import *
if on_vm == False: os.chdir(os.path.dirname(__file__))

def load_csv(filename):
    s3 = boto3.resource('s3')

    bucket =  'civilience-data'
    key = f'twitter_topic_historical/{filename}'

    print('retrieving', key)
    obj = s3.Object(bucket, key)
    df = pd.read_csv(obj.get()['Body'])[0:100]
    return df

from datetime import date, datetime, timedelta

<<<<<<< HEAD:2206_internship_program/220623_project2/file_2_mp_download.py
filename = 'monkeypox'
for day in range(7):
    ref_date = '220627' #we input the starting day, and this date will keep INCREASING (if we input 220501 -> 220502...)
=======
def dateToStr(date):
  return datetime.strftime(date, '%Y-%m-%d')
  
# filename = 'monkeypox'
filename = sys.argv[1]

for day in range(7):
    datetime.today()
    ref_date = datetime.today().strftime("%Y%m%d")[2:] #we input the starting day, and this date will keep INCREASING (if we input 220501 -> 220502...
>>>>>>> main:2206_internship_program/220623_sentiment_scraper/file_2_mp_download.py
    date_ = datetime.strptime('20'+ref_date, "%Y%m%d").date() - timedelta(days=day) #does not take today into account, careful
    date_ = str(date_).replace('-', '')[2:]
    try:
        df = load_csv(f'{filename}_{date_}.csv')
        print('success', f'{filename}_{date_}.csv')
        #if you load the file from S3 then save on local
        df.to_csv(f'topic_files/{filename}_{date_}.csv', index=None)
    except:
        print('err', f'{filename}_{date_}.csv')
        #scrape then save on local
        df = scrape_twitter(filename, date_, 2)
        df.to_csv(f'topic_files/{filename}_{date_}.csv', index=None)
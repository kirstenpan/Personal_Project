#set the path to relative
import os
from file_0_mp import *
if on_vm == False: os.chdir(os.path.dirname(__file__))

#run entire pipeline
import file_1_mp_scraper
os.system('python3 file_2_mp_download.py monkeypox')
import file_3_mp_sentiment_analysis
import file_4_mp_S3

print('completed')
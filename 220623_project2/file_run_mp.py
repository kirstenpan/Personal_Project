#set the path to relative
import os
from file_0_mp import *
if on_vm == False: os.chdir(os.path.dirname(__file__))

#run entire pipeline
import file_1_mp_scraper
import file_2_mp_download
import file_3_mp_sentiment_analysis

print('completed')
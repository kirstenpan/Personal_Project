#set the path to relative
import os
from file_0 import *
if on_vm == False: os.chdir(os.path.dirname(__file__))

#run entire pipeline
import file_1_scraper
import file_2_encoding
import file_3_clustering
import file_4_zeroshot
# import file_5_visualize

print('completed')
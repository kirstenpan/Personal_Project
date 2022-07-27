import pandas as pd
from textblob import TextBlob
from tqdm import tqdm
from statistics import mean
import os
import json

from file_0_mp import *
if on_vm == False: os.chdir(os.path.dirname(__file__))

filename_list = set()
for file in os.listdir('topic_files'):
    filename_list.add(file.split('_')[0])
    print(filename_list)

for topic in list(filename_list):
    #create an empty dictionary
    sentiment_dictionary = {}

    for file in os.listdir('topic_files'):
        if topic in file:
            #read in all the csv files
            df = pd.read_csv('topic_files/'+file)
            #create sentiment columns for each csv file
            df['sentiment'] = df['Text'].apply(lambda x : TextBlob(x).sentiment[0])
            df.to_csv(f'topic_files/' + file, index=None)

            #calculate avg sentiment for each row
            avgSen = mean(df['sentiment'])

            #add all the avg sentiments to a dictionary    
            sentiment_dictionary[file.split("_")[1][:-4]] = avgSen

    print(sentiment_dictionary)
    #save to json
    with open(f'json_files/{topic}.json', 'w') as file:
        json.dump(sentiment_dictionary, file)




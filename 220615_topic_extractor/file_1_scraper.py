#import variables and functions
from file_0 import *
# importing libraries and packages
import snscrape.modules.twitter as sntwitter
import pandas as pd
import progressbar
from time import sleep
from datetime import datetime
#set path to this folder
import os
if on_vm == False: os.chdir(os.path.dirname(__file__)) #os.chdir not working on vm

movie_dict = {
    'vaccine': ['covid vaccine since:2022-06-08 until:2022-06-09', 1000]
}

today = datetime.today().strftime('%Y%m%d')[2:]+'_'
for index, movie_name in enumerate(movie_dict):
    print(movie_name, '%')
    tweets_list1 = []
    bar = progressbar.ProgressBar(maxval=movie_dict[movie_name][1]+2, widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
    bar.start()
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'{movie_dict[movie_name][0]}').get_items()): #declare a username
        bar.update(i+1)
        if i>movie_dict[movie_name][1]: #number of tweets you want to scrape
            break
        #print(movie_name, i, tweet)
        tweets_list1.append([tweet.date, tweet.id, tweet.content, tweet.username]) #declare the attributes to be returned
    tweets_df1 = pd.DataFrame(tweets_list1, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
    #tweets_df1[['Datetime', 'Text']].to_csv(f'{today+movie_name}.csv', index=None)
    tweets_df1[['Datetime', 'Text']].to_csv(PATH+'df_0_raw.csv', index=None)
    bar.finish()
    #look at the file

tweets_df1
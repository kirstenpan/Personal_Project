import os
import snscrape.modules.twitter as sntwitter
import pandas as pd
import progressbar
from time import sleep
from datetime import datetime, timedelta
import os
from datetime import datetime, timedelta

from file_0_mp import *
if on_vm == False: os.chdir(os.path.dirname(__file__))

def dateToStr(date):
  return datetime.strftime(date, '%Y-%m-%d')

def scrape_twitter(topic_name, ref_date, days):
    date1 = datetime.strptime('20'+ref_date, "%Y%m%d").date() #does not take today into account, careful
    date2 = date1 + timedelta(days=days)
    # today = dateToStr(datetime.today())
    # yesterday = dateToStr(datetime.today() - timedelta(1))

    movie_dict = {
        topic_name: [f"{topic_name} since:{date1} until:{date2}", 2000]
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
        bar.finish()
        #save file
        date_str = (date2-timedelta(1)).strftime('%Y%m%d')[2:]+'_'
        return tweets_df1[['Datetime', 'Text']] #.to_csv(f'{date_str+movie_name}.csv', index=None)

<<<<<<< HEAD:2206_internship_program/220623_project2/file_1_mp_scraper.py
#print(scrape_twitter('monkeypox', '220615', 2))
for i in range(7):
    ref_date = '220620'
    date1 = datetime.strptime('20'+ref_date, "%Y%m%d").date() #does not take today into account, careful
    date2 = (date1 + timedelta(days=i)).strftime('%Y%m%d')[2:]

    print(scrape_twitter('monkeypox', date2, 2))
=======
# print(scrape_twitter('monkeypox', '220626', 2))
>>>>>>> main:2206_internship_program/220623_sentiment_scraper/file_1_mp_scraper.py

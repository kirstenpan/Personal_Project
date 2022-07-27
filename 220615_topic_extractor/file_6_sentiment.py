import pandas as pd
from textblob import TextBlob
from tqdm import tqdm
from file_0 import *
from statistics import mean
import os
if on_vm == False: os.chdir(os.path.dirname(__file__))

# import original csv file
df = pd.read_csv('df_0_raw.csv').dropna()

# loop through every row of the csv file, add another column to track the sentiments for each row
tqdm.pandas()
df['sentiment'] = df['Text'].progress_apply(lambda x : TextBlob(x).sentiment[0])

# calculate the average of the last column
avgSen = mean(df['sentiment'])
print (avgSen)

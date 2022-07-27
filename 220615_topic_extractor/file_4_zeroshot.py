#import variables and functions
from file_0 import *
#set path to this folder
import os
if on_vm == False: os.chdir(os.path.dirname(__file__))
#import rest of the libraries to execute this .py
import numpy as np
from sentence_transformers import SentenceTransformer
import pandas as pd

model = SentenceTransformer('all-MiniLM-L6-v2') #all-MiniLM-L6-v2 #all-mpnet-base-v2

#import dataset
df = pd.read_parquet(PATH+'df_2_clustered.parquet')

#add a column with zeroshot (keywords) values
#model is the encoder, ex. from sentence-transformers
df['zeroshots'] = zeroshot(df['Text'], df['text_vector_'], model, 1000, 3)
df = df.sort_values('clusters')

#save the clustered file
df.to_parquet(PATH+'df_2_clustered.parquet', index=None)
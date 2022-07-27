#import variables and functions
from file_0 import *
#set path to this folder
import os
if on_vm == False: os.chdir(os.path.dirname(__file__))
#import rest of the libraries to execute this .py
import numpy as np
from sklearn.cluster import KMeans
import pandas as pd

#load encoded files
df = pd.read_parquet(PATH+'df_1_encoded.parquet')

#perfrom clustering on the vectors
kmeans = KMeans(n_clusters=10, random_state=0) #load model
kmeans.fit(df['text_vector_'].values.tolist()) #perform clustering

#creates a new column assigning each samples (text) to a cluster
df['clusters']=kmeans.labels_
df

#save the clustered file
df.to_parquet(PATH+'df_2_clustered.parquet', index=None)
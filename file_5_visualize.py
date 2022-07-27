#import variables and functions
from file_0 import *
#set path to this folder
import os
if on_vm == False: os.chdir(os.path.dirname(__file__))
#import rest of the libraries to execute this .py
import umap
import matplotlib.pyplot as plt
import pandas as pd

#load encoded files
df = pd.read_parquet(PATH+'df_2_clustered.parquet')

#dim reduction
umap_embeddings = umap.UMAP(
    n_neighbors=22, 
    n_components=2, 
    metric='cosine'
).fit_transform(df['text_vector_'].values.tolist())

#components
fig = plt.figure(figsize=(14, 8))
x = list(umap_embeddings[:,0])
y = list(umap_embeddings[:,1])
# x and y given as array_like objects

#graph data
import plotly.express as px
fig = px.scatter(df, x=x, y=y, hover_name=df['Text'], color=df['clusters'])
fig.update_traces(textfont_size=22)
fig.show()
# python-daemon==2.2.3
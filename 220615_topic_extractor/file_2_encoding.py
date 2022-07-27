# from distutils.command.install_lib import install_lib
# from gettext import install
# from tarfile import PAX_NAME_FIELDS

#import variables and functions
from file_0 import *
#set path to this folder
import os
if on_vm == False: os.chdir(os.path.dirname(__file__))
#import rest of the libraries to execute this .py
import pandas as pd
from tqdm import tqdm
from sentence_transformers import SentenceTransformer
tqdm.pandas()

model = SentenceTransformer('all-MiniLM-L6-v2') #all-MiniLM-L6-v2 #all-mpnet-base-v2

#load the csv file to df
df = pd.read_csv(PATH+'df_0_raw.csv').dropna()

#creates a new column with the encoded text
df['text_vector_'] = df['Text'].progress_apply(lambda x : model.encode(x).tolist())
df

#save the encoded csv file
df.to_parquet(PATH+'df_1_encoded.parquet', index=None)
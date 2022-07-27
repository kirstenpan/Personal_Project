import nltk
import ssl
import numpy as np
#solves nltk issues, without this, nltk.download() throws an error
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
nltk.download('stopwords')
nltk.download('punkt')
stopwords = nltk.corpus.stopwords.words('english')
from sklearn.metrics.pairwise import euclidean_distances
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

def zeroshot(df_text, df_text_vectors, model, top_common, top_sample):
    #df_text is the list of text
    #df_text is the list of vecotrized text

    #tokenize all words
    all_words = []
    for t in df_text:
        all_words += nltk.tokenize.word_tokenize(t)
    all_words

    #frequency dictionary
    all_words_dist = nltk.FreqDist(w.lower() for w in all_words)
    all_words_except_stop_dist = nltk.FreqDist(w.lower() for w in all_words if w not in stopwords and w.isalnum() and len(w) != 1)

    #dictionary of vectorized top frequent words
    dictionary_words = [{"_id": i,"label": w[0], "label_vector_": model.encode(w[0])} for i, w in enumerate(all_words_except_stop_dist.most_common(top_common))]

    #
    closest_topn_index = np.argsort(euclidean_distances(
        [d for d in df_text_vectors], 
        np.array([vectorized_word["label_vector_"] for vectorized_word in dictionary_words])
    ), axis=1)[:, :top_sample]

    word_list = list()
    count = 0
    for vector in df_text_vectors:
        tags = []
        for ind in closest_topn_index[count]:
            tags.append(dictionary_words[ind]["label"])
        word_list.append(tags)
        count += 1

    #we obtain a list of lists, long as the sample itself
    return word_list

import socket

PATH = ''
on_vm = False
if socket.gethostname().find('ec2') != -1:
    on_vm = True
    PATH = 'civilience/2206_internship_program/220615_scraping_pipeline/'

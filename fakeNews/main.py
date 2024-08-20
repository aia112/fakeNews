#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pickle
from dataClean import clean
from nltk import word_tokenize
import numpy as np
from newspaper import Article


# In[2]:


### LOAD THE MODEL ###
with open("pickles/model", "rb") as pick:
    model = pickle.load(pick)
#### LOAD VECTORS #####
with open("pickles/titleVector", 'rb') as pick:
    titleVector = pickle.load(pick)
with open("pickles/textVector", 'rb') as pick:
    textVector = pickle.load(pick)


# In[76]:


#### HERE WRITE NEWSPAPER CODE FOR TAKING URL AS INPUT
#### FETCH article AND title
def main(url):
    # url=input("url?") ## Enter url here
    obj=Article(url) ##Creating object of class Article
    obj.download()
    obj.parse()
    article = obj.text
    title = obj.title


    # In[77]:


    def l2s(X):
        return " ".join(X)


    # In[78]:


    article = l2s(clean(article, True))
    title = l2s(clean(title, True))


    # In[79]:


    def vectorize(title, text):
        titleArray = titleVector.transform([title]).toarray()
        textArray = textVector.transform([text]).toarray()
        vector = np.concatenate((titleArray, textArray), axis=1)
        return vector


    # In[80]:


    vector = vectorize(title, article)


    # In[81]:


    prob = model.predict_proba(vector)
    result = model.predict(vector)
    # print(obj.title)
    # print("Probablity of False: ", prob[0][0])
    # print("probability of True:", prob[0][1])
    # print("News is henceforth, ", result[0])
    return obj.title, obj.text, prob[0][0], prob[0][1], result[0]

    #

    # In[ ]:

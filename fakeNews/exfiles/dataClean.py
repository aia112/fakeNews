#!/usr/bin/env python
# coding: utf-8

# In[ ]:


########### Write all data cleaning/pre-processing functions in this Module only #################
########### Remember to use str.lower() before using any of the functions ########################
########### Use Comments and Proper Identifier Names #################


# In[1]:


import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import SnowballStemmer 


# In[4]:



def remove_punctuations(token):
    token = re.sub(r'[^\w\s]|[_]', '', token)
    return token


# In[5]:


def remove_digits(token, space = True):
    token = re.sub(r'\d', ' ', token)
    if space:
        token = remove_spaces(token)
    return token


# In[6]:


####### Removes More Multiple(More than 1 consecutive) spaces ##########
def remove_spaces(token):
    token = re.sub(r'[\s]+', ' ', token)
    return token


# In[7]:


####### Only Works for single word tokens and not sentences #########
def remove_stopwords(token, stopWordList = stopwords.words('english'), noPunctuations = True):    
    if noPunctuations:
        for i in range(len(stopWordList)):
                stopWordList[i] = remove_punctuations(stopWordList[i])
    if type(token) is list:
		words=list()
		for i in token:
			if i not in stopWordList:
				words.append(i)
		return words
    elif token not in stopWordList:
        return token


# In[8]:


####### Use this to remove None objects from List after removing stopwords ####### 
def remove_None(LIST):
    return list(filter(None, LIST))


# In[31]:


def stem(tokens, porter= False, lancaster= False, snowball= False):
    stemmed_tokens = []
    if porter:
        for i in tokens:
            stemmed_tokens.append(PorterStemmer().stem(i))
    elif lancaster:
        for i in tokens:
            stemmed_tokens.append(LancasterStemmer().stem(i))
    elif snowball:
        for i in tokens:
            stemmed_tokens.append(SnowballStemmer('english').stem(i))
    return stemmed_tokens


# In[33]:


test = "'Its a lore-m ips_sum 2 test data zeus ./ with punctuation? t856"


# In[ ]:





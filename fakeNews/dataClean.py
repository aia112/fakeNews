#!/usr/bin/env python
# coding: utf-8

# In[ ]:


########### Write all data cleaning/pre-processing functions in this Module only #################
########### Remember to use str.lower() before using any of the functions ########################
########### Use Comments and Proper Identifier Names #################


# In[4]:

from word2number import w2n
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.stem.snowball import SnowballStemmer 
from nltk.stem import WordNetLemmatizer
import pandas as pd
# In[5]:



def remove_punctuations(token):
    token = re.sub(r'[^\w\s]|[_]', '', token)
    return token


# In[6]:


def remove_digits(token, space = True):
    token = re.sub(r'\d', ' ', token)
    if space:
        token = remove_spaces(token)
    return token


# In[7]:


####### Removes More Multiple(More than 1 consecutive) spaces ##########
def remove_spaces(token):
    token = re.sub(r'[\s]+', ' ', token)
    return token


# In[10]:


####### Only Works for single word tokens and not sentences #########
def remove_stopwords(token, stopWordList = stopwords.words('english'), noPunctuations = True):
    if noPunctuations:
        for i in range(len(stopWordList)):
                stopWordList[i] = remove_punctuations(stopWordList[i])
    if type(token) is list:
        words = list()
        for i in token:
            if i not in stopWordList:
                words.append(i)
        return words
    elif token not in stopWordList:
        return token


# In[1]:


####### Use this to remove None objects from List after removing stopwords ####### 
def remove_None(LIST):
    return list(filter(None, LIST))


# In[2]:


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

# idhar se daalra hoon dono function
stop=stopwords.words('english')
stop.extend(['said','day','year','month','also','week','take','would','came','come','thought','think','told','well','much','mostly','likely'])
#print(stop, len(stop))
for i in range(len(stop)):
    stop[i]=stop[i].lower()


stemmer=SnowballStemmer("english")
lemmatizer=WordNetLemmatizer()

def clean_complete(func):
	def inner(word, absolute = False):
		words = word_tokenize(word)
		return func(words, absolute)
	return inner


@clean_complete
def clean(word, absolute = False):
   l1=[]
   l2=[]
   l3=[]	
   if absolute:
       word = removehyphen_underscore(word)
   for i in word:
      if not i.lower() in stop:      ## removing stopwords ##
        l1.append(i.lower())
      else:
        continue  
   
   

   for i in range(len(l1)):
        if l1[i] in w2n.american_number_system:  ## converting words to digits ##
            l1[i]=str(w2n.word_to_num(l1[i]))
   

   for i in l1:
      
      if re.match('^([A-Za-z]|[A-Za-z][0-9]*|[0-9]*[A-Za-z])+$',i):
        l2.append(i)
   for i in range(len(l2)):
       tag=nltk.pos_tag([l2[i]])
       if tag[0][1]=="NN" or tag[0][1]=="NNP" or tag[0][1]=="NNS" or tag[0][1]=="NNPS" or tag[0][1]=="RB" or tag[0][1]=="RBR" or tag[0][1]=="RBS" or tag[0][1]=="JJ" or tag[0][1]=="JJR" or tag[0][1]=="JJS":  ## stemming words;except noun and proper noun and adjective and adverb ##
           continue
       else:
           l2[i]=stemmer.stem(l2[i])
   for i in range(len(l2)):
       tag=nltk.pos_tag([l2[i]])
       if tag[0][1]=="NNS" or tag[0][1]=="NNPS":           
           l2[i]=lemmatizer.lemmatize(l2[i],pos='n')                          ##lemmatization of
       if tag[0][1]=="RB" or tag[0][1]=="RBR" or tag[0][1]=="RBS":            ##plural nouns,
           l2[i]=lemmatizer.lemmatize(l2[i],pos='r')                          ##adverbs,
       if tag[0][1]=="JJ" or tag[0][1]=="JJR" or tag[0][1]=="JJS":            ##adjectives
           l2[i]=lemmatizer.lemmatize(l2[i],pos='a')
   
   for i in range(len(l2)):
       if (len(l2[i])>1):
           l3.append(l2[i])
       else:
           continue
   return l3

def removehyphen_underscore(token,x=[],z=" ",k=" "):
    y=' '.join(token)
    x=y.split("_")
    z=' '.join(x)
    x.clear()
    x=z.split("-")
    k=' '.join(x)
    x.clear()
    x=k.split(" ")
    return x
#fr=nltk.FreqDist()

#idhar loop daaldena
#word=word_tokenize(df.iloc[400]['Text'])
#fcl=removehyphen_underscore(word)
#ufcl=clean(word_tokenize("removehyphen_underscore"), absolute= True)
#print(ufcl)
#fr=nltk.FreqDist(cl)




# In[7]:


test = "'Its a lore-m ips_sum 2 test data zeus ./ with punctuation? t856"

##print(clean(test, True))

# In[8]:


#nltk.word_tokenize(remove_punctuations(test))


# In[11]:


#text = "He is a  ABC gaurav"
#remove_stopwords(nltk.word_tokenize(text.lower()))


# In[ ]:





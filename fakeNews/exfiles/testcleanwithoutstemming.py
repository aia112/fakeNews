import nltk
from nltk.tokenize import word_tokenize
import pandas as pd
from nltk.corpus import stopwords
import re
from word2number import w2n
from nltk.stem.snowball import SnowballStemmer 
from nltk.stem import WordNetLemmatizer

df=pd.read_csv('dataset/Titledataset.csv')
stop=stopwords.words('english')
for i in range(len(stop)):
    stop[i]=stop[i].lower()
word=word_tokenize(df['Text'][200])

stemmer=SnowballStemmer("english")
lemmatizer=WordNetLemmatizer()
def clean(word,l1=[],l2=[],l3=[]):
   
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
   
   return l2

def removehyun(token,x=[],z=" ",k=" "):
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


fcl=removehyun(word)
ufcl=clean(fcl)
print(ufcl)
#fr=nltk.FreqDist(cl)

    

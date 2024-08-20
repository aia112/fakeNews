import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pd

df=pd.read_csv("C:/users/ansar/Desktop/Fakenews/fakeNews/dataset.csv")

word=word_tokenize(df['Text'][400],language='english')
data_clean=[]
stop=stopwords.words('english')
for i in word:
    if not i.lower() in stop:
      data_clean.append(i)  

data_clean1=[]
for i in data_clean:
    if re.match('[\w+]' ,i):
        data_clean1.append(i)
    else:
        continue
        
## Gives List of words free from stopwords and punctuation ##
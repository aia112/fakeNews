# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 20:04:57 2020

@author: Rony
"""

from bs4 import BeautifulSoup
import urllib3
import re
import feedparser
from newspaper import Article
import certifi
import csv


manager = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where()) ##Manages no. of requests .PoolManager(no.)##

url = 'https://indianexpress.com/syndication/'  ##rss feed ka url##
response = manager.request('GET', url)
soupparser = BeautifulSoup(response.data) ##Parsing html,xml using bs4##
li=[]
for link in soupparser.findAll('a',attrs={'href':re.compile("http:.*feed/$")}):  ## DNA,FOX ka blogspot wala## #Indian Express#
    li.append(link.get('href'))
for link in soupparser.findAll('a',attrs={'href':re.compile("http:.*rss$")}):  ## CNN ##
    li.append(link.get('href'))
for link in soupparser.findAll('a',attrs={'href':re.compile("^https://.*rssfeeds.*cms$")}):  ## Economic Times ##
    li.append(link.get('href'))
for link in soupparser.findAll('a',attrs={'href':re.compile("^[/].*rssfeeds.*cms$")}):  ## Economic Times ##
    li.append("https://economictimes.indiatimes.com" + link.get('href'))
for link in soupparser.findAll('a',attrs={'href':re.compile("https://rss.*xml$")}):  ## BBC,New York Times ##
    li.append(link.get('href'))
for link in soupparser.findAll('a',attrs={'href':re.compile("^https://feeds.feedburner.com/")}):  ## NDTV ##
    li.append(link.get('href'))
for link in soupparser.findAll('a',attrs={'href':re.compile("http://feeds.*$")}):  ##Washington post##
    li.append(link.get('href'))
for link in soupparser.findAll('a',attrs={'href':re.compile("^https://www.thehindu.com..*rss$")}):  ##The Hindu##
    li.append(link.get('href'))
for link in soupparser.findAll('a',attrs={'href':re.compile(".*feeds.a.dj.com/rss.*xml$")}):  ## Wallstreet Journal ##
    li.append(link.get('href'))
for link in soupparser.findAll('a',attrs={'href':re.compile("^https://.*rss$")}):  ## Business Standard ##
    li.append(link.get('href'))
for link in soupparser.findAll('a',attrs={'href':re.compile(".*rss$")}):  ## Business Standard ##
    li.append("https://www.business-standard.com" + link.get('href'))

print(soupparser)
for i in range(len(li)):
    if (re.match('.*subscription.*',li[i])):
        del li[i]
    if (re.match('.*subscribe.*',li[i])):
        del li[i]



print(li)
l1=[]    

k=int(input("Enter range beginning:"))
l=int(input("Enter range end:"))

for i in range(k,l):
   feed = feedparser.parse(li[i])
   for post in feed.entries:
     print("post title: " + post.title)
     print("post link: " + post.link)
     l1.append(post.link) ## CNN ke liye ye part ko comment rehne de,sirf ye ek line ##
     ## Baaki sab ke liye sirf upar wala line lagega,to neeche wala part comment mei rakh baaki ke liye ##
    
    ## abhi dono comment mei hai jab jo lagega use kar; baaki comment mei rehne de##
    
     ## CNN ke liye neeche wala ye part hai##
    ## if (re.match('^https://.*.cnn.com.*cnn$',post.link)):
      ## l1.append(post.link)
     ##if (re.match('^https://.*.cnn.com.*html$',post.link)):  
      ## l1.append(post.link) 
     ##if (re.match('^http://.*.cnn.com.*cnn$',post.link)):
      ## l1.append(post.link)
     ##if (re.match('^http://.*.cnn.com.*html$',post.link)):  
     ## l1.append(post.link)'''

print(l1) 


for i in range(len(l1)):
 f=Article(l1[i])
 f.download()
 f.parse()
 f.nlp()
 print(f.authors)
 ##print(f.summary)
 ##print(f.keywords)
 
 with open('dataset4.csv','w') as new_file:##a to append
     csv_writer = csv.writer(new_file,lineterminator='\n')
     ##csv_writer.writerow(['Authors','Text','URL','label'])##first uncomment this
     for i in range(len(l1)):
       f=Article(l1[i])
       f.download()
       f.parse()
       f.nlp()
       csv_writer.writerow([f.authors,f.text,l1[i]])
     
     
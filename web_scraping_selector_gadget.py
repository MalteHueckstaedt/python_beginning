#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 18:31:53 2022

@author: malte
"""
#https://medium.com/@devkosal/scraping-data-with-beautifulsoup-and-selectorgadget-in-python-3-decf798e1a1e
#pip install bs4
#pip install requests


from bs4 import BeautifulSoup
import requests
import pandas as pd


url = "https://www.imdb.com/search/title?genres=drama&groups=top_250&sort=user_rating,desc"
res = requests.get(url)
soup = BeautifulSoup(res.text)
soup

movies = soup.select(".lister-item-header a")
print(movies)

movies_titles = [title.text for title in movies]
movies_links = ["http://imdb.com"+title["href"] for title in movies]
print(movies_titles)
print(movies_links)
type(movies_titles) # Type=Liste
df = {'Title':movies_titles,'URL':movies_links} # Erzeugt aus zwei Listen eine Dictonary
type(df) #ist ein Dictonary
df = pd.DataFrame(df) #wandelt Dictonary in einen Pandas-DataFrame um
df
type(df)

df[df["Title"].str.contains("Herr")] #Filtere Zeilen mit dem String "Herr"

######################################
######################################
######################################
#scrape monpol ###################
######################################
######################################
######################################

#load url
url = "https://www.monopol-magazin.de/ressort/kunstmarkt"
res = requests.get(url)
res

#generate BeautifulSoup
soup = BeautifulSoup(res.text)
soup

# select all header objects
articles = soup.select("#block-kf-bootstrap-content header")
print(articles)

#get titles
articles_titles = [article__title.text for article__title in articles]
print(articles_titles)
type(articles_titles)

#get urls
 articles_urls = []
 for article__title in soup.find_all(attrs={'class':'article__title'}):
     for link in article__title.find_all('a'):
         url = "https://www.monopol-magazin.de"+link.get('href')
         articles_urls.append(url)
print(articles_urls)
type(articles_urls)

print(len(articles_titles))
print(len(articles_urls))

#join list to dataframe
print(monopol)
pd.DataFrame(articles_titles,articles_urls)

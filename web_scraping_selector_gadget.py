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
df = {'Month':movies_titles,'Day':movies_links} # Erzeugt aus zwei Listen eine Dictonary
type(df) #ist ein Dictonary
df = pd.DataFrame(df) #wandelt Dictonary in einen Pandas-DataFrame um
type(df)

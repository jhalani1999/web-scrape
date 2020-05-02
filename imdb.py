from bs4 import BeautifulSoup
import requests
import pandas as pd

#source = requests.get("https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250").text
#soup = BeautifulSoup(source, 'lxml')
#movies = []
#years = []
#ratings = []
#
#source_lister = soup.find('div', class_='lister')
#for movie in source_lister.tbody.find_all('td', class_='titleColumn'):
#    movies.append(movie.a.text)
#    years.append(movie.span.text)
#
#for rating in source_lister.tbody.find_all('td', class_='ratingColumn imdbRating'):
#    ratings.append(rating.strong.text)
#    
#df = pd.DataFrame({'Movie Title':movies, "Year":years, "Rating":ratings}) 
#
#df = df.replace(to_replace ='[()]', value = '', regex = True) 

source_rotten = requests.get("https://www.rottentomatoes.com/top/bestofrt/").text
soup = BeautifulSoup(source_rotten, 'lxml')
movies = []
years = []
ratings = []

soup.find('table', class_='table').find('span',class_="tMeterScore").text
soup.find('table', class_='table').find('a',class_='unstyled articleLink').text
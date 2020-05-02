from bs4 import BeautifulSoup
import requests
import pandas as pd

source = requests.get('http://www.ets.org/gre/revised_general/prepare/analytical_writing/issue/pool').text
soup = BeautifulSoup(source, 'lxml')
content= []

for article in soup.find_all('div', class_='indented'):
    content.append(article.p.text)

df = pd.DataFrame({'Content':content}) 

df.to_csv('issue.csv')
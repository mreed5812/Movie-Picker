import requests
import pandas
from bs4 import BeautifulSoup

#URL = 'https://www.monster.com/jobs/search/?q=Programmer&where=New-York'
URL = 'https://www.netflix.com/browse/genre/34399'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
#results = soup.find(id='row-5')

movie_rows = soup.findAll('span', {"class": "nm-collections-title-name"})

movie_list = []

for row in movie_rows:
    movie_list.append(row.text)
    print(row.text)

pd = pandas.DataFrame(movie_list)
pd.to_csv("movies.csv")

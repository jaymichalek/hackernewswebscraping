import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(res.text, 'html.parser')
# Grabs the links for the story title:
links = soup.select('.titlelink')
# Grabs all the votes for stories:
votes = soup.select('.score')
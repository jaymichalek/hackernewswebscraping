import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/')
# Grabs page 2 of hacker news:
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
# Grabs the links for the story title:
links = soup.select('.titlelink')
links2 = soup2.select('.titlelink')
# Grabs all the votes for stories:
subtext = soup.select('.subtext')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2


# Function sorts the hashmap from create_custom_hn fn to a list in reverse order
# by number of votes.
def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


# This function grabs the title, link and number of votes from hackernews web articles site with votes
# that are greater than 99 votes only.
def create_custom_hn(link, text):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


# Used pprint to print output neatly on console.
pprint.pprint(create_custom_hn(mega_links, mega_subtext))

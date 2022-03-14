import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(res.text, 'html.parser')
# Grabs the links for the story title:
links = soup.select('.titlelink')
# Grabs all the votes for stories:
subtext = soup.select('.subtext')


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
pprint.pprint(create_custom_hn(links, subtext))

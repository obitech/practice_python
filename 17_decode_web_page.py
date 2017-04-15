import re
import requests
import datetime
from bs4 import BeautifulSoup as bs

# Loading HTML into variable
r = requests.get('https://nytimes.com')
r_html = r.text

# Initializing BeautifulSoup
soup = bs(r_html, 'html.parser')

titles = []

# Getting all strings which are in a <h><a> tag with class '*story*'
# This will also get some other titles since they have a story class as well
for x in soup.find_all(re.compile('h'), class_ = re.compile('story')):
    titles.append(str(x.find_next('a').string).strip())

# Removing duplicates
titles = [x for x in set(titles)]

print("All the titles of the NYTimes Homepage from " + datetime.datetime.now().strftime("%d.%m.%y %H:%M"))

for string in titles:
    print(string)
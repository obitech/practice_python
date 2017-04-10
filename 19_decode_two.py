import re
from bs4 import BeautifulSoup
import requests

r = requests.get("http://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture")
r_html = r.text

soup = BeautifulSoup(r_html, "html.parser")

# Saves article in dictionary, with actual text in list
article = {'text': []}

article['title'] = str(soup.find("title").string)
article['author'] = str(soup.find("a", class_ = re.compile("author")).string)

for x in soup.find_all("p"):
    if x.string != None:
        article['text'].append(x.string)

# Uncomment this to have a long string for the article
# article_string = ''.joint(article['text'])

# Uncomment this to remove copyright stuff at end of article
# article['text'] = article['text'][:-4]
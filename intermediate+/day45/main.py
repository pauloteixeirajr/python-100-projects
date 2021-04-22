import requests
from bs4 import BeautifulSoup

# Scraping A live website
response = requests.get("https://news.ycombinator.com/news")
markup = response.text

soup = BeautifulSoup(markup, "html.parser")
articles = soup.select(".storylink")
upvotes = soup.select(".score")
article_texts = []
article_links = []

for article in articles:
    article_texts.append(article.getText())
    article_links.append(article.get("href"))

article_upvotes = [int(score.getText().split(" ")[0]) for score in upvotes]

print(article_texts)
print(article_links)
print(article_upvotes)

# Reading local files
with open('website.html') as html:
    markup = html.read()

soup = BeautifulSoup(markup, 'html.parser')
print(soup.title)
# print(soup.body)

all_anchors = soup.find_all(name="a")
for tag in all_anchors:
    # Get inner text
    print(tag.getText())
    # Get attributes
    print(tag.get("href"))

# Finding by ID
heading = soup.find(name="h1", id="name")
# heading = soup.select_one("#name")
print(heading.getText())

# Finding by class
section = soup.find(name="h3", class_="heading")
# section = soup.select(".heading")
print(section.getText())

# Finding nested children
first_anchor = soup.select_one("p a")
print(first_anchor.get("href"))

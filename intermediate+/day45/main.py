from bs4 import BeautifulSoup

with open('website.html') as html:
    markup = html.read()

soup = BeautifulSoup(markup, 'html.parser')
print(soup.title)
# print(soup.body)

print(soup.a)

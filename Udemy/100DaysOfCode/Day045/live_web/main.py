import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://news.ycombinator.com/")
yc_website = response.text

soup = BeautifulSoup(yc_website, "html.parser")
articles = soup.select("td.title > span.titleline > a")
article_texts = []
article_links = []
for article_tag in articles:
    article_text = article_tag.getText()
    article_link = article_tag.get('href')
    article_texts.append(article_text)
    article_links.append(article_link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.select("td.subtext > span.subline > span.score")]

print(len(article_texts))
print(len(article_links))
print(len(article_upvotes))
print(article_upvotes)

max_index = article_upvotes.index(max(article_upvotes))
print(max_index, article_texts[max_index], article_links[max_index], article_upvotes[max_index])

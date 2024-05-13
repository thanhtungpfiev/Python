import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)
contents = BeautifulSoup(response.text, "html.parser")
films = [film.getText() for film in contents.find_all("h3", class_="title")][::-1]
with open("movies.txt", "w") as fp:
    fp.write("\n".join(films))

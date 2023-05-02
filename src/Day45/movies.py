import requests
from bs4 import BeautifulSoup
import os.path

DIR = os.path.dirname(__file__)

response = requests.get(
    "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
website = response.text
soup = BeautifulSoup(website, 'html.parser')

titles_raw = soup.select("h3.title")
titles = [t.getText() for t in titles_raw]
titles.reverse()

print(titles)

with open(os.path.join(DIR, "movies_list.txt"), 'w', encoding='UTF-8') as file:
    for title in titles:
        file.write(title + '\n')


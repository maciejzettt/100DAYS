import requests
from bs4 import BeautifulSoup
import print_dict

response = requests.get("https://news.ycombinator.com/")
website = response.text

soup = BeautifulSoup(website, 'html.parser')

story_list_raw = soup.select("span.titleline")
story_list = [{'title': tag.a.get_text(), 'href': tag.a.get('href')}
              for tag in story_list_raw]
print_dict.print_dict(story_list)
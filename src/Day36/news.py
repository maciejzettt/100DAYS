import requests
import html

NEWSAPI_ENDPOINT = "https://newsapi.org/v2/top-headlines"

class NewsAPIHeadlines:
    def __init__(self, api_key) -> None:
        news_params = {
            "apiKey": api_key,
            "q": "Tesla",
            "country": "us",
            "category": "business"
        }
        news_resp_raw = requests.get(NEWSAPI_ENDPOINT, news_params)
        news_resp_raw.raise_for_status()
        news_resp = news_resp_raw.json()
        self.articles_num = news_resp.get("totalResults")
        
        if int(self.articles_num) > 0:
            self.news_list = news_resp.get("articles")
        else:
            self.news_list = ["No news found today."]
        
        self.current_article = 0

    def has_news(self) -> bool:
        return self.articles_num > self.current_article
    
    def get_next_headline(self) -> dict:
        if self.has_news():
            article = self.news_list[self.current_article]
            article['author'] = "Not provided" if article['author'] is None else html.unescape(article['author'])
            article['title'] = "Not provided" if article['title'] is None else html.unescape(article['title'])
            article['description'] = "Not provided" if article['description'] is None else html.unescape(article['description'])
            self.current_article += 1
            return article
        else:
            return None


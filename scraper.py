from newspaper import Article
import requests


def scrape(url):
    
    article = Article(url)
    article.download()
    article.parse()

    title = article.title
    text = article.text

    return title, text

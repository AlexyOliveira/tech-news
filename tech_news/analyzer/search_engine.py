from tech_news.database import db
import re


# Requisito 7
def search_by_title(title):
    news = []
    regex_title = re.compile(title, re.IGNORECASE)
    db_news = db.news.find(
        {"title": regex_title}, {"_id": False, "title": True, "url": True}
    )
    for new in db_news:
        news.append((new["title"], new["url"]))
    return news


# print(search_by_title("notícia bacana"))


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError

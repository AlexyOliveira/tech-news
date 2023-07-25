from tech_news.database import db
from datetime import datetime
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
    try:
        news = []

        date_object = datetime.strptime(date, "%Y-%m-%d")

        dd_mm_yyyy_format_date = date_object.strftime("%d/%m/%Y")

        db_news = db.news.find(
            {"timestamp": dd_mm_yyyy_format_date},
            {"_id": False, "title": True, "url": True},
        )

        for new in db_news:
            news.append((new["title"], new["url"]))
        return news

    except ValueError:
        raise ValueError("Data inválida")


# print(search_by_date("2021"))


# Requisito 9
def search_by_category(category):
    news = []
    category_title = re.compile(category, re.IGNORECASE)
    db_news = db.news.find(
        {"category": category_title},
        {"_id": False, "title": True, "url": True},
    )
    for new in db_news:
        news.append((new["title"], new["url"]))
    return news


# print(search_by_date("tecnologia"))

from tech_news.database import create_news
from parsel import Selector
import requests
import time


# Requisito 1
def fetch(url):
    headers = {"user-agent": "Fake user-agent"}
    try:
        time.sleep(1)
        page = requests.get(url, headers=headers, timeout=3)
        if page.status_code != 200:
            return None
        else:
            return page.text
    except requests.Timeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    get_links = selector.css(".entry-title a::attr(href)").getall()
    return get_links


# html = fetch("https://blog.betrybe.com/")
# print(scrape_updates(html))


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    get_link = selector.css(".next::attr(href)").get()
    return get_link


# print(scrape_next_page_link(fetch("https://blog.betrybe.com/page/80/")))


# Requisito 4
def scrape_news(html_content):
    selector = Selector(text=html_content)
    get_url = selector.css('link[rel="canonical"]::attr(href)').get()
    get_title = selector.css(".entry-title::text").get().strip("\xa0")
    get_date = selector.css(".meta-date::text").get()
    get_writer = selector.css(".author a::text").get()
    get_reading_time = (
        selector.css(".meta-reading-time::text").get().split()[0]
    )
    get_summary = selector.css(
        ".entry-content > p:first-of-type *::text"
    ).getall()
    get_category = selector.css(".label::text").get()
    return {
        "url": get_url,
        "title": get_title,
        "timestamp": get_date,
        "writer": get_writer,
        "reading_time": int(get_reading_time),
        "summary": "".join(get_summary).strip(),
        "category": get_category,
    }


# print(scrape_news("https://blog.betrybe.com/carreira/glossario-de-tecnologia/"))


# Requisito 5
def get_tech_news(amount):
    url = "https://blog.betrybe.com/"
    news = list()
    while len(news) < amount:
        html_content = fetch(url)
        links_list = scrape_updates(html_content)
        news.extend(links_list)
        url = scrape_next_page_link(html_content)

    news = [scrape_news(fetch(item)) for item in news[:amount]]
    create_news(news)

    return news

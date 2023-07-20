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
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError

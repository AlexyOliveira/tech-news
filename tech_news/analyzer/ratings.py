from tech_news.database import find_news
from collections import Counter


def top_5_categories():
    news = find_news()
    category_counts = Counter(item["category"] for item in news)
    top_categories = sorted(
        category_counts.items(), key=lambda x: (-x[1], x[0])
    )
    return [category for category, _ in top_categories[:5]]

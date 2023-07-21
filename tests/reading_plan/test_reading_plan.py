from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501
import pytest


def test_reading_plan_group_news():
    r = ReadingPlanService()
    a = r.group_news_for_available_time(1)
    with pytest.raises(ValueError):
        r.group_news_for_available_time(0)
    assert a["unreadable"] == [("Notícia bacana", 4)]
    assert a["readable"] == [
        {"unfilled_time": 0, "chosen_news": [("Notícia bacana 2", 1)]}
    ]

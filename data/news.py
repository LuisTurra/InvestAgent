import feedparser

def get_news(ticker):

    feed = feedparser.parse(
        f"https://news.google.com/rss/search?q={ticker}+stock"
    )

    news = []

    for item in feed.entries[:20]:

        news.append({
            "title": item.title
        })

    return news
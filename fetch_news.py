import os
import requests

API_KEY = os.getenv("NEWS_API_KEY")  # Set secret in Streamlit Cloud

def fetch_news(q="technology", page_size=20):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": q,
        "pageSize": page_size,
        "language": "en",
        "sortBy": "publishedAt",
        "apiKey": API_KEY
    }
    r = requests.get(url, params=params)
    data = r.json()
    return data.get("articles", [])

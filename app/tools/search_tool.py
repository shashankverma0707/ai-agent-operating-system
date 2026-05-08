import requests
from bs4 import BeautifulSoup


def search_web(url: str):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "lxml")

    return soup.get_text()[:5000]
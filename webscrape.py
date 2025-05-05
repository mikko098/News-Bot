from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse
import test


def get_first_n_articles(url, n):
    result = requests.get(url)
    doc = BeautifulSoup(result.text, features="xml")
    a = doc.find_all("item")
    article_list = []
    count = 1
    for item in a:
        if count <= n:
            article_url = item.find("link").text
            article_title = clean_title(item.find("title").text)
            new_url = test.get_article_url(article_url)
            article_list.append((article_title, new_url))
            count += 1
        else:
            break
    return article_list

def get_all_paragraphs(url):
    try:
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")
        paragraphs = doc.find_all("p")
        string = ""
        for i in paragraphs:
            string = f"{string} {i.text}"
    except:
        return string
    return string


def search_word(word, country):
    url = "https://news.google.com"
    search_word = "search?q=" + word +"&ceid=" + country + ":en"
    parsed_url = urlparse(url)
    base_url = (f"{parsed_url.scheme}://{parsed_url.netloc}/rss/{search_word}")
    return base_url

def clean_title(title):
    return title[:title.find("-")]

if __name__ == "__main__":
    word = input("enter word to search :")
    url = search_word(word, "MY")
    new_urls = get_first_n_articles(url, 3)[0]
    # for i, j in new_urls:
    i, j = new_urls
    print(j)
    print(get_all_paragraphs(j))
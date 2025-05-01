from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse, urljoin
import base64

def get_first_n_articles(url, n):
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    a = doc.find_all("article")
    article_list = []
    parsed_url = urlparse(url)

    for i in a:
        x = i.find("a")
        article_url = (f"{parsed_url.scheme}://{parsed_url.netloc}{x["href"].lstrip('.')}")
        article_list.append(article_url)
    return article_list[0 : min(len(article_list), n)]

def search_word(word):
    url = "https://news.google.com"
    search_word = "search?q=" + word
    parsed_url = urlparse(url)
    base_url = (f"{parsed_url.scheme}://{parsed_url.netloc}/{search_word}")
    return base_url

if __name__ == "__main__":
    word = input("enter word to search :")
    url = search_word(word)
    new_url = get_first_n_articles(url, 1)[0]
    final = requests.get(new_url, allow_redirects=True)
    soup = BeautifulSoup(final.text, "html.parser")
    
    print(new_url)
    with open("file.txt", "w") as file:
        for i in soup.prettify().split("\n"):
            try:
                file.write(i)
            except:
                continue


    parsed_new_url = urlparse(new_url)
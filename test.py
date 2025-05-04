import requests
import json
from bs4 import BeautifulSoup

# Credit to GTK from https://stackoverflow.com/questions/79388897/how-to-scrape-google-rssfeed-links

def get_article_url(google_rss_url):
    resp = requests.get(google_rss_url)
    data = BeautifulSoup(resp.text, 'html.parser').select_one('c-wiz[data-p]').get('data-p')
    obj = json.loads(data.replace('%.@.', '["garturlreq",'))

    payload = {
        'f.req': json.dumps([[['Fbv4je', json.dumps(obj[:-6] + obj[-2:]), 'null', 'generic']]])
    }

    headers = {
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
    }

    url = "https://news.google.com/_/DotsSplashUi/data/batchexecute"
    response = requests.post(url, headers=headers, data=payload)
    array_string = json.loads(response.text.replace(")]}'", ""))[0][2]
    article_url = json.loads(array_string)[1]

    return article_url
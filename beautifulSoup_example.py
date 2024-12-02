import requests
from bs4 import BeautifulSoup

url = 'https://sports.news.naver.com/wfootball/index'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    div = soup.select_one('div.good_news')
    articles = div.select('ol > li > a')
    for article in articles:
        title = article.get_text() 
        link = article.get('href')
        print(f'Title: {title}\nLink: {link}\n')
else:
    print(f'요청 실패: {response.status_code}')
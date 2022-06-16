import requests
from bs4 import BeautifulSoup

APPLE_DAILY_HEADLINE = 'http://www.appledaily.com.tw/appledaily/hotdaily/headline'
LTN_NEWS = 'https://news.ltn.com.tw/list/breakingnews'

def main():
    print('頻果今日焦點')
    resp = requests.get(APPLE_DAILY_HEADLINE).text
    soup = BeautifulSoup(resp, 'html5lib')
    for headline in soup.find('ul', 'all').find_all('li'):
        print(
            headline.find('div', 'aht_title_num').text,
            headline.find('div', 'aht_title').text,
            #headline.find('div', 'aht_title_pv').text
        )
    print('---------')
    print('自由今日焦點')
    resp = requests.get(LTN_NEWS).text
    soup = BeautifulSoup(resp, 'html5lib')
    for lte_news in soup.find(class_='list').find_all('li'):
        print(lte_news.find('p').text)


if __name__ == '__main__':
    main()

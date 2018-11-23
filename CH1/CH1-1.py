# -*- encoding: utf8-*-
import requests
from bs4 import BeautifulSoup

def main():

    res = requests.get('https://ccsys2.niu.edu.tw/Webcrawler/ch1-1.html')
    res.encoding='utf8'
    #判斷Status 是否正常瀏覽網頁
    if res.status_code!=200:
        print('Invalid URL：',res.url)
        return None

    soup = BeautifulSoup(res.text,'html.parser')
    #取得第一個h1
    print(soup.find('h1'))
    #取得第一個h2
    print(soup.find('h2'))

    #取得所有h3
    All_h3 =  soup.find_all('h3')
    for ah3 in All_h3:
        print(ah3.a.text)


if __name__ == '__main__':
    main()
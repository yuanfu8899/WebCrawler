import requests
from bs4 import BeautifulSoup

def main():
    res = requests.get('https://ccsys2.niu.edu.tw/Webcrawler/ch1-2.html')
    res.encoding='utf8'
    #判斷Status 是否正常瀏覽網頁
    if res.status_code!=200:
        print('Invalid URL：',res.url)
        return None
    soup = BeautifulSoup(res.text,'html.parser')
    print(res.encoding)
    print('編號|名稱|屬性|圖片網址')
    # 取得 編號 名稱 屬性 圖片網址
    rows = soup.find('table', 'table').tbody.find_all('tr')
    for row in rows:
        all_tds = row.find_all('td')
        print(all_tds[0].text,all_tds[1].text,all_tds[3].text,all_tds[2].img.get('src'))

if __name__ == '__main__':
    main()

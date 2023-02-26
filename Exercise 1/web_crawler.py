import requests
import lxml
from bs4 import BeautifulSoup
from xlwt import *
workbook = Workbook(encoding='utf-8')
table = workbook.add_sheet('data')
table.write(0, 0, 'URL')
table.write(0, 1, 'Title')
table.write(0, 2, 'Content')
line = 1
url = "https://news.ifeng.com/c/89TNORdIths"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}
f = requests.get(url, headers=headers)
soup = BeautifulSoup(f.content, 'lxml')
title = soup.find('h1', {'class': 'topic-2Eq5D0Zm'}).string.strip()
content_p = soup.find('div',{'class': 'main_content-28C-Fj2p'}).find_all('p')
content=''
for i in content_p:
    content += i.string.strip("</p>")
table.write(line, 0, url)
table.write(line, 1, title)
table.write(line, 2, content)
line += 1
workbook.save('web_crawler_res.xls')

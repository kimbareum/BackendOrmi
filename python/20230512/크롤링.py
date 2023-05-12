"""
advanced 과제 : 제주코딩베이스캠프 연구원에 2019.09.24일 부터 2019.10.23일까지 거래된 거래총량을 구해주세요.

https://paullab.co.kr/stock.html
"""

import requests
from bs4 import BeautifulSoup

response = requests.get("http://www.paullab.co.kr/stock.html")

response.encoding = "utf-8"
html = response.text

soup = BeautifulSoup(html, "html.parser")

총액정보 = soup.select("table.table-hover")
제코베연구원_일일거래량 = 총액정보[0].select('tr > td.num:nth-child(7)')

total = 0
for i in 제코베연구원_일일거래량 :
    total += int(i.text.replace(',',''))

print(total)

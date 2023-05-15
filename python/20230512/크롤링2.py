import requests
from bs4 import BeautifulSoup
from datetime import datetime


class Stock:
    def __init__(self, 날짜, 종가, 전일비, 시가, 고가, 저가, 거래량):
        self.날짜 = 날짜
        self.종가 = 종가
        self.전일비 = 전일비
        self.시가 = 시가
        self.고가 = 고가
        self.저가 = 저가
        self.거래량 = 거래량


def str_to_datetime(s, char):
    return datetime.strptime(s.replace(char, ""), "%Y%m%d")


def get_parsing_data(url):
    response = requests.get(url)
    response.encoding = "utf-8"
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    return soup


def get_select_data(soupdata, location):
    return list(
        map(lambda x: x.text.strip().replace(",", ""), soupdata.select(location))
    )


def create_instance(dataset, selectdata):
    dataset.append(Stock(*selectdata))


soupdata = get_parsing_data("http://www.paullab.co.kr/stock.html")
name = "제주코딩베이스캠프연구원"
제코베연구원 = get_select_data(soupdata, f"body > .main > #{name} ~ table td")

제코베연구원_일일 = []
for i in range(0, len(제코베연구원), 7):
    제코베연구원_일일.append(제코베연구원[i : i + 7])

dataset = []
for i in 제코베연구원_일일:
    create_instance(dataset, i)

start_date = datetime.strptime("20190924", "%Y%m%d")
end_date = datetime.strptime("20191023", "%Y%m%d")

총액 = []
for date, *data in 제코베연구원_일일:
    date = str_to_datetime(date, ".")
    if date >= start_date and date <= end_date:
        총액.append(int(data[-1]))
print(sum(총액))

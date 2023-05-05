import requests, config
from bs4 import BeautifulSoup

#url = "https://ru.investing.com/currencies/usd-rub"
#url = "https://ru.tradingview.com/symbols/USDRUB_TOM/?exchange=MOEX"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}

def chekConnect():
    padge = requests.get(config.urlRBC, headers=headers)
    print(padge)

def parse():
    padge = requests.get(config.urlRBC, headers=headers)
    soup = BeautifulSoup(padge.text, "html.parser")

    cost = soup.find('span', class_='chart__info__sum')
    cost_str = cost.get_text().lstrip('₽')
    print(cost_str)

    return cost_str


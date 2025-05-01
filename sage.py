from bs4 import BeautifulSoup
import requests
import time
import datetime

def get_price(ticker):
    try:
        time.sleep(10)
        url = f'https://finance.yahoo.com/quote/{ticker}/'
        # apparently these headers make me seem like a human lol
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text, 'html.parser')
        price_element = soup.find(attrs={"data-testid": "qsp-price"})

        if price_element:
            return float(price_element.text.replace(",","").strip())
        else:
            return "failed"
    except:
        time.sleep(30)
        url = f'https://finance.yahoo.com/quote/{ticker}/'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text, 'html.parser')
        price_element = soup.find(attrs={"data-testid": "qsp-price"})

        if price_element:
            return float(price_element.text.replace(",","").strip())
        else:
            return "failed"

def get_market_cap(ticker):
    try:
        time.sleep(10)
        url = f'https://finance.yahoo.com/quote/{ticker}/'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text, 'html.parser')
        price_element = soup.find(attrs={"data-field": "marketCap"})

        if not price_element:
            return "failed"

        T = 1000000000000
        B = 1000000000
        M = 1000000
        actual = price_element.text.replace(",","").strip()
        money = actual[-1]
        actual = float(actual[:-1])
        match(money):
            case "T":
                actual *= T
            case "B":
                actual *= B
            case "M":
                actual *= M
            case _:
                actual = price_element.text.replace(",","").strip()
        return float(actual)
    except:
        time.sleep(30)
        url = f'https://finance.yahoo.com/quote/{ticker}/'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text, 'html.parser')
        price_element = soup.find(attrs={"data-field": "marketCap"})

        if not price_element:
            return "failed"

        T = 1000000000000
        B = 1000000000
        M = 1000000
        actual = price_element.text.replace(",","").strip()
        money = actual[-1]
        actual = float(actual[:-1])
        match(money):
            case "T":
                actual *= T
            case "B":
                actual *= B
            case "M":
                actual *= M
            case _:
                actual = price_element.text.replace(",","").strip()
        return float(actual)

def get_market_open(ticker):
    try:
        time.sleep(10)
        url = f'https://finance.yahoo.com/quote/{ticker}/'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text, 'html.parser')
        opens = soup.find(attrs={"data-field": "regularMarketOpen"})

        if not opens:
            return "failed"

        opens = opens.text


        return float(opens.replace(",","").strip())
    except:
        time.sleep(30)
        url = f'https://finance.yahoo.com/quote/{ticker}/'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text, 'html.parser')
        opens = soup.find(attrs={"data-field": "regularMarketOpen"})

        if not opens:
            return "failed"

        opens = opens.text


        return float(opens.replace(",","").strip())

def get_time():
    now = datetime.datetime.now()
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    minutes_since_midnight = (now - midnight).seconds // 60
    return int(minutes_since_midnight)

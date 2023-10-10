# import modules
import yfinance as yf
import numpy as np
import pandas as pd
import requests
import os
import json
from bs4 import BeautifulSoup as bs
from matplotlib import pyplot as pyplot
from dotenv import load_dotenv

# retrive S&P 500 company tickers finalcial historycal data


def sp500Symbols():
    # env management
    load_dotenv()  # take environment variables from .env.
    url = os.getenv('S&P500list')

    # retrive S&P 500 company tickers
    rawPage = requests.get(url)
    soup = bs(rawPage.text, "html.parser")

    nameRows = soup.find_all("tr")
    for i in nameRows:
        nameRows += i.find_all("td")

    equityNames = list()
    for j in range(len(nameRows)):
        equityNames += [nameRows[j].text.split('\n')]

    equityNames.pop(0)

    companies = dict()
    for k in range(503):
        if len(equityNames[k]) >= 8:
            companies[equityNames[k][3]] = equityNames[k][1]
        else:
            pass
    with open("Name&Symbols.txt", "w") as f:
        json.dump(companies, fp=f, indent=4)
    return None


def getData(symbol=None, period=None, interval=None):
    # dowload hiastorical data
    tk = yf.Ticker(symbol)
    return tk.history(period=period, interval=interval)


sp500Symbols()

df3M = getData(symbol="MMM", period="2d", interval="1h")
df3M.to_csv("df3M")

tk = yf.Ticker('AAPL')


df = yf.download("AAPL")

print(df)
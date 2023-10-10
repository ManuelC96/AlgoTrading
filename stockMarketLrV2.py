# import modules
import yfinance as yf
import numpy as np
import pandas as pd
import requests
import os
import json
import datetime
from bs4 import BeautifulSoup as bs
from matplotlib import pyplot as plt
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


def getData(symbol=None, startDate=None, endDate=None):
    '''
    :paramer symbol: ticker
    :paramer startDate: str(YYYY-MM-DD)
    :paramer endDate: str(YYYY-MM-DD)

    '''
    # dowload hiastorical data
    df = yf.download(symbol, start=startDate, end=endDate)
    return df


sp500Symbols()
today = str(datetime.date.today())
print(today)
df = getData("AMZN", startDate="2023-01-01", endDate=today)

normDf = (df-df.min())/(df.max()-df.min())
normDf.reset_index(inplace=True)
print(normDf)

plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.plot(normDf["Date"], normDf["Close"], color="yellow", linewidth=.5)
ax.scatter(normDf["Date"], normDf["Close"], color="red", linewidth=.1)
plt.tight_layout()
plt.show()

# polynomial reg using Normal eq

exp = 3
# equation
def polynomialEq(X:list, Y:list, Deg: int):
    


polynomialEq()


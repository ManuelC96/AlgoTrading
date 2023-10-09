# import modules
import yfinance as yf
import numpy as np
import pandas as pd
import requests
import os
from bs4 import BeautifulSoup as bs
from matplotlib import pyplot as pyplot
from dotenv import load_dotenv

# env management
load_dotenv()  # take environment variables from .env.
url = os.getenv('S&P500list')


# retrive S&P 500 company tickers
rawPage = requests.get(url)
soup = bs(rawPage.text, "html.parser")

# OLD code
# simbolRows = soup.find_all(
#     "a", attrs={"rel": "nofollow", "class": "external text"})
# simbols = tuple()
# for i in range(len(simbolRows)):
#     if len(simbolRows[i].text.strip()) < 5:
#         simbols += (simbolRows[i].text.strip(),)
#     else:
#         pass

nameRows = soup.find_all("tr")
for i in nameRows:
    nameRows += i.find_all("td")

equityNames = list()
for j in range(len(nameRows)):
    equityNames += [nameRows[j].text.split('\n')]

equityNames.pop(0)

companies = dict()
for k in range(503):
    # print(f'{k} ', equityNames[k], '\n', len(equityNames[k]))
    if len(equityNames[k]) >= 8:
        companies[equityNames[k][3]] = equityNames[k][1]
    else:
        pass


# get historycal financial data
def getData(originalFunc):
    def wrapperFunc(*args, **kwargs):
        tk = yf.Ticker(originalFunc(*args, **kwargs))
        return tk.history(period="1d", interval="1h")
    return wrapperFunc


# retrive S&P 500 company tickers
@getData
def getSymbol(companyName: str):
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
    return companies[companyName]


df3M = getSymbol("3M")

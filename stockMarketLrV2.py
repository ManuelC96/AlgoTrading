# import modules
import yfinance as yf
import numpy as np
import pandas as pd
import requests
import os
import random as rnd
import json
import datetime
from bs4 import BeautifulSoup as bs
from matplotlib import pyplot as plt
from dotenv import load_dotenv
import icecream as ic
# retrive S&P 500 company tickers finalcial historycal data


# def sp500Symbols():
#     # env management
#     load_dotenv()  # take environment variables from .env.
#     url = os.getenv('S&P500list')

#     # retrive S&P 500 company tickers
#     rawPage = requests.get(url)
#     soup = bs(rawPage.text, "html.parser")

#     nameRows = soup.find_all("tr")
#     for i in nameRows:
#         nameRows += i.find_all("td")

#     equityNames = list()
#     for j in range(len(nameRows)):
#         equityNames += [nameRows[j].text.split('\n')]

#     equityNames.pop(0)

#     companies = dict()
#     for k in range(503):
#         if len(equityNames[k]) >= 8:
#             companies[equityNames[k][3]] = equityNames[k][1]
#         else:
#             pass
#     with open("Name&Symbols.txt", "w") as f:
#         json.dump(companies, fp=f, indent=4)
#     return None


# def getData(symbol=None, startDate=None, endDate=None):
#     '''
#     :paramer symbol: ticker
#     :paramer startDate: str(YYYY-MM-DD)
#     :paramer endDate: str(YYYY-MM-DD)

#     '''
#     # dowload hiastorical data
#     df = yf.download(symbol, start=startDate, end=endDate)
#     return df


# sp500Symbols()
# today = str(datetime.date.today())
# print(today)
# df = getData("AMZN", startDate="2023-01-01", endDate=today)

# normDf = (df-df.min())/(df.max()-df.min())
# normDf.reset_index(inplace=True)
# print(normDf)

# plt.style.use('dark_background')
# fig, ax = plt.subplots()
# ax.plot(normDf["Date"], normDf["Close"], color="yellow", linewidth=.5)
# ax.scatter(normDf["Date"], normDf["Close"], color="red", linewidth=.1)
# plt.tight_layout()
# plt.show()

# polynomial reg using Normal eq
rnd.seed = 1
exp = 3
high = 50
xVals = np.arange(1, high + 1)
# rnd.shuffle(xVals)
print(xVals)


def polynomialEq(X: list, Deg: int, Seed: int):
    Y = []
    rgn = np.random.default_rng(seed=Seed)
    # print(W)
    for i in range(len(X)):
        tempStack = []

        W = rgn.integers(low=1, high=5, size=Deg)
        for j in range(Deg):

            x = W[j]*X[i]**(j + 1)
            tempStack.append(x)

        # print(tempStack)
        y = np.sum(tempStack)
        Y.append(y)
    # print(Y)
    return Y


yVals = polynomialEq(X=xVals, Deg=3, Seed=1)
print(yVals)

fig, ax = plt.subplots(figsize=(10, 5))
ax.scatter(xVals, yVals)
ax.plot(xVals, yVals)
plt.show()

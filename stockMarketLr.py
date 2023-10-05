# import modules
import yfinance as yf
import numpy as np
import pandas as pd 
from matplotlib import pyplot as pyplot
import requests


# nasdaq api
link = "https://data.nasdaq.com/api/v3/datasets/"
apiKey = "?api_key=dxacqqyjomm6cyJhG_VZ"
endpoint = "MER/F1.xml"
finalUrl = link + endpoint + apiKey
print(finalUrl)
# retrive stock data
data = requests.get(url="https://data.nasdaq.com/api/v3/datatables/ETFG/FUND.csv?ticker=SPY&api_key=dxacqqyjomm6cyJhG_VZ")
print(data.content)
# data = yf.Ticker()
import yfinance as yf


def get_data(symbol="AAPL"):
    '''
    :param symbol: chose stock ticker

    '''
    # define the ticker symbol
    tickerSymbol = symbol

    # create a ticker obj
    ticker = yf.Ticker(tickerSymbol)

    # dowload hiastorical data
    return ticker.history(period='2d', interval='1d')

# dowloa Recent hist data


historicalData = get_data()


def testEngulfing(df):
    lastOpen = df.iloc[-1, :].Open
    lastClose = df.iloc[-1, :].Close
    previousOpen = df.iloc[-2, :].Open
    previousClose = df.iloc[-2, :].Close

    if (previousOpen < previousClose
            and lastOpen > previousClose
            and lastClose < previousOpen
        ):
        return 1  # bearish market
    elif (previousOpen > previousClose
          and lastOpen < previousClose
          and lastClose > previousOpen
          ):
        return 2  # bullish market
    else:
        return 0  # no engulfing pattern

# sent Live Signal

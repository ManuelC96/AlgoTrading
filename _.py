
from apscheduler.schedulers.blocking import BlockingScheduler
import smtplib
import ssl
from email.message import EmailMessage
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


em = EmailMessage()
username = str('facebehind@yahoo.com')
password = str('xxxxxxxxxxxxxxxxxxxx')

subject = 'info signal'


def someJob():
    msg = 'Trading signal message \n'
    historicalData = get_data()

    if testEngulfing(historicalData) == 1:
        msg = str('bearish')

    elif testEngulfing(historicalData) == 2:
        msg = str(bullish)

    em['From'] = username
    em['To'] = username
    em['Subject'] = subject
    em.set_content(msg)

    context = ssl.create_default_context()

    server = smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465, context=context)
    server.ehlo()
    server.login(username, password)
    server.sendmail(username, password, em.as_string())
    server.close()


someJob()

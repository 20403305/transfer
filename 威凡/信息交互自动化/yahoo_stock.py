import yfinance as yf

msft = yf.Ticker("AAPL")

# get stock info
a = msft.info
print(a)

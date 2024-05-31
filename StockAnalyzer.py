import pandas as pd
import yfinance as yf
import matplotlib as plt
#Simple Linear Regression Model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


# Return a given ticker's data, reformatting the data
def get_stock_data(ticker_symbol):
    ticker = yf.Ticker(ticker_symbol)
    historical_data = ticker.history(period='1mo', interval='1d')
    
    #Drop the "dividends" and "stock splits" columns
    top_entry = historical_data.iloc[0]
    dividend_col = 'Dividends'
    stock_splits_col = 'Stock Splits'
    if dividend_col and stock_splits_col in top_entry.index:
        historical_data = historical_data.drop(columns=[dividend_col, stock_splits_col])
    historical_data = historical_data.drop(historical_data.index[1]) #Delete the 2nd row
    return historical_data
 

#current_ticker = input("Ticker Symbol: ")
current_ticker = 'GOOGL'
curr_ticker_data = get_stock_data(current_ticker)

print(curr_ticker_data)

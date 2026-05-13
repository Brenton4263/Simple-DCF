import yfinance as yf
import pandas as pd
import numpy as np

# donwload income statement, balance sheet, cash flow statement and return as data frame

def financial_data(ticker):
    stock = yf.Ticker(ticker)
    bal_sheet = stock.balance_sheet
    inc_stmt = stock.financials
    cf_stmt = stock.cash_flow

    inputs = {
        'Revenue':inc_stmt.loc["Total Revenue"].iloc[0], 
        'EBIT': inc_stmt.loc['EBIT'].iloc[0], 
        'FCF': cf_stmt.loc['Free Cash Flow'].iloc[0], 
        'Debt': bal_sheet.loc['Total Debt'].iloc[0], 
        'Cash': bal_sheet.loc['Cash And Cash Equivalents'].iloc[0],
        'Shares': stock.info.get('sharesOutstanding')}
    return inputs

data = financial_data('MSFT')


def forecast_fcf(current_fcf, growth_rate, years):
    forecast_values = []
    for year in range(1, years+1):
        result = current_fcf * (1 + growth_rate) ** year
        forecast_values.append(result)
    return forecast_values

FCF_forecast = forecast_fcf(100,0.1,3)

def Discount_fcfs(fcfs, WACC):
    discounted_values = []
    for year, fcf in enumerate(fcfs, start=1):
        pv = fcf / (1+WACC) ** year
        discounted_values.append(pv)
    return discounted_values
print(Discount_fcfs(FCF_forecast, 0.1))

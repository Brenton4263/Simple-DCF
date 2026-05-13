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
years = 5
growth_rate = 0.02

#forecasted FCF
forecast_fcfs = []
for year in range(1, years+1):
    result = data['FCF'] * (1 + growth_rate) ** year
    forecast_fcfs.append(result)
 
# Discount FCF 
discounted_fcfs = []
for year, fcf in enumerate(forecast_fcfs, start=1):
    pv = fcf / (1+WACC) ** year
    discounted_fcfs.append(pv)

# PV of cash flows
sum(discounted_fcfs)

#Terminal Value calculation
tv = forecast_fcfs[-1] * (1 + growth_rate) / (wacc - growth_rate)

#Discount terminal value
pv_tv = tv / (1 + wacc) ** years

#Calculate enterprise value, equity value, share price
enterprise_value = sum(discounted_fcfs) + pv_tv


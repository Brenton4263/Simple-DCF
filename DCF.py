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
        'FCF ALL': cf_stmt.loc['Free Cash Flow'],
        'Debt': bal_sheet.loc['Total Debt'].iloc[0], 
        'Cash': bal_sheet.loc['Cash And Cash Equivalents'].iloc[0],
        'Shares': stock.info.get('sharesOutstanding'),
        'Stock Price': stock.info['regularMarketPrice']}
    return inputs

data = financial_data('MSFT')
#hardcoded values
years = 5
terminal_growth = 0.02
WACC = 0.05

#estimate free cash flow growth rate from previous data
valid_fcf = data['FCF ALL'].dropna()
periods = len(valid_fcf) - 1
start_fcf = valid_fcf.iloc[-1]
end_fcf = valid_fcf.iloc[0]
fcf_growth = (end_fcf / start_fcf) ** (1 / periods) - 1

    



#forecasted FCF
forecast_fcfs = []
for year in range(1, years+1):
    result = data['FCF'] * (1 + fcf_growth) ** year
    forecast_fcfs.append(result)
 
# Discount FCF 
discounted_fcfs = []
for year, fcf in enumerate(forecast_fcfs, start=1):
    pv = fcf / (1+WACC) ** year
    discounted_fcfs.append(pv)

# PV of cash flows
pv_fcf = sum(discounted_fcfs)

#Terminal Value calculation
tv = forecast_fcfs[-1] * (1 + terminal_growth) / (WACC - terminal_growth)

#Discount terminal value
pv_tv = tv / (1 + WACC) ** years

#Calculate enterprise value, equity value, share price
enterprise_value = pv_fcf + pv_tv
equity_value = enterprise_value - data['Debt'] + data['Cash']
Share_price = equity_value / data['Shares']
print(f"Current share price: {data['Stock Price']}")
print(f'Estimated price: {Share_price}')
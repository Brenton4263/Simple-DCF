# Automated DCF Valuation Engine

A Python project that performs a basic Discounted Cash Flow (DCF) valuation using financial data pulled from the `yfinance` API and estimates share prices.
## Features

- Pulls financial data automatically using `yfinance`
- Extracts key valuation inputs such as:
  - Revenue
  - EBIT
  - Free Cash Flow
  - Debt
  - Cash
  - Shares Outstanding
  - Current Stock Price
- Forecasts future free cash flows over a chosen time period
- Discounts projected cash flows back to present value
- Calculates terminal value
- Computes:
  - Enterprise Value
  - Equity Value
  - Estimated Share Price
- Compares estimated share price to current market price

## How It Works

The model follows a standard DCF process:

1. Pull historical company financial data from Yahoo Finance
2. Estimate or manually set free cash flow growth
3. Forecast future free cash flows
4. Discount projected free cash flows using WACC
5. Calculate terminal value using a perpetual growth formula
6. Add discounted cash flows and discounted terminal value to get Enterprise Value
7. Adjust for debt and cash to get Equity Value
8. Divide by shares outstanding to estimate intrinsic value per share

## Assumptions

This model depends heavily on the following assumptions as:

- Forecast period(hardcoded)
- Free Cash Flow growth rate(hardcoded)
- Terminal growth rate(hardcoded)
- WACC(hardcoded)

## Limitations

-Is extremely sensitive to inputted WACC values and terminal growth values
-Simplified DCF model so not that accurate

## Future Improvements

-Add error safetyguards
-Estimate WACC
-Add sensitivity analysis
- Support multiple ticker valuation
- Build a cleaner terminal/CLI output format

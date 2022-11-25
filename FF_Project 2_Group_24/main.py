import pandas as pd
df = pd.read_csv('sp.csv')
dividend_rate = dict()
dividend_rate['2018'] = 1.5
dividend_rate['2019'] = 1
dividend_rate['2020'] = 1
dividend_rate['2021'] = 2
dividend_rate['2022'] = 5
stock_prices = list(df['Close Price'])
months = list(df['Month'])
total_shares = 0
total_stock_value = 0
remainder = 0
for i in range(len(stock_prices)):
  investment = 10000 + remainder
  shares = investment//stock_prices[i]
  total_shares += shares
  total_stock_value += (shares*stock_prices[i])
  remainder = investment - (shares*stock_prices[i]) + total_shares*dividend_rate[months[i][-4:]]
print('Total Value of Investment till November, 2022: ', total_stock_value)
print('Total Number of Shares till November, 2022: ', total_shares)
print('Remainder Amount till November, 2022: ', remainder)
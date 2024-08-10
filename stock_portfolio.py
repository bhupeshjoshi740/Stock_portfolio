import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Define your portfolio
portfolio = {
    'AAPL': 10,  # Apple
    'GOOGL': 5,  # Alphabet (Google)
    'AMZN': 2    # Amazon
}

# Function to fetch stock data
def fetch_stock_data(tickers, start_date, end_date):
    stock_data = {}
    for ticker in tickers:
        stock_data[ticker] = yf.download(ticker, start=start_date, end=end_date)['Adj Close']
    return pd.DataFrame(stock_data)

# Function to calculate portfolio value
def calculate_portfolio_value(stock_data, portfolio):
    portfolio_values = stock_data.copy()
    for ticker in portfolio:
        portfolio_values[ticker] = portfolio_values[ticker] * portfolio[ticker]
    portfolio_values['Total'] = portfolio_values.sum(axis=1)
    return portfolio_values

# Function to plot portfolio value
def plot_portfolio_value(portfolio_values):
    plt.figure(figsize=(10, 6))
    plt.plot(portfolio_values.index, portfolio_values['Total'], label='Total Portfolio Value')
    plt.title('Stock Portfolio Value Over Time')
    plt.xlabel('Date')
    plt.ylabel('Portfolio Value (USD)')
    plt.legend()
    plt.show()

# Main script
start_date = '2023-01-01'
end_date = '2024-01-01'
tickers = list(portfolio.keys())
stock_data = fetch_stock_data(tickers, start_date, end_date)
portfolio_values = calculate_portfolio_value(stock_data, portfolio)
plot_portfolio_value(portfolio_values)

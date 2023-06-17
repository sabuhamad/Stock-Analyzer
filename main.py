import yahooquery as yf
import pandas as pd

def analyze_company(ticker_symbol):
    # Fetch the data
    company = yf.Ticker(ticker_symbol)

    # Get the balance sheet
    balance_sheet = company.balance_sheet()

    # Get the current stock price
    current_price = company.financial_data[ticker_symbol]['currentPrice']

    # Get the income statement
    income_statement = company.income_statement()
    income_statement = income_statement.dropna(subset=['DilutedEPS'])
    # Analyze the data
    earnings_per_share = income_statement['DilutedEPS'].iloc[-1]  # Use the most recent year's net income

    pe_ratio = current_price / earnings_per_share
    
    return pe_ratio

# Get user input
user_input = input("Enter the ticker symbols of the companies you want to analyze, separated by commas: ")

# Split the user input into a list of ticker symbols
ticker_symbols = user_input.split(',')

# Analyze each company
for ticker_symbol in ticker_symbols:
    pe_ratio = analyze_company(ticker_symbol.strip())
    print(f"The P/E ratio for {ticker_symbol.strip()} is {pe_ratio}")

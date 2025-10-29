import streamlit as st
import pandas as pd
import yfinance as yf

st.title("Portfolio Tracker")

st.sidebar.header("Portfolio Settings")
tickers_input = st.sidebar.text_input("Tickers (comma-separated)", "AAPL,MSFT,GOOGL,EURUSD=X")
quantities_input = st.sidebar.text_input("Quantities (comma-separated)", "10,5,2,1000")

tickers = [t.strip().upper() for t in tickers_input.split(",")]
quantities = [float(q.strip()) for q in quantities_input.split(",")]

portfolio = dict(zip(tickers, quantities))

portfolio_data = {}
for ticker, quantity in portfolio.items():
    stock = yf.Ticker(ticker)
    data = stock.history(period='1d')
    price = data['Close'].iloc[-1] if not data.empty else float('nan')
    portfolio_data[ticker] = {
        'quantity': quantity,
        'last_price': price,
        'value': price * quantity if not pd.isna(price) else float('nan')
    }

df = pd.DataFrame.from_dict(portfolio_data, orient='index')
df = df[['quantity', 'last_price', 'value']]
total_value = df['value'].sum()

st.subheader("Portfolio Overview")
st.dataframe(df.style.format({'last_price': '{:.2f}', 'value': '{:.2f}'}))
st.success(f"Total Portfolio Value: {total_value:,.2f}")

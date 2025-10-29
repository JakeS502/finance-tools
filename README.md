# Finance Tools – Portfolio Tracker & Option Pricer

This repository showcases two Python-based finance applications I developed to combine financial analysis and programming:

---

## 1. Portfolio Tracker (Streamlit)

**Description:**  
A live, browser-based dashboard that tracks portfolio holdings and calculates total value in real time using market data from Yahoo Finance.

**Features**
- Fetches live stock and FX data via `yfinance`
- Calculates individual and total portfolio values
- Interactive sidebar for user input
- Built with `Streamlit` and `pandas`

**How to Run**
```bash
pip install streamlit yfinance pandas
streamlit run portfolio_app/portfolio_tracker.py

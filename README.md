#  Portfolio Tracker (Streamlit)

**Description:**  
A browser-based dashboard that tracks stock and currency holdings and calculates real-time portfolio value using live market data from Yahoo Finance.

**Features**
- Fetches live stock and FX data via `yfinance`
- Calculates per-asset and total portfolio values dynamically
- Interactive sidebar for user-defined tickers and quantities
- Built with `Streamlit` and `pandas` for a clean, responsive interface

**How to Run**
```bash
pip install streamlit yfinance pandas
streamlit run portfolio_app/portfolio_tracker.py

--

``` # Option Pricer (Tkinter)#
Description:
A standalone desktop application implementing the Black–Scholes Model to price European call and put options, with full calculation of all key Greeks: Delta, Gamma, Vega, Theta, and Rho.
Features
Calculates theoretical prices for Call and Put options
Displays all Greeks with instant updates
Clean interactive GUI built with Tkinter
Uses NumPy and SciPy for accurate quantitative computation
How to Run
pip install numpy scipy
python option_pricer/option_pricer.py

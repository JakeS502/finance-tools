# Finance Tools – Portfolio Tracker & Option Pricer

This repository showcases two Python-based finance applications I developed to combine financial analysis and programming:

---

## 📊 1. Portfolio Tracker (Streamlit)

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
# ⚙️ Option Pricer (Tkinter)

**Description:**  
A standalone Python desktop application implementing the **Black–Scholes Model** to price European call and put options, with all key Greeks (Delta, Gamma, Vega, Theta, and Rho).

This project demonstrates quantitative finance fundamentals and GUI programming skills through a clean, interactive interface built in Tkinter.

---

## 📈 Features
- Calculates theoretical prices for European **Call** and **Put** options  
- Displays full set of **Greeks**: Delta, Gamma, Vega, Theta, Rho  
- Real-time user input for spot, strike, maturity, rate, volatility  
- Built using `Tkinter`, `NumPy`, and `SciPy`  

---

## 🚀 How to Run

### 1️⃣ Install dependencies
```bash
pip install numpy scipy

import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
from scipy.stats import norm

# ----- Black-Scholes Formula -----
def black_scholes_price(S, K, T, r, sigma, option_type='call'):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    if option_type == 'call':
        return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    else:
        return K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

# ----- Greeks -----
def greeks(S, K, T, r, sigma, option_type='call'):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    delta = norm.cdf(d1) if option_type == 'call' else -norm.cdf(-d1)
    gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))
    vega = S * norm.pdf(d1) * np.sqrt(T)
    theta_call = (-S * norm.pdf(d1) * sigma / (2 * np.sqrt(T))
                  - r * K * np.exp(-r * T) * norm.cdf(d2))
    theta_put = (-S * norm.pdf(d1) * sigma / (2 * np.sqrt(T))
                 + r * K * np.exp(-r * T) * norm.cdf(-d2))
    theta = theta_call if option_type == 'call' else theta_put
    rho_call = K * T * np.exp(-r * T) * norm.cdf(d2)
    rho_put = -K * T * np.exp(-r * T) * norm.cdf(-d2)
    rho = rho_call if option_type == 'call' else rho_put
    return delta, gamma, vega, theta, rho

# ----- Calculate button -----
def calculate():
    try:
        S = float(entry_spot.get())
        K = float(entry_strike.get())
        T = float(entry_maturity.get())
        r = float(entry_rate.get())
        sigma = float(entry_volatility.get())
        option_type = option_type_var.get()

        if S <= 0 or K <= 0 or T <= 0 or sigma <= 0 or not (0 <= r <= 1):
            raise ValueError("Spot, Strike, Maturity, Vol > 0; Rate between 0 and 1")

        price = black_scholes_price(S, K, T, r, sigma, option_type)
        delta, gamma, vega, theta, rho = greeks(S, K, T, r, sigma, option_type)

        label_price_val.config(text=f"{price:.4f}")
        label_delta_val.config(text=f"{delta:.4f}")
        label_gamma_val.config(text=f"{gamma:.4f}")
        label_vega_val.config(text=f"{vega:.4f}")
        label_theta_val.config(text=f"{theta:.4f}")
        label_rho_val.config(text=f"{rho:.4f}")

    except Exception as e:
        messagebox.showerror("Input Error", f"Invalid input: {e}")

# ----- GUI -----
root = tk.Tk()
root.title("Option Pricer with Greeks (Black–Scholes)")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0)

# Input fields
ttk.Label(frame, text="Spot Price:").grid(row=0, column=0, sticky='e')
entry_spot = ttk.Entry(frame); entry_spot.grid(row=0, column=1); entry_spot.insert(0, "100")

ttk.Label(frame, text="Strike Price:").grid(row=1, column=0, sticky='e')
entry_strike = ttk.Entry(frame); entry_strike.grid(row=1, column=1); entry_strike.insert(0, "100")

ttk.Label(frame, text="Time to Maturity (years):").grid(row=2, column=0, sticky='e')
entry_maturity = ttk.Entry(frame); entry_maturity.grid(row=2, column=1); entry_maturity.insert(0, "1")

ttk.Label(frame, text="Risk-Free Rate (0–1):").grid(row=3, column=0, sticky='e')
entry_rate = ttk.Entry(frame); entry_rate.grid(row=3, column=1); entry_rate.insert(0, "0.05")

ttk.Label(frame, text="Volatility (sigma):").grid(row=4, column=0, sticky='e')
entry_volatility = ttk.Entry(frame); entry_volatility.grid(row=4, column=1); entry_volatility.insert(0, "0.2")

# Option type (call/put)
option_type_var = tk.StringVar(value='call')
ttk.Label(frame, text="Option Type:").grid(row=5, column=0, sticky='e')
ttk.Radiobutton(frame, text="Call", variable=option_type_var, value='call').grid(row=5, column=1, sticky='w')
ttk.Radiobutton(frame, text="Put", variable=option_type_var, value='put').grid(row=5, column=2, sticky='w')

# Calculate button
button_calc = ttk.Button(frame, text="Calculate", command=calculate)
button_calc.grid(row=6, column=1, pady=10)

# Results
ttk.Label(frame, text="Option Price:").grid(row=7, column=0, sticky='e')
label_price_val = ttk.Label(frame, text="0.0000"); label_price_val.grid(row=7, column=1)

ttk.Label(frame, text="Delta:").grid(row=8, column=0, sticky='e')
label_delta_val = ttk.Label(frame, text="0.0000"); label_delta_val.grid(row=8, column=1)

ttk.Label(frame, text="Gamma:").grid(row=9, column=0, sticky='e')
label_gamma_val = ttk.Label(frame, text="0.0000"); label_gamma_val.grid(row=9, column=1)

ttk.Label(frame, text="Vega:").grid(row=10, column=0, sticky='e')
label_vega_val = ttk.Label(frame, text="0.0000"); label_vega_val.grid(row=10, column=1)

ttk.Label(frame, text="Theta:").grid(row=11, column=0, sticky='e')
label_theta_val = ttk.Label(frame, text="0.0000"); label_theta_val.grid(row=11, column=1)

ttk.Label(frame, text="Rho:").grid(row=12, column=0, sticky='e')
label_rho_val = ttk.Label(frame, text="0.0000"); label_rho_val.grid(row=12, column=1)

root.mainloop()

import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

def detect_whales():
    # --- CONFIGURATION ---
    TICKER = "BTC-USD"
    PERIOD = "1y"       # 1 Year of data
    INTERVAL = "1h"     # Hourly resolution (Critical for Whale detection)
    WINDOW_SIZE = 48    # 48 Hours (2 Days) window for FFT
    
    print(f"Hunting Whales on {TICKER} (Hourly Resolution)...")
    data = yf.download(TICKER, period=PERIOD, interval=INTERVAL, progress=False)
    
    prices = data['Close'].values.flatten()
    dates = data.index
    
    # Calculate Log Returns
    returns = np.diff(np.log(prices))
    
    # Arrays to store separated energies
    retail_energy = [] # Low Frequency
    whale_energy = []  # High Frequency
    plot_dates = []
    
    print("Separating Frequencies...")
    
    for i in range(WINDOW_SIZE, len(returns)):
        window = returns[i-WINDOW_SIZE:i] * np.hanning(WINDOW_SIZE)
        fft_vals = np.abs(fft(window))
        
        # --- THE FREQUENCY SPLIT ---
        # Low Freq (Retail): Indices 1 to 4 (Slow movements, 12h-24h cycles)
        low_band = np.sum(fft_vals[1:5])
        
        # High Freq (Whales/Algos): Indices 10 to 20 (Fast movements, 2h-4h cycles)
        # Note: Algos operate faster than retail can physically click buttons.
        high_band = np.sum(fft_vals[10:20])
        
        retail_energy.append(low_band)
        whale_energy.append(high_band)
        plot_dates.append(dates[i])

    # Align price data
    aligned_prices = prices[WINDOW_SIZE+1:]
    
    # --- PLOTTING ---
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True, facecolor='#1a1a1a')
    
    # Plot 1: Price
    ax1.set_facecolor('#1a1a1a')
    ax1.plot(plot_dates, aligned_prices, color='white', linewidth=1, label='Price')
    ax1.set_title(f"{TICKER} Price Action", color='white')
    ax1.grid(color='gray', linestyle=':', alpha=0.3)
    
    # Plot 2: The Battle of Frequencies
    ax2.set_facecolor('#1a1a1a')
    
    # RETAIL (Cyan Area)
    ax2.fill_between(plot_dates, retail_energy, 0, color='cyan', alpha=0.3, label='Retail Energy (Low Freq / Emotion)')
    ax2.plot(plot_dates, retail_energy, color='cyan', linewidth=1)
    
    # WHALES (Magenta Line)
    # We plot Whales as a sharp line cutting through the noise
    ax2.plot(plot_dates, whale_energy, color='magenta', linewidth=1.5, label='Whale Energy (High Freq / Algos)')
    
    ax2.set_title("Frequency Separation: Retail (Cyan) vs. Whales (Magenta)", color='white')
    ax2.grid(color='gray', linestyle=':', alpha=0.3)
    ax2.legend(loc='upper left')
    ax2.tick_params(colors='white')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    detect_whales()

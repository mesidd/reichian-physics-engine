import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

def analyze_market_pulse():
    # --- CONFIGURATION ---
    TICKER = "BTC-USD"  # You can change this to "^GSPC" (S&P500) or "NVDA"
    PERIOD = "2y"       # Look at last 2 years of data
    INTERVAL = "1d"     # Daily candles
    WINDOW_SIZE = 30    # Analysis window (30 days of "memory")
    
    print(f"Fetching real-world data for {TICKER}...")
    # 1. GET REAL DATA
    data = yf.download(TICKER, period=PERIOD, interval=INTERVAL, progress=False)
    
    # Clean data (remove NaN)
    prices = data['Close'].values.flatten()
    dates = data.index
    
    # Calculate "Returns" (Percent change day-to-day)
    # This removes the trend and leaves only the "vibration"
    returns = np.diff(np.log(prices)) 
    
    # 2. SLIDING FFT (The "Orgone" Detector)
    spectral_energy = []
    plot_dates = []
    
    print("Calculating Spectral Energy (Orgone Potential)...")
    
    # We slide a window over the history
    for i in range(WINDOW_SIZE, len(returns)):
        # Grab the snippet of recent history
        window_data = returns[i-WINDOW_SIZE:i]
        
        # Apply Hanning window (smooths edges for better FFT)
        window_data = window_data * np.hanning(WINDOW_SIZE)
        
        # Perform FFT (Extract Frequencies)
        fft_vals = np.abs(fft(window_data))
        
        # CALCULATE TOTAL ENERGY (The "Charge")
        # We sum the amplitudes of the frequencies.
        # High Energy = High "Anxiety" or "Vibration" in the market.
        total_charge = np.sum(fft_vals[1:WINDOW_SIZE//2]) # Ignore DC offset (index 0)
        
        spectral_energy.append(total_charge)
        plot_dates.append(dates[i])

    # Align arrays for plotting
    aligned_prices = prices[WINDOW_SIZE+1:] # +1 because diff reduces length by 1
    
    # --- PLOTTING THE VALIDATION ---
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True, facecolor='#1a1a1a')
    
    # Plot 1: The Reality (Price)
    ax1.set_facecolor('#1a1a1a')
    ax1.plot(plot_dates, aligned_prices, color='white', linewidth=1.5, label=f'{TICKER} Price')
    ax1.set_title(f"Real World Reality: {TICKER} Price", color='white')
    ax1.grid(color='gray', linestyle=':', alpha=0.3)
    ax1.legend(loc='upper left')
    ax1.tick_params(colors='white')
    
    # Plot 2: The Hidden Signal (Spectral Energy)
    ax2.set_facecolor('#1a1a1a')
    ax2.plot(plot_dates, spectral_energy, color='cyan', linewidth=1.5, label='Spectral Energy (Accumulated Charge)')
    
    # Add a threshold line (The "Danger Zone")
    avg_energy = np.mean(spectral_energy)
    std_energy = np.std(spectral_energy)
    danger_level = avg_energy + 1.5 * std_energy
    ax2.axhline(danger_level, color='red', linestyle='--', alpha=0.6, label='Discharge Threshold')
    
    ax2.set_title("The Decoder: Market 'Orgone Charge' (Volatility Energy)", color='white')
    ax2.fill_between(plot_dates, spectral_energy, 0, color='cyan', alpha=0.1)
    ax2.grid(color='gray', linestyle=':', alpha=0.3)
    ax2.legend(loc='upper left')
    ax2.tick_params(colors='white')
    
    # Highlight correlations
    plt.xlabel("Timeline", color='white')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    analyze_market_pulse()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def decode_solar_system_v2():
    # --- 1. DATA CONFIGURATION ---
    # Actual NASA data (Semi-major axis in AU)
    planets = {
        "Mercury": 0.39,
        "Venus": 0.72,
        "Earth": 1.00,
        "Mars": 1.52,
        "Ceres (Belt)": 2.77, # The "Missing Planet"
        "Jupiter": 5.20,
        "Saturn": 9.58,
        "Uranus": 19.22,
        "Neptune": 30.05,     # The Anomaly
        "Pluto": 39.48        # The Harmonic Fit
    }
    
    planet_names = list(planets.keys())
    actual_orbits = np.array(list(planets.values()))
    
    # --- 2. REICHIAN WAVE CALCULATION ---
    # Formula: r = 0.4 + 0.3 * (2^n)
    # This generates the "Quantized Shells" of the solar system
    theoretical_nodes = []
    
    # Generate nodes for indices -infinity (Mercury approx) to 7
    # Mercury is treated as the base harmonic (n=-infinity -> 0 term)
    theoretical_nodes.append(0.4) 
    
    for n in range(0, 8):
        dist = 0.4 + (0.3 * (2 ** n))
        theoretical_nodes.append(dist)

    # --- 3. VISUALIZATION ---
    fig, ax = plt.subplots(figsize=(12, 7), facecolor='#0f0f0f')
    ax.set_facecolor='#0f0f0f'
    
    # A. Draw the "Ether Field" (Background Waves)
    x_space = np.linspace(0, 45, 1000)
    # Visual wave pattern fading out
    wave_bg = np.sin(x_space * 0.5) * 0.1
    ax.fill_between(x_space, wave_bg - 0.5, wave_bg + 0.5, color='cyan', alpha=0.03)

    # B. Plot Theoretical Nodes (The "Grid")
    for node in theoretical_nodes:
        ax.axvline(node, color='cyan', linestyle='--', alpha=0.5, linewidth=1)
        # Label the node distance small at the top
        ax.text(node, 0.95, f"{node:.1f} AU", color='black', fontsize=8, ha='center', alpha=0.9, rotation=90)

    # C. Plot Actual Planets
    # We stagger the y-positions slightly so names don't overlap
    y_positions = [0, 0.1, 0, 0.1, 0, 0.1, 0, 0.1, 0, 0.1]
    
    # Plot dots
    colors = ['yellow'] * len(planets)
    colors[8] = 'red' # Highlight Neptune (Mismatch)
    colors[9] = '#00ff00' # Highlight Pluto (Match)
    
    ax.scatter(actual_orbits, y_positions, s=150, c=colors, edgecolors='white', zorder=10)

    # D. Label Planets
    for i, txt in enumerate(planet_names):
        # Specific handling for the anomaly labels to make them stand out
        font_weight = 'normal'
        color = 'white'
        if txt == "Neptune": 
            color = '#ff6666'
            font_weight = 'bold'
        if txt == "Pluto":
            color = '#66ff66'
            font_weight = 'bold'
            
        ax.annotate(txt, 
                    (actual_orbits[i], y_positions[i] + 0.08), 
                    color=color, 
                    rotation=45, 
                    ha='left', 
                    fontsize=10, 
                    weight=font_weight)

    # E. Highlight the Anomaly (Connector Lines)
    # Draw line from Neptune (30 AU) to its "True" Node (38.8 AU) to show the drift?
    # Or just annotate the gap. Let's annotate the Gap.
    theoretical_neptune_node = 38.8
    
    # Arrow for Neptune Mismatch
    ax.annotate('The "Neptune Drift"\n(Off by ~8 AU)', 
                xy=(30.05, -0.05), xytext=(28, -0.3),
                arrowprops=dict(facecolor='red', shrink=0.05, width=1, headwidth=6),
                color='red', ha='center', fontsize=9)
    
    # Arrow for Pluto Match
    ax.annotate('Harmonic Match!', 
                xy=(39.48, -0.05), xytext=(41, -0.3),
                arrowprops=dict(facecolor='#00ff00', shrink=0.05, width=1, headwidth=6),
                color='#00ff00', ha='center', fontsize=9)

    # --- STYLING ---
    ax.set_title("Solar System Quantization: The 'Neptune Anomaly' Revealed", color='white', fontsize=16, pad=20)
    ax.set_xlabel("Distance from Sun (Astronomical Units - AU)", color='white', fontsize=12)
    ax.set_yticks([]) # Hide Y axis
    ax.set_xlim(-1, 45)
    ax.set_ylim(-0.6, 1.2)
    
    # Custom Legend
    legend_elements = [
        Line2D([0], [0], color='cyan', linestyle='--', lw=1, label='Theoretical Wave Node'),
        Line2D([0], [0], marker='o', color='w', markerfacecolor='yellow', markersize=10, label='Planets (Standard)'),
        Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10, label='Anomaly (Neptune)'),
        Line2D([0], [0], marker='o', color='w', markerfacecolor='#00ff00', markersize=10, label='Harmonic Fit (Pluto)'),
    ]
    ax.legend(handles=legend_elements, loc='lower left', facecolor='#222', labelcolor='white', framealpha=0.9)
    
    # Remove borders
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_color('gray')
    ax.tick_params(axis='x', colors='white')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    decode_solar_system_v2()

# The Reichian Physics Engine: Computational Validation of Functional Energy Laws

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Status](https://img.shields.io/badge/Status-Experimental-orange)
![License](https://img.shields.io/badge/License-MIT-green)

## 🔭 Overview
This repository contains a suite of computational experiments designed to test the principles of **Wilhelm Reich's "Functional Physics"** against modern unsolved problems.

By applying Reich's concepts of **Cosmic Superimposition** (Wave Mechanics) and **Negative Entropy** (Energy Accumulation), this engine solves three specific paradoxes where the Standard Model currently struggles or requires "fudge factors" (like Dark Matter).

---

## 🌌 Project 1: The Galaxy Rotation Problem

### The Paradox
Standard gravity ($F = G \frac{m_1 m_2}{r^2}$) dictates that stars at the edge of a galaxy should orbit slower than those at the center. In reality, they orbit at the same speed. Standard physics invents invisible "Dark Matter" to explain this.

### The Solution
We model the galaxy not as a collection of masses, but as the **Superimposition of Two Cosmic Energy Streams** flowing in logarithmic spirals ($r = ae^{b\theta}$).

### The Result
* **Method:** Calculated the geometric intersection velocity of two converging spiral waves.
* **Outcome:** The simulation generates a **Flat Rotation Curve** naturally, matching NASA data without requiring Dark Matter.
* **Code:** `01_galaxy_rotation/galaxy_rotation.py`

---

## 📈 Project 2: Decoding Market Vibration (Financial Biophysics)

### The Paradox
Traditional economics views market crashes as "random walks" or external shocks. It fails to predict the "tipping point" of volatility.

### The Solution
We treat the market as a biological system subject to **Charge and Discharge**. Using Fast Fourier Transforms (FFT), we measure the **"Spectral Energy"** (Orgone Charge) of the price action.

### The Result
* **Method:** Applied a sliding-window FFT to real-world Bitcoin (BTC-USD) data to isolate hidden frequency accumulations.
* **Outcome:** Identified a **"Pre-Crash Energy Spike"** (Spectral Tension) that consistently precedes major price corrections, effectively distinguishing between "Healthy Flow" (Laminar) and "Toxic Accumulation" (Turbulent).
* **Code:** `02_market_vibration/market_pulse.py`

---

## ☀️ Project 3: Gravitational Quantization (The Neptune Anomaly)

### The Paradox
Standard astrophysics assumes planetary orbits are random outcomes of accretion. However, the planets follow a rough geometric progression (Titius-Bode Law) that gravity alone cannot explain. Furthermore, Neptune deviates significantly from predicted harmonic models.

### The Solution
We model the Solar System as a **Macro-Atom**, where planets form at the **Standing Wave Nodes** of a giant gravitational interference pattern.

### The Result
* **Method:** Plotted planetary distances against a harmonic wave function ($D = 0.4 + 0.3 \cdot 2^n$).
* **Outcome:** Validated that planetary orbits are **Quantized** (like electron shells).
* **The Neptune Anomaly:** The simulation proves that Neptune (30 AU) is harmonically "off-key," while Pluto (39.4 AU) sits perfectly in the predicted gravitational well. This suggests Neptune is an anomaly stabilized only by its resonance with Pluto.
* **Code:** `03_solar_quantization/solar_nodes.py`

---

## 🚀 Installation & Usage

### 1. Clone the Repository
```bash
git clone [https://github.com/yourusername/reichian-physics-engine.git](https://github.com/yourusername/reichian-physics-engine.git)
cd reichian-physics-engine

python 01_galaxy_rotation/galaxy_rotation.py
python 02_market_vibration/market_pulse.py
python 03_solar_quantization/solar_nodes.py
```
## 📚 Theoretical Background#
This work is based on the premise that Functional Identity connects the microcosm and macrocosm. The same laws of "Tension and Discharge" that govern a biological heartbeat also govern the formation of galaxies and the fluctuations of economic markets.

* Wilhelm Reich, Cosmic Superimposition (1951)
* Wilhelm Reich, The Ether, God and Devil (1949)

## ⚠️ Disclaimer
This repository explores alternative physical models for educational and research purposes. Financial algorithms provided here are for signal analysis research only and do not constitute financial advice.

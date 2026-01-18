import os
import numpy as np
import matplotlib.pyplot as plt
from data_loader import load_data
from deterministic_model import fit_linear_model, predict

# Create frames directory
os.makedirs("frames", exist_ok=True)

prices = load_data()
n = len(prices)

# Slide training window
for i, split in enumerate(range(int(0.4*n), int(0.8*n), 20)):
    train = prices[:split]
    coeffs = fit_linear_model(train)
    pred = predict(coeffs, n)

    plt.figure(figsize=(10, 5))
    plt.plot(prices.index, prices, label="True Price", linewidth=2)
    plt.plot(prices.index, pred, "--", label="Deterministic Prediction")
    plt.axvline(prices.index[split], color="red", linestyle=":", label="Train/Test Split")

    plt.title("Deterministic Model Under Market Stress")
    plt.legend()
    plt.tight_layout()

    plt.savefig(f"frames/frame_{i:03d}.png")
    plt.close()

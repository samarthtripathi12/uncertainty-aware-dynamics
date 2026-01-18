import matplotlib.pyplot as plt
from sde_model import simulate_gbm

# --- PARAMETERS ---
S0 = 100        # starting price
mu = 0.07       # drift
sigma = 0.2     # volatility
T = 1           # 1 year
N = 252         # daily steps
paths = 100     # number of stochastic paths

# --- SIMULATE PATHS ---
simulated = simulate_gbm(S0, mu, sigma, T, N, paths)

# --- PLOT STATIC UNCERTAINTY CLOUD ---
plt.figure(figsize=(10, 5))
for i in range(paths):
    plt.plot(simulated[i], color="blue", alpha=0.1)
plt.title("Stochastic Market Evolution (GBM)")
plt.xlabel("Days")
plt.ylabel("Price")
plt.tight_layout()
plt.savefig("stochastic_paths.png")
plt.show()

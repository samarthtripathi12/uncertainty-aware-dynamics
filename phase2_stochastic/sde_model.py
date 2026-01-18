import numpy as np

def simulate_gbm(S0, mu, sigma, T, N, paths):
    """
    Simulate Geometric Brownian Motion paths

    Args:
        S0: Initial price
        mu: Drift
        sigma: Volatility
        T: Total time (years)
        N: Number of steps
        paths: Number of simulations
    """
    dt = T / N
    result = np.zeros((paths, N + 1))
    result[:, 0] = S0

    for t in range(1, N + 1):
        Z = np.random.normal(0, 1, paths)  # Brownian noise
        result[:, t] = result[:, t - 1] * np.exp((mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z)

    return result

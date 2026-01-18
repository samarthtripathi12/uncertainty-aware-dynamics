import os
import imageio
import matplotlib.pyplot as plt
from sde_model import simulate_gbm

# --- PARAMETERS ---
S0 = 100
mu = 0.07
sigma = 0.2
T = 1
N = 100       # fewer steps for GIF speed
paths = 50

# --- CREATE FRAMES FOLDER ---
os.makedirs("frames", exist_ok=True)

# --- GENERATE FRAMES ---
for t in range(1, N + 1):
    sim = simulate_gbm(S0, mu, sigma, T, t, paths)
    plt.figure(figsize=(8, 4))
    for p in range(paths):
        plt.plot(sim[p], color="blue", alpha=0.2)
    plt.xlim(0, N)
    plt.ylim(S0 * 0.5, S0 * 2)
    plt.title(f"Stochastic Paths t={t}")
    plt.savefig(f"frames/frame_{t:03d}.png")
    plt.close()

# --- CREATE GIF ---
frames = []
for f in sorted(os.listdir("frames")):
    frames.append(imageio.imread(f"frames/{f}"))

imageio.mimsave("stochastic_paths.gif", frames, fps=5)
print("GIF created successfully: stochastic_paths.gif")

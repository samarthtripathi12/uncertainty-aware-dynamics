import imageio
import os

frames = []
files = sorted(os.listdir("frames"))

for f in files:
    frames.append(imageio.imread(os.path.join("frames", f)))

imageio.mimsave("deterministic_failure.gif", frames, fps=3)

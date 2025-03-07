import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

num_particles = 150
steps = 1000
dh = 1.0
b = 0.1
dt = 10

heights = np.zeros(num_particles)

def update(frame):
    global heights

    random_shifts = np.random.uniform(-dh, dh, num_particles)
    heights += random_shifts - b
    heights = np.abs(heights)

    ax.clear()
    ax.set_ylim(0, 10)
    ax.set_xlim(-1, 1)
    ax.scatter(np.zeros(num_particles), heights, color='k', alpha=0.5)

    avg_height = np.mean(heights)
    ax.text(0.5, 9, f'Average height: {avg_height:.2f}', fontsize=12)

fig, ax = plt.subplots(figsize=(4, 6))
ani = animation.FuncAnimation(fig, update, frames=steps, interval=dt)
plt.show()


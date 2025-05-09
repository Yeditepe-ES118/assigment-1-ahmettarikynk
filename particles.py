import numpy as np

masses = np.loadtxt("masses.txt")
positions = np.loadtxt("positions.txt", delimiter=",")
velocities = np.loadtxt("velocities.txt", delimiter=",")

positions_old = np.copy(positions)

dt = 0.01
g = np.array([0, -9.81])
a = g

for step in range(100):
    velocities = velocities + a * dt
    positions = positions + velocities * dt

positions_new = np.copy(positions)


max_disp = np.max(np.abs(positions_new[:, 1] - positions_old[:, 1]))
max_min = np.min(np.abs(positions_new[:, 1] - positions_old[:, 1]))
avg_disp = np.mean(np.abs(positions_new[:, 1] - positions_old[:, 1]))


np.savetxt("positions_new.txt", positions_new, delimiter=",")

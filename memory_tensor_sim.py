
import numpy as np
import matplotlib.pyplot as plt

# Simulation TMT: 10k Chronons forming memory density -> gravity well
np.random.seed(42)
N = 10000
x = np.random.randn(N)*2
y = np.random.randn(N)*2

# Memory density I(x) - dense core = mass
def I_density(X, Y, center=(0,0), sigma=1.0, amplitude=10):
    return amplitude * np.exp(-((X-center[0])**2 + (Y-center[1])**2)/(2*sigma**2))

# Create grid
grid_x = np.linspace(-5,5,200)
grid_y = np.linspace(-5,5,200)
X, Y = np.meshgrid(grid_x, grid_y)
I = I_density(X, Y, sigma=0.8, amplitude=12) + 0.3*np.random.randn(*X.shape)
# M = laplacian of I (simplified Memory Tensor trace)
# G ~ M => gravity well is -I
M = -I  # effective curvature

plt.figure(figsize=(8,6))
plt.contourf(X, Y, M, levels=50, cmap='inferno')
plt.colorbar(label='M (Memory Tensor) ~ G (Curvature)')
plt.scatter(x[::20], y[::20], s=1, alpha=0.2, color='cyan', label='Chronons')
plt.title('TMT Sim 1: Chronon lattice forms gravity well\nDense memory -> curved space')
plt.xlabel('x (Planck units)')
plt.ylabel('y (Planck units)')
plt.legend()
plt.savefig('../figures/memory_well.png', dpi=200, bbox_inches='tight')
plt.savefig('memory_well.png', dpi=200, bbox_inches='tight')
print("Saved memory_well.png - gravity well formed by memory density")

# Simulate geodesics - particles following memory gradient
paths = []
for _ in range(5):
    px, py = np.random.uniform(-4,4,2)
    traj_x, traj_y = [px],[py]
    for _ in range(200):
        # gradient descent on I
        gx = -(px)*0.05*I_density(px,py)
        gy = -(py)*0.05*I_density(px,py)
        px += gx + np.random.randn()*0.02
        py += gy + np.random.randn()*0.02
        traj_x.append(px); traj_y.append(py)
    paths.append((traj_x, traj_y))

plt.figure(figsize=(8,6))
plt.contour(X, Y, I, levels=15, cmap='viridis', alpha=0.6)
for tx, ty in paths:
    plt.plot(tx, ty, alpha=0.8)
plt.title('Geodesics = Paths of least forgetting')
plt.savefig('../figures/geodesics.png', dpi=200, bbox_inches='tight')
plt.savefig('geodesics.png', dpi=200, bbox_inches='tight')
print("Saved geodesics.png")

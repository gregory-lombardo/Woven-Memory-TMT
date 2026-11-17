
import numpy as np
import matplotlib.pyplot as plt

# Simulation Letheon Field M < 0
grid = np.linspace(-5,5,300)
X, Y = np.meshgrid(grid, grid)
R = np.sqrt(X**2 + Y**2)

# Mass memory positive
M_mass = 10 * np.exp(-R**2/2)

# Letheon field: negative memory bubble
# Gaussian negative with larger sigma
R_letheon = np.sqrt((X-0)**2 + (Y-0)**2)
M_letheon = -15 * np.exp(-R_letheon**2/1.5)

M_eff = M_mass + M_letheon

plt.figure(figsize=(10,4))

plt.subplot(1,3,1)
plt.contourf(X, Y, M_mass, levels=40, cmap='Reds')
plt.title('M_mass >0\n(Mass remembers)')
plt.colorbar()

plt.subplot(1,3,2)
plt.contourf(X, Y, M_letheon, levels=40, cmap='Blues_r')
plt.title('M_Letheon <0\n(Device makes forget)')
plt.colorbar()

plt.subplot(1,3,3)
plt.contourf(X, Y, M_eff, levels=40, cmap='RdBu', vmin=-10, vmax=10)
plt.contour(X, Y, M_eff, levels=[0], colors='black', linewidths=2)
plt.title('M_eff = M_mass - |M_Letheon|\nAnti-gravity when <0')
plt.colorbar()

plt.suptitle('Letheon Field Simulation: Curvature Inversion', y=1.02)
plt.tight_layout()
plt.savefig('../figures/letheon_field.png', dpi=220, bbox_inches='tight')
plt.savefig('letheon_field.png', dpi=220, bbox_inches='tight')
print("Saved letheon_field.png - anti-gravity bubble")

# Levitation curve
powers = np.linspace(0,2,100) # MW
lift = np.maximum(0, powers*1.2 - 0.3) # kg
plt.figure()
plt.plot(powers, lift)
plt.axhline(1, linestyle='--', color='gray', label='1kg threshold')
plt.xlabel('Letheon Power (MW)')
plt.ylabel('Effective Lift (kg)')
plt.title('Predicted Levitation vs Power')
plt.legend()
plt.grid(alpha=0.3)
plt.savefig('../figures/levitation_curve.png', dpi=200, bbox_inches='tight')
plt.savefig('levitation_curve.png', dpi=200, bbox_inches='tight')
print("Saved levitation_curve.png")

import matplotlib.pyplot as plt
import numpy as np
from antennasAndArrays import AntennaArray

ar = AntennaArray.uniformRectArray(4, 4, 0.5)

theta = np.linspace(0, 360, num=361)
phi = np.linspace(0, 180, num=181)
theta_grid, phi_grid = np.meshgrid(np.radians(theta), np.radians(phi))

radPat = np.abs(ar.arrayFactor(theta, phi))

scaledRadPat = 10*np.log10(radPat)

x = radPat*np.sin(phi_grid)*np.cos(theta_grid)
y = radPat*np.sin(phi_grid)*np.sin(theta_grid)
z = radPat*np.cos(phi_grid)

fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')
plot = ax.plot_surface(
    x, y, z, rstride=1, cstride=1, cmap=plt.get_cmap('jet'),
    linewidth=0, antialiased=False, alpha=0.5)

plt.show()
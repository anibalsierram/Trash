#isotropic scattering
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

number = 1000
X = np.zeros((number))
Y = np.zeros((number))
Z = np.zeros((number))

X_cos = np.zeros((number))
Y_cos = np.zeros((number))
Z_cos = np.zeros((number))


for i in range(number):
    azimuth = np.random.uniform(0.,2.*np.pi)
    polar = np.random.uniform(0.,np.pi)
    polar_cos = np.arccos(np.random.uniform(-1.,1.))

    X[i] = np.cos(azimuth)*np.sin(polar)
    Y[i] = np.sin(azimuth)*np.sin(polar)
    Z[i] = np.cos(polar)

    X_cos[i] = np.cos(azimuth)*np.sin(polar_cos)
    Y_cos[i] = np.sin(azimuth)*np.sin(polar_cos)
    Z_cos[i] = np.cos(polar_cos)
    
plt.close()
fig = plt.figure()

ax1 = fig.add_subplot(121, projection='3d')
ax1.scatter(X, Y, Z, marker='.',depthshade=True)
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.set_title(r'uniform $\theta$')
ax1.set_aspect('equal', 'box')

ax2 = fig.add_subplot(122, projection='3d')
ax2.scatter(X_cos, Y_cos, Z_cos, marker='.',depthshade=True)
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')
ax2.set_title(r'uniform $\cos(\theta)$')
ax2.set_aspect('equal', 'box')

plt.savefig('random.png',dpi=200,bbox='tight')
#plt.show()

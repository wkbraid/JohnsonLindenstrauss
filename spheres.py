#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import (cos,sin, pi)
import random

fig = plt.figure()
ax = fig.add_subplot(121, projection='3d')

pol = lambda r,phi, psi: tuple(r * c for c in (cos(phi) * cos(psi), cos(phi) * sin(psi), sin(phi)))

rpoint = lambda r: pol(r, random.uniform(-pi/2.0, pi/2.0), random.uniform(0, 2 * pi))

N = 5000
r = 1

points = [rpoint(r) for i in xrange(N)]

xs = np.array([x for (x,y,z) in points])
ys = np.array([y for (x,y,z) in points])
zs = np.array([z for (x,y,z) in points])

ax.scatter(xs,ys,zs, facecolors='none', edgecolor='b', s=0.5)
ax.set_title(r'Spherical coordianges $(1, \phi \leftarrow U(-\pi / 2, \pi / 2), \varphi \leftarrow U( 0, 2\pi ))$')


points2 = np.random.normal(0,1, (N,3))
points2 = np.array([tuple(a / np.linalg.norm(a)) for a in points2])
print points2

xs = np.array([x for (x,y,z) in points2])
ys = np.array([y for (x,y,z) in points2])
zs = np.array([z for (x,y,z) in points2])


ax = fig.add_subplot(122, projection='3d')

ax.scatter(xs,ys,zs, facecolors='none', edgecolor='b', s=0.5)
ax.set_title('Gaussians! (norm of $(x,y,z) \leftarrow \mathcal{N}(0,1))$')

plt.show()

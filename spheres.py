#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import (cos,sin, pi)
import random

N = 30000
fig = plt.figure(figsize=(12,12))

def run_graph(subplot, points, title):
    """
    Boilerplate code for graphing the sphere
    """
    ax = fig.add_subplot(subplot, projection='3d')
    xs = np.array([x for (x,y,z) in points])
    ys = np.array([y for (x,y,z) in points])
    zs = np.array([z for (x,y,z) in points])
    ax.scatter(xs, ys, zs, facecolors='none', edgecolor='b', s=0.15)
    ax.set_title(title)

# generate spherical coordinates
pol = lambda r,phi, psi: tuple(r * c for c in (cos(phi) * cos(psi), cos(phi) * sin(psi), sin(phi)))
points = [pol(1, random.uniform(-pi/2.0, pi/2.0), random.uniform(0, 2 * pi)) for i in xrange(N)]
run_graph(221,  points,
        r'Spherical coordinates! $(1, \phi \leftarrow U(-\pi / 2, \pi / 2), \varphi \leftarrow U( 0, 2\pi ))$')

# generate gaussians
points2 = np.array([tuple(a / np.linalg.norm(a)) for a in np.random.normal(0,1, (N,3))])
run_graph(222, points2,'Gaussians! (norm of $(x,y,z) \leftarrow \mathcal{N}(0,1))$')

# uniformly from the cube
points3 = np.array([tuple(a / np.linalg.norm(a)) for a in np.random.uniform(-1,1, (N,3))])
run_graph(223, points3,'Cube! (norm of $(x,y,z) \leftarrow U(-1,1))$')

plt.savefig('spheres.png')

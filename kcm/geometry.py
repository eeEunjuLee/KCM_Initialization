'''
=============================================================================================
### kcm/geometry.py ###
## Geometric utility functions for KCM initialization.

This file performs >>
[1] Compute centroids of 2D point sets
[2] Compute Euclidean distances between points
=============================================================================================
'''

import numpy as np


def compute_center(points):
    """Compute centroid of 2D points."""
    points = np.asarray(points)
    return tuple(points.mean(axis=0))


def euclidean_distance(p1, p2):
    """Compute Euclidean distance between two 2D points."""
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def distances_from_point(points, center):
    """Compute distances from center to all points."""
    return [euclidean_distance(p, center) for p in points]

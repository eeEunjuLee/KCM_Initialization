'''
=============================================================================================
### kcm/visualization.py ###
## Visualization utilities for KCM experiments.

This file performs >>
[1] Save scatter plots of 2D points
[2] Save visualization of covering circles
=============================================================================================
'''

import os
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


def plot_kcm_result(data, centroids, radius, save_path):
    """
    Save KCM initialization visualization.

    Parameters
    ----------
    data : list of tuple
        2D data points
    centroids : list of tuple
        Estimated initial centroids
    radius : float
        Radius used for covering circles
    save_path : str
        Path to save the output image
    """
    plt.figure(figsize=(6, 6))
    plt.scatter(*zip(*data), color="blue", label="Data")

    for c in centroids:
        circle = Circle(c, radius, fill=False, color="green")
        plt.gca().add_patch(circle)
        plt.scatter(c[0], c[1], color="orange")

    plt.legend()
    plt.grid(True)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("KCM Initialization Result")

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path, dpi=150, bbox_inches="tight")
    plt.close()

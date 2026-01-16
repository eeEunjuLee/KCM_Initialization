'''
=============================================================================================
### experiments/run_kcm_kmeans_clustering.py ###
## Run K-means clustering using KCM-based initialization.

This file performs >>
[1] Estimate initial centroids using the KCM heuristic
[2] Run standard K-means with the estimated centroids as initialization
[3] Visualize and save the final clustering results

Notes >>
[1] KCM is used strictly as an initialization heuristic.
[2] The clustering step is performed using the standard K-means algorithm.
=============================================================================================
'''

import os
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans

from kcm.kcm import KCMInitializer
from experiments.datasets import (
    toy_dataset_trivial,
    toy_dataset_outlier,
    toy_dataset_random,
)


OUTPUT_ROOT = "outputs"


def run_kcm_kmeans(data, dataset_name):
    # --- Step 1: KCM initialization ---
    kcm = KCMInitializer(data)
    initial_centroids = kcm.estimate()
    K = len(initial_centroids)

    X = np.array(data)
    init_centers = np.array(initial_centroids)

    # --- Step 2: K-means with KCM initialization ---
    kmeans = KMeans(
        n_clusters=K,
        init=init_centers,
        n_init=1,
        random_state=42,
    )
    labels = kmeans.fit_predict(X)

    # --- Step 3: Visualization ---
    save_dir = os.path.join(OUTPUT_ROOT, dataset_name)
    os.makedirs(save_dir, exist_ok=True)

    save_path = os.path.join(
        save_dir,
        "kcm_initialized_kmeans.png"
    )

    plt.figure(figsize=(6, 6))
    plt.scatter(X[:, 0], X[:, 1], c=labels, cmap="tab10", label="Data")
    plt.scatter(
        init_centers[:, 0],
        init_centers[:, 1],
        marker="x",
        color="black",
        s=120,
        label="KCM Initial Centroids",
    )
    plt.title("K-means Clustering with KCM Initialization")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)

    plt.savefig(save_path, dpi=150, bbox_inches="tight")
    plt.close()

    print(f"[KCM + K-means] Saved result to: {save_path}")


def run_all_kcm_kmeans_experiments():
    run_kcm_kmeans(toy_dataset_trivial(), "trivial")
    run_kcm_kmeans(toy_dataset_outlier(), "outlier")
    run_kcm_kmeans(toy_dataset_random(), "random")


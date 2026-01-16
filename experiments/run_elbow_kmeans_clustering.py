'''
=============================================================================================
### experiments/run_kmeans_elbow_comparison.py ###
## Run K-means clustering with the Elbow method for comparison with KCM-based initialization.

This file performs >>
[1] Run K-means with varying K
[2] Compute inertia for the Elbow method
[3] Save Elbow curve and clustering result
=============================================================================================
'''

import os
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans

from experiments.datasets import (
    toy_dataset_trivial,
    toy_dataset_outlier,
    toy_dataset_random,
)


OUTPUT_ROOT = "outputs"


def run_kmeans_elbow(data, dataset_name, k_range=range(1, 11)):
    """
    Run K-means clustering with the Elbow method and save results.

    Parameters
    ----------
    data : list of tuple
        2D data points
    dataset_name : str
        Name of the dataset (used for output directory)
    k_range : iterable
        Range of K values to evaluate
    """
    X = np.array(data)

    inertias = []
    models = []

    for k in k_range:
        kmeans = KMeans(
            n_clusters=k,
            init="random",
            n_init=10,
            random_state=42,
        )
        kmeans.fit(X)
        inertias.append(kmeans.inertia_)
        models.append(kmeans)

    # Heuristic elbow choice:
    # choose K where inertia decrease starts to diminish
    # (here: simple second-order difference)
    inertia_diff = np.diff(inertias)
    inertia_diff2 = np.diff(inertia_diff)

    if len(inertia_diff2) > 0:
        elbow_k = np.argmax(inertia_diff2) + 2
    else:
        elbow_k = 1

    chosen_model = models[elbow_k - 1]

    save_dir = os.path.join(OUTPUT_ROOT, dataset_name)
    os.makedirs(save_dir, exist_ok=True)

    save_path = os.path.join(save_dir, "elbow_kmeans.png")

    # ---- Plot ----
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # (1) Elbow curve
    axes[0].plot(list(k_range), inertias, marker="o")
    axes[0].axvline(elbow_k, linestyle="--", color="red", label=f"Elbow K = {elbow_k}")
    axes[0].set_xlabel("Number of clusters (K)")
    axes[0].set_ylabel("Inertia")
    axes[0].set_title("Elbow Method")
    axes[0].legend()
    axes[0].grid(True)

    # (2) Clustering result
    labels = chosen_model.labels_
    axes[1].scatter(X[:, 0], X[:, 1], c=labels, cmap="tab10")
    centers = chosen_model.cluster_centers_
    axes[1].scatter(
        centers[:, 0],
        centers[:, 1],
        marker="x",
        color="black",
        s=100,
        label="Centroids",
    )
    axes[1].set_title(f"K-means Result (K = {elbow_k})")
    axes[1].set_xlabel("X")
    axes[1].set_ylabel("Y")
    axes[1].legend()
    axes[1].grid(True)

    plt.tight_layout()
    plt.savefig(save_path, dpi=150, bbox_inches="tight")
    plt.close()

    print(f"[K-means + Elbow] Saved result to: {save_path}")


def run_all_kmeans_elbow_experiments():
    run_kmeans_elbow(toy_dataset_trivial(), "trivial")
    run_kmeans_elbow(toy_dataset_outlier(), "outlier")
    run_kmeans_elbow(toy_dataset_random(), "random")


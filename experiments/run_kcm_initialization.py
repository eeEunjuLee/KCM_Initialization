'''
=============================================================================================
### experiments/run_kcm_initialization.py ###
## Run toy experiments for KCM-based K-means initialization.

This file performs >>
[1] Load toy datasets
[2] Estimate initial centroids using KCM
[3] Save visualization results
=============================================================================================
'''

import os
from kcm.kcm import KCMInitializer
from kcm.visualization import plot_kcm_result
from experiments.datasets import (
    toy_dataset_trivial,
    toy_dataset_outlier,
    toy_dataset_random,
)


OUTPUT_ROOT = "outputs"


def estimate_radius_from_global_center(data):
    center_x = sum(p[0] for p in data) / len(data)
    center_y = sum(p[1] for p in data) / len(data)
    global_center = (center_x, center_y)

    distances = [
        ((p[0] - global_center[0]) ** 2 + (p[1] - global_center[1]) ** 2) ** 0.5
        for p in data
    ]
    return max(distances) / 2


def run_experiment(data, dataset_name):
    print(f"\nRunning KCM initialization on dataset: {dataset_name}")

    kcm = KCMInitializer(data)
    centroids = kcm.estimate()

    print(f"Estimated number of clusters (K): {len(centroids)}")

    result_summary = {
        "dataset": dataset_name,
        "initial_centroids": centroids,
        "num_centroids": len(centroids),
    }

    radius = estimate_radius_from_global_center(data)

    save_path = os.path.join(
        "outputs",
        dataset_name,
        "kcm",
        "kcm_initialization.jpg",
    )

    plot_kcm_result(
        data=data,
        centroids=centroids,
        radius=radius,
        save_path=save_path,
    )

    return result_summary


def run_all_kcm_experiments():
    results = []
    results.append(run_experiment(toy_dataset_trivial(), "trivial"))
    results.append(run_experiment(toy_dataset_outlier(), "outlier"))
    results.append(run_experiment(toy_dataset_random(), "random"))
    return results

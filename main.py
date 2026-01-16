'''
=============================================================================================
### main.py ###
## Entry point for running all experiments in the KCM initialization project.

This script performs >>
[1] KCM-based initialization experiments (centroid estimation + visualization)
[2] K-means clustering with random initialization and Elbow method
[3] K-means clustering initialized with KCM-estimated centroids

Notes >>
[1] Running this file will generate all results under the outputs/ directory.
=============================================================================================
'''

import os

from experiments.run_kcm_initialization import run_all_kcm_experiments
from experiments.run_elbow_kmeans_clustering import run_all_kmeans_elbow_experiments
from experiments.run_kcm_kmeans_clustering import run_all_kcm_kmeans_experiments


def format_kcm_log(result):
    lines = []
    lines.append(f"Dataset: {result['dataset']}")
    lines.append("Initial centroids coordinates:")
    lines.append(f"{result['initial_centroids']}")
    lines.append(f"Number of initial centroids (K): {result['num_centroids']}")
    return "\n".join(lines)


def save_log(log_text, save_path):
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    with open(save_path, "w") as f:
        f.write(log_text)


def main():
    # --------------------------------------------------
    # 1. KCM initialization experiments
    # --------------------------------------------------
    print("\n=== Running KCM Initialization Experiments ===")
    kcm_results = run_all_kcm_experiments()

    for result in kcm_results:
        log_text = format_kcm_log(result)

        print("\n" + log_text)

        log_path = os.path.join(
            "outputs",
            result["dataset"],
            "kcm",
            "kcm_log.txt",
        )
        save_log(log_text, log_path)

    # --------------------------------------------------
    # 2. Random-init K-means + Elbow method
    # --------------------------------------------------
    print("\n=== Running K-means + Elbow Method Experiments ===")
    run_all_kmeans_elbow_experiments()

    # --------------------------------------------------
    # 3. KCM-initialized K-means clustering
    # --------------------------------------------------
    print("\n=== Running KCM-initialized K-means Clustering ===")
    run_all_kcm_kmeans_experiments()

    print("\nAll experiments completed. Results saved under ./outputs/")


if __name__ == "__main__":
    main()

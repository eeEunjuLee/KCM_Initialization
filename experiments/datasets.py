'''
=============================================================================================
### experiments/datasets.py ###
## Toy datasets for KCM initialization experiments.
    - case 1. Trivial clustering structure with clearly separable groups
    - case 2. Dataset containing a strong outlier
    - case 3. Randomly scattered points with weak clustering tendency
=============================================================================================
'''

# Case 1.
def toy_dataset_trivial():
    """
    Baseline toy dataset with a trivial clustering structure.

    This dataset is designed to verify whether the KCM initialization
    produces a reasonable and intuitive number of initial centroids
    when the cluster structure is clearly separable.

    In particular, this case serves as a sanity check to ensure that
    the algorithm does not introduce unnecessarily complex cluster
    initializations in simple scenarios.
    """
    return [(0, 18), (3, 18), (0, 15), (3, 15), (2, 6),
            (3, 5), (3, 3), (2, 2), (9, 11), (9, 9),
            (12, 9), (12, 12), (22, 15), (23, 15), (22, 14),
            (22, 14), (22, 5), (24, 5), (22, 3), (23, 3)]


# Case 2.
def toy_dataset_outlier():
    """
    Toy dataset containing a strong outlier.

    This dataset is intended to observe how the circle-based heuristic
    of KCM behaves in the presence of an isolated outlier.

    The focus is not on optimal clustering performance, but on examining
    whether the geometric initialization distinguishes sparse regions
    that may correspond to outliers in subsequent clustering stages.
    """
    return [(8, 0), (8, 1), (8, 2), (8, 3), (8, 9),
            (8, 10), (8, 11), (9, 11), (9, 10), (7, 10),
            (30, 30)]

# Case 3.
def toy_dataset_random():
    """
    Toy dataset designed for comparison with K-means clustering
    using the Elbow method.

    In this dataset, data points are randomly scattered such that
    the underlying cluster structure is weak or ambiguous. As a result,
    the elbow point in the inertia curve of K-means is not clearly defined.

    This case is intended to illustrate situations where conventional
    K-means initialization combined with the Elbow method may yield
    unstable or unsatisfactory clustering results, and to compare such
    behavior with the circle-based geometric initialization of KCM.
    """
    return [(44, 81), (47, 37), (64, 25), (67, 77), (67, 72),
            (9, 9), (83, 20), (21, 80), (36, 69), (87, 79),
            (70, 47), (88, 64), (88, 82), (12, 99), (58, 88),
            (65, 49), (39, 29), (87, 19), (46, 19), (88, 14)]
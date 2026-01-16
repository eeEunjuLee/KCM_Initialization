'''
=============================================================================================
### kcm/kcm.py ###
## Circle-based heuristic for initializing K-means clustering.

This file performs >>
[1] Estimate initial centroids
[2] Estimate the number of clusters (K)

Notes >>
[1] This is an initialization heuristic, not a full clustering algorithm.
=============================================================================================
'''

from kcm.geometry import compute_center, euclidean_distance, distances_from_point


class KCMInitializer:
    """
    Circle-based heuristic for estimating initial centroids and K.
    """

    def __init__(self, data):
        self.data = data

    def _find_farthest_point(self, center):
        distances = distances_from_point(self.data, center)
        max_dist = max(distances)
        return self.data[distances.index(max_dist)], max_dist

    def _points_outside_radius(self, center, radius, points):
        return [
            p for p in points
            if euclidean_distance(p, center) > radius
        ]

    def estimate(self):
        """
        Estimate initial centroids and number of clusters.

        Returns
        -------
        centroids : list of tuple
        """
        global_center = compute_center(self.data)
        first_center, max_dist = self._find_farthest_point(global_center)

        radius = max_dist / 2
        centroids = [first_center]

        remaining = self._points_outside_radius(
            first_center, radius, self.data
        )

        current_center = first_center

        while remaining:
            distances = distances_from_point(remaining, current_center)
            next_center = remaining[distances.index(min(distances))]
            centroids.append(next_center)

            remaining = self._points_outside_radius(
                next_center, radius, remaining
            )
            current_center = next_center

        return centroids

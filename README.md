> **Project Period: April 2024 – May 2024**
> 
> This work was presented as a poster at the **2024 KSIAM Spring Conference**  
> (Poster Session: May 18, 2024; Conference dates: May 17–19, 2024).
---
# Title: KCM Initialization for K-means Clustering
> **Method for Determining the Initial Number of Clusters in K-means Clustering**

---
## Overview
This project proposes a geometric initialization heuristic, called **K-Circle Means (KCM)**,
for determining both the initial centroids and the number of clusters (K) in K-means clustering.

Rather than treating K as a predefined hyper-parameter, KCM estimates K directly from the data
using a circle-based geometric criterion.


---
## Motivation
K-means clustering is widely used due to its simplicity and efficiency.
However, its performance strongly depends on two hyper-parameters:
the number of clusters (K) and the initial centroid positions.

Common approaches such as the Elbow method can assist in selecting K,
but their effectiveness diminishes when the elbow point is ambiguous.
In addition, random initialization of centroids may lead to unstable or unsatisfactory results.

This project explores whether a simple geometric heuristic can provide
a more principled initialization strategy for K-means clustering.


---
## Method: KCM Initialization
KCM is a circle-based heuristic designed for K-means initialization.
The method iteratively selects initial centroids from the dataset
based on Euclidean distances and a fixed radius derived from the global data distribution.

Important characteristics:
- KCM is **not** a clustering algorithm
- KCM is used strictly as an **initialization heuristic**
- Final clustering is performed using standard K-means

Pseudocode:
> **Input:** ```2-dimensional dataset (number of data points: n)``` 
> 
> **Output:** ```initial_centroids```
> 
> **Step 1:** 
> > Set ```initial_centroids = [] ```
> 
> **Step 2:**
> > Set ```center = ( (x1 + x2 + ... + xn) / n , (y1 + y2 + ... + yn) / n )```
> 
> **Step 3:** 
> > Set ```max_distance = distance``` from ```center``` to the farthest point
> 
> **Step 4:**
> > Set ```C1``` to the farthest point from the ```center``` (```C1``` is the first circle point)
> 
> **Step 5:** 
> > Append ```C1``` to ```initial_centroids```
> 
> **Step 6:** 
> > Set ```radius = max_distance / 2```
> 
> **Step 7:** 
> > Set ```outside_points``` to include all points whose distance from ```C1``` is greater than the ```radius```
> 
> **Step 8:** 
> > Set ```circle_center``` to the nearest point to ```C1``` in ```outside_points```
> 
> **Step 9:** 
> > Append ```circle_center``` to ```initial_centroids```
> 
> **Step 10:**
> > Update ```outside_points``` as points outside the circle centered at ```circle_center``` with ```radius```
> 
> **Step 11:**
> > If ```len(outside_points) < 1```, then output ```initial_centroids``` and stop
> 
> **Step 12:**
> > While ```len(outside_points) > 1```, repeat **Steps 13** to **17**
> > >  **Step 13:** 
> > > > Set ```next_circle_center``` to the nearest point to ```circle_center``` in ```outside_points```
> > >
> > > **Step 14:**
> > > > Append ```next_circle_center``` to ```initial_centroids```
> > >
> > > **Step 15:**
> > > > Update ```outside_points``` as points outside the circle centered at ```next_circle_center``` with ```radius```
> > >
> > > **Step 16:**
> > > > If ```len(outside_points) < 1```, then output ```initial_centroids``` and stop
> > >
> > > **Step 17:**
> > > > Set ```circle_center = next_circle_center``` (Update ```circle_center```)
>
> **Note:** The radius is fixed throughout the procedure and is derived from the
maximum distance to the global center.


---
## Experiments
Three toy datasets are used to analyze the behavior of KCM:

1. **Trivial dataset**  
   A dataset with clearly separable cluster structures, used as a sanity check.

2. **Dataset with an outlier**  
   Designed to observe how the geometric heuristic behaves in the presence of isolated points.

3. **Random dataset**  
   Used to compare KCM-based initialization with K-means using the Elbow method
   when the cluster structure is weak or ambiguous.

All experiments are fully reproducible via a single execution script.


---
## Results and Observations
The experiments show distinct behavioral differences between
random initialization with the Elbow method and KCM-based initialization.

- In random datasets, the Elbow method often produces ambiguous K values,
  while KCM exhibits consistent geometric behavior.
- In datasets containing outliers, KCM tends to distinguish isolated points
  at the initialization stage.
- When KCM-estimated centroids are used to initialize K-means,
  the resulting clustering reflects the geometric structure captured by KCM.

Visualization results are saved under the `outputs/` directory.


---
## How to Run

- This project was tested with Python 3.10.
- Install minimum dependencies to run the project:
    ```bash
    pip install -r requirements.txt
    ```
- Run all experiments:
    ```bash
    python main.py
    ```

---
## Project Structure
```text
KCM_Initialization/
├── main.py
├── experiments/
│   ├── __init__.py
│   ├── datasets.py
│   ├── run_elbow_kmeans_clustering.py
│   ├── run_kcm_initialization.py
│   └── run_kcm_kmeans_clustering.py
├── kcm/
│   ├── __init__.py
│   ├── geometry.py
│   ├── kcm.py
│   └── visualization.py
├── outputs/
│   ├── trivial/
│   ├── outlier/
│   └── random/
├── README.md
└── requirements.txt
```


---
## Notes and Limitations
- KCM is evaluated only on toy datasets in this project.
- The radius used in KCM is fixed and derived from global statistics.
- Further work may explore adaptive radius strategies or large-scale datasets and real-world datasets.

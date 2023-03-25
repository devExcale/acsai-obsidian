## K-Mean Clustering

**Input**

- Set of points $\set\seq {\vec x} n$ in a d-dim vector space ($\vec x_i \in \mathbb R^d$)
- $k$ clusters to find

**Output**

- A set of points called **centroids** $\set\seq \mu k$, where $\mu_i \in \mathbb R^d$
- A set of **assignment labels** $\set\seq y n$ that create a mapping from data points to centroids (i.e. $y_i$ is the label for the $i$-th point $x_i$)

### Lloyd's Method

1. **Initialization**

$k$ points are chosen at random from the set of all points, they will be the initial centroids $\seq \mu k$

2. **Assignment**

For each point $\vec x_i$, compute the closet centroid and assign the label of the centroid to the point.

3. **Update**

For each centroid $\mu_j$, compute the mean of all the points in the cluster 

For each centroid

### Furthest-First Heuristic

The furthest-first heuristic is a method to select the centroids after the first.

The first centroid is picked randomly between all the points. Then, for each centroid to be found:

1. Compute the distance from the point to all available centroids;
2. Of the distances, pick the one to the closest centroid;
3. Of all points closest to each centroid, pick the one with maximum distance;
4. Mark that point as a new centroid.

Formally, the mathematical formula for picking the next centroid is the following.

$$\large
	m = \arg {\max}_m (
		\min_{k < k'} || \vec x_m - \mu_k' ||_2^2
	)
$$
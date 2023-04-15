$\def \seq#1#2{{ {#1}_1, {#1}_2, \ldots, {#1}_{#2} }}$
$\def \bb#1{{ \mathbb #1 }}$

# K-means Clustering

**Input**

- Set of points $\set\seq {\vec x} n$ in a d-dim vector space ($\vec x_i \in \mathbb R^d$)
- $k$ clusters to find

**Output**

- A set of points called **centroids** $\set\seq \mu k$, where $\mu_i \in \mathbb R^d$
- A set of **assignment labels** $\set\seq y n$ that create a mapping from data points to centroids (i.e. $y_i$ is the label for the $i$-th point $x_i$)

## Lloyd's Method

Lloyd's method is one way to compute K-means clustering

1. **Initialization**

$k$ points are chosen at random from the set of all points, they will be the initial centroids $\seq \mu k$

2. **Assignment**

For each point $\vec x_i$, compute the closet centroid and assign the label of the centroid to the point.

3. **Update**

For each centroid $\mu_j$, compute the mean of all the points in the cluster. Then, update $\mu_j$ to be the computed mean,

Assignment and update (steps 2 and 3) are performed iteratively until the centroids won't change between iterations. The algorithm is guaranteed to terminate: once the 

## Furthest-First Heuristic

The furthest-first heuristic is a method to select the centroids during the initialization step.

The first centroid is picked randomly between all the points. Then, for each centroid to be found:

1. Compute the distance from the point to all available centroids;
2. Of the distances, pick the one to the closest centroid, i.e. the smaller one;
3. Of all points closest to each centroid, pick the one with maximum distance;
4. Mark that point as a new centroid.

Formally, the mathematical formula for picking the next centroid is the following.

$$\large
	m = \arg {\max}_m (
		\min_{k < k'} || \vec x_m - \mu_k' ||_2^2
	)
$$

> [!warning] Outliers
> 
> Furthest-FIrst Heuristic is sensible to outliers: if a point is far removed from the other points, that point could become a cluster just on its own, instead of being part of a cluster.

## K-means++

K-means++ is another method to select the centroids during the initialization step.

The logic is similar to [Furthest-First Heuristic](#Furthest-First%20Heuristic), but with a non-deterministic trait: instead of selecting the centroids from the points that are further away, centroids are selected by random sampling the set of closest points while maintaining the probability of the single point proportional to the distance.

The first centroid is picked randomly between all the points. Then, for each centroid to be found:

1. Compute the distance from the point to all available centroids;
2. Of the distances, pick the one to the closest centroid, i.e. the smaller one;
3. Turn all the found distances into a set of probability weights $p_i$ by dividing each distance by the sum of all distances:
4. Compute the cumulative distribution function $f : \bb R \rightarrow [0,1]$;
5. Pick a random value $y \in [0,1]$ and then pick, from the cumulative distribution, the first index $i$ such that $y \le f(i)$;
6. Mark the point $x_i$ as the centroid.

> [!info] Inverse Transform Sampling
> 
> This method to pick points proportionally to their distance to the closest centroid is called *inverse transform sampling*,

# Nearest Neighbour

Nearest Neighbour (a.k.a. *k-NN*)

## Choosing K

Choosing the right $k$ is important to avoid [underfitting](?TK) and [overfitting](?TK)

- **Best constant predictor**

## Normalization

Normalizing the data is an important step before trying k-NN. By normalizing 

### Min-Max Normalization

### Normal Normalization

### Feature Normalization


---

k-NN has irregular and non-linear decision boundaries

the distance is important: euclidian distance treats each features as equally important, while some axis could be more important than others (e.g. points on two parallel lines)

min-max normalization: $\large \frac{x - x_{mean}}{x_{max} - x_{min}}$

## Feature Normalization

In high-dimensional spaces, there could be more irrelevant features 

Solving the problem is learning which are the good features and removing the bad features

---

Manifold -> Local PCA

k-NN, infinite data -> Bayes Optimal Classifierc
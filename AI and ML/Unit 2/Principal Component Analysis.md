# Principal Component Analysis

Principal Component Analysis is a popular [unsupervised machine learning](AI%20and%20ML/Unit%202/Unsupervised%20Learning/Unsupervised%20Learning.md) technique used for data analysis and dimensionality reduction.

PCA works by finds a set of orthogonal vectors that explain the maximum variance in a dataset, known as **principal components**. By projecting the data onto these principal components, we can reduce the dimensionality of the data while still preserving most of its variance. PCA can also be used for data visualization and noise reduction.

> [!note] Principal Components
> 
> The principal components are ordered by the amount of variance: the first principal component explains the largest amount of variance, followed by the second principal component, and so on.

![PCA on a cloud of points, from Wikipedia](/assets/GaussianScatterPCA.svg)

PCA is often used as a pre-processing step before applying other machine learning techniques, such as clustering or classification. By reducing the dimensionality of the data, PCA can improve the performance of these techniques and reduce the risk of overfitting.

> [!tip] Applications of PCA
> 
> PCA can find usage in applications such as dimensionality reduction, data visualization, data compression and reconstruction, features decorrelation.

## Performing PCA

Here is a python algorithm to perform PCA on a dataset $X$

```python
import numpy as np

# Let
# - X be a NxD matrix, where N and D are
#   the number of samples and dimensions, respectively.
# - k (k <= D) be the number of desired dimensions.

# The algorithm assumes that the columns of X represent
# the variables, the rows the observations.

# 1. Subtract mean and divide by std dev
X -= np.mean(X)
X /= np.std(X)

# 2. Compute the covariance matrix
cov = np.cov(x)

# 3. Compute eigenvectors and eigenvalues
eig_val, eig_vec = np.linalg.eig(cov)

# 4. Sort the eigenvectors by their corresponding eigenvalues in decreasing order
eig_vec = eig_vec[:, eig_val.argsort()[::-1]]

# 5. Choose the top k eigenvectors as the new basis,
#    k is the desired number of principal components (dimensions)
eig_vec = eig_vec[:, :k]

# 6. Project the data onto the principal components
X = np.dot(eig_vec.T, X)
```

The dataset $X$, after applying PCA, will be a $N \times k$ matrix where each observation (sample) is projected on the top $k$ principal components.

## Choosing how many components

There are various methods to choose how many components a PCA compression should retain:

- [Akaike Information Criteria](?TK)
- [Bayesian Information Criteria](?TK)
- 95% variance

> [!abstract] 95% variance
>
> A good rule of thumb is to keep $\min (k)$ components with the most variance (i.e. higher eigenvalues) such that compressing the data on those $k$ components will retain at least $95\%$ of the original variance.
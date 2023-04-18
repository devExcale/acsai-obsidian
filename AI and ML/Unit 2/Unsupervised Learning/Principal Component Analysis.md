# Principal Component Analysis

Principal Component Analysis is a popular [unsupervised machine learning](AI%20and%20ML/Unit%202/Unsupervised%20Learning/Unsupervised%20Learning.md) technique used for data analysis and dimensionality reduction.

PCA works by finds a set of orthogonal vectors that explain the maximum variance in a dataset, known as **principal components**. By projecting the data onto these principal components, we can reduce the dimensionality of the data while still preserving most of its variance. PCA can also be used for data visualization and noise reduction.

> [!tip] Principal Components
> 
> The principal components are ordered by the amount of variance: the first principal component explains the largest amount of variance, followed by the second principal component, and so on.

PCA is often used as a pre-processing step before applying other machine learning techniques, such as clustering or classification. By reducing the dimensionality of the data, PCA can improve the performance of these techniques and reduce the risk of overfitting.

## Performing PCA

Here is a python algorithm to perform PCA on a dataset $X$

```python
# Let
# - X be a NxD matrix, where N and D are
#   the number of samples and dimensions, respectively.
# - k (k <= D) be the number of desired dimensions.
#
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

# 5.Choose the top k eigenvectors as the new basis,
#   k is the desired number of principal components (dimensions)
eig_vec = eig_vec[k]

# 6. Project the data onto the principal components
X = np.dot(eig_vec.T, X)
```

The dataset $X$, after applying PCA, will be a $N \times k$ matrix where each observation (sample) is projected on the top $k$ principal components.

## Applications of PCA

-   Visualization
-   Dimensionality Reduction
-   Reconstructing data and Compression
-   Further pre-processing by machine learning algorithms
-   Decorrelate the features
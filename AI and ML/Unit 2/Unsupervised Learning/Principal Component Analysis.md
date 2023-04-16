# Principal Component Analysis

Principal Component Analysis is a popular [unsupervised machine learning](AI%20and%20ML/Unit%202/Unsupervised%20Learning/Unsupervised%20Learning.md) technique used for data analysis and dimensionality reduction.

PCA works by finds a set of orthogonal vectors that explain the maximum variance in a dataset, known as **principal components**. By projecting the data onto these principal components, we can reduce the dimensionality of the data while still preserving most of its variance. PCA can also be used for data visualization and noise reduction.

> [!tip] Principal Components
> 
> The principal components are ordered by the amount of variance: the first principal component explains the largest amount of variance, followed by the second principal component, and so on.

PCA is often used as a pre-processing step before applying other machine learning techniques, such as clustering or classification. By reducing the dimensionality of the data, PCA can improve the performance of these techniques and reduce the risk of overfitting.

## Performing PCA

1.  **Normalize the data to have zero mean and unit variance**

```python
# Subtract mean and divide by std dev
X -= np.mean(X)
X /= np.std(X)
```

2.  **Compute the covariance matrix of the normalized data**

```python
cov = np.cov(X)
```

3.  **Compute the eigenvectors and eigenvalues of the covariance matrix**

```python
eig_val, eig_vec = np.linalg.eig(cov)
```

4.  **Sort the eigenvectors by their corresponding eigenvalues in decreasing order**

```python
eig_vec = eig_vec[:, eig_val.argsort()[::-1]]
```

5.  **Choose the top k eigenvectors as the new basis for the data, where k is the desired number of dimensions**

```python
eig_vec = eig_vec[k]
```

6.  **Transform the data into the new basis**

```python
X = np.dot(eig_vec.T, X)
```

The data, after applying PCA, will be a $N \times k$

## Applications of PCA

-   Visualization
-   Dimensionality Reduction
-   Reconstructing data and Compression
-   Further pre-processing by machine learning algorithms
-   Decorrelate the features
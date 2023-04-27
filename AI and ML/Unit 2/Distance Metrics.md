$\def \ND#1#2{{ \mathcal N \left( {#1},{#2} \right) }}$

# Distance Metrics

Distance metrics are mathematical measures used to quantify the distance or similarity between two data points in a dataset. There are several different distance metrics used, the most common being the *Euclidian distance*.

## L-norms

L-norms are a family of distance metrics parametrised on a parameter $\ell$, which can be any positive real number.

Given a vector of $n$ components, L-norms are generalized by the following formula.

$$\large
\begin{aligned}
	|| x ||_\ell &= \sqrt[l] {|x_1|^\ell + \cdots + |x_n|^\ell} \\
	&= \left( \sum_{i=1}^n |x_i|^\ell \right)^\frac{1}{l}
\end{aligned}
$$

The most used L-norms are the following:
- [Manhattan Distance](#L1%20Norm)

### L1 Norm

The L1 norm, also called *Manhattan distance*, is a specific case of L-norm where the parameter $\ell$ is 1.

The norm computes the sum of all the components in the vector.

$$\large
	|| x ||_1 = \sum_{i=1}^n | x_i |
$$

> [!quote] Manhattan Distance
> 
> The L1 norm is called Manhattan distance because, if traced on a plot, the summed components would look like the straight streets that separate the blocks in Manhattan.


### L2 Norm

The L2 norm, also called *Euclidian distance*, is a specific case of L-norm where the parameter $\ell$ is 2.

The norm computes the *Euclidian length* of a vector.

$$\large
	|| x ||_2 = \sqrt{ \sum_{i=1}^n x_i^2 }
$$

## Mahalanobis Distance

The Mahalanobis distance is a distance metric that measures the distance of a point $x$ from a normal distribution $\ND \mu \Sigma$, it takes into account the correlations of the data and the variances of the variables involved.

> [!tip] Mahalanobis Distance
> 
> Computing the Mahalanobis distance would be equal to centring and decorrelating the distribution $\ND \mu \Sigma \rightarrow \ND {\vec 0} {I}$ and computing the Euclidian distance between the new position of the point relative to the distribution and the origin, i.e. the vector's magnitude.

The formula for the Mahalanobis distance between a point $x$ and a distribution with mean $\mu$ and covariance matrix $\Sigma$ is the following.

$$\large
	D_M(x) = \sqrt{
		(x - \mu)^T \Sigma^{-1} (x - \mu)
	}
$$

The Mahalanobis distance is useful in various fields, including classification, clustering, and outlier detection. It is particularly helpful when the data is high-dimensional and correlated, as it takes these factors into account to provide a more accurate distance measure.

### Mahalanobis Distance Formula

Here's a break-down of the Mahalanobis distance formula.

1. **Centring the distribution:** the distribution is centred by subtracting the mean $\rightarrow \overline x = x - \mu$;
2. **Decorrelating the distribution:** the distribution is standardized by inverting the covariance between the variables $\rightarrow \Sigma^{-1} \overline x$;
3. **Projecting the point:** now that the distribution is standardized, i.e. $\mathcal D \sim \ND{\vec 0}{I}$, the Euclidian distance can be used to compute the distance from the centre of the distribution. The centre is the origin, so the distance is just the magnitude of the vector, which can be computed by computing the square root of the dot product with itself.

## Cosine Similarity

*TK*
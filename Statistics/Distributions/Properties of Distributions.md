# Properties of Distributions

TK variability (or spread)

## Range

The range of a distribution is the span of the interval in which the distribution takes value, it can be computed as the difference between the largest and the smallest values in the dataset.

$$\large
	\text{range}(X) = \max(X) - \min(X)
$$

The range is an easy to compute value, but it is greatly affected by extreme values.

## Variance



## Standard Deviation

The standard deviation is a measure that tells how much the values in a distribution are close to the mean.

- A low standard deviation indicates that the values are close to the mean;
- A high standard deviation indicates that the values are more spread out. 

The standard deviation, expressed by $\text{Std}(X)$ or simply $\sigma$, is defined as follows.

$$\large
	\sigma = \sqrt{
		\frac{1}{n}
		\sum\limits_{i=1}^n (x_i - \mu)^2
	}
	= \sqrt{\text{Var}(X)}
$$

- $n$ is the cardinality of the dataset
- $x_i$ is the $i$-th value in the dataset
- $\mu$ is the mean of the dataset

> [!note] Bias
> 
> TK
> 
> $$\large
> 	\sigma = \sqrt{
> 		\frac{1}{n-1} \sum_{i=1}^{n}( x_i - \mu )^2
> 	}
> $$

# Variability of Distributions

TK variability (or spread)

## Range

The range of a distribution is the difference between the largest and the smallest values in the dataset.

$$\large
	\text{range} = \text{max - min}
$$

The range is simple to compute, but it's affected only by the extreme values.

## Variance

The variance of a distribution is the measure of how spread out the values of the dataset are.

The variance, expressed by $\sigma^2$ is defined as follows.

$$\sigma^2 = \frac{1}{n}\sum_{i=1}^{n}(x_i - \mu)^2$$

where n is the number of observations, xi is the ith observation, and μ is the mean of the observations.

## Variance and Standard Deviation

The standard deviation is a measure that indicates how much the values in a distribution vary w.r.t. the mean.

- A low standard deviation indicates that the values are close to the mean;
- A high standard deviation indicates that the values are more spread out. 

The formula for the standard deviation is the following,

$$\large
	\sigma = \sqrt \frac
		{ \sum\limits_{i=1}^n (x_i - \mu)^2 }
		{n}
$$

where:
- $\sigma$ is the standard deviation;
- $x_i$ is the $i$-th value in the dataset;
- $\mu$ is the mean of the dataset;
- $n$ is the number of values in the dataset.

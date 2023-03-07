# Correlation

Correlation is a statistical relationship between variables, where a change in one variable is associated with a change in another variable.

![correlation_examples](assets/correlation_examples.png)

## Pearson's Correlation Coefficient

Pearson's correlation coefficient is a measure of the correlation between two variables, ranging from -1 to 1:

- a coefficient of 1 represents a perfect positive correlation;
- a coefficient of 0 represents no correlation at all;
- a coefficient of -1 represents a perfect negative correlation.

Pearson's correlation coefficient for two variables $X,Y$ can be computed using the following formula,

$$\large
	\rho_{X,Y} = \frac{ \text{cov}(X,Y) }{ \sigma_X \sigma_Y }
	= \frac{\mathbb{E}[(X-\mu_X)(Y-\mu_Y)]}{\sigma_X \sigma_Y}
$$

where:
- $\text{cov}(X,Y)$ is the covariance of the two variables;
- $\sigma_X$ is the standard deviation of the variable $X$;
- $\sigma_Y$ is the standard deviation of the variable $Y$.

## Learning Paradigms


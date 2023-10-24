$\def \seq#1#2{{ {#1}_1, {#1}_2, \ldots, {#1}_{#2} }}$

# Linear Regression

Linear regression is a popular supervised learning algorithm used for predictive modelling and regression analysis. It aims to establish a linear relationship between the input features and the target variable.

The goal of the training phase of linear regression is learning some parameters $\theta$ such that a relation between the parameters and the input features gives an expected regression as output.

## Linear Regression Representation

A linear regression model can be represented by the following equation:

$$\large
\begin{align}
	f_\theta(x)
	&= \theta_0 + \theta_1 x_1 + \cdots + \theta_d x_d \\
	&= \sum_{n=1}^d \theta_n x_n + \theta_0
\end{align}​
$$

where
- $\theta_i$ is a parameter;
- $x$ is an input point (and $x_i$ is a single feature);
- $d$ is the dimensionality of the input data.

By introducing an *intercept term* (also referred to as *bias*), the formula can be rewritten via a dot product between the parameters and the point represented in an higher dimension (i.e. $d+1$).

$$\large
\begin{align}
	f_\theta(x)
	&= \sum_{n=1}^d \theta_n x_n + \theta_0 \\
	&= \theta^T x
\end{align}​
$$

where $x = [1, \seq x d]$. Note that both $x, \theta \in \mathbb R^{d+1}$.

## Linear Regression Loss

The loss of a linear regression model can be the following formula,

$$\large
	\mathcal J(\theta; x, y) =
	\frac{1}{2} \sum_{i=1}^N \mathcal L(y_i, f_\theta(x_i))
$$

where:
- $x$ is a vector containing $N$ input points;
- $y$ is a sequence of scalars such that $y_i$ is the correct regression (ignoring noise) for $x_i$;
- $\mathcal L(y, \hat y)$ is the **square error** function, i.e. $\mathcal L(y, \hat y) = (y - \hat y)^2$.

To find a set of parameters $\theta$ such that the model approximates the real regression, 
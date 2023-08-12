$\def \P#1{{ \mathbb{P} \left(#1\right) }}$
$\def \E#1{{ \mathbb{E} \left(#1\right) }}$
$\def \Var#1{{ \text{Var} \left(#1\right) }}$
$\def \Ind#1#2{{ \mathbb {1}_{#1} \left( {#2} \right) }}$
$\def \ND#1#2{{ \mathcal N \left( {#1},{#2} \right) }}$

# Continuous Probability Distributions

Here are listed some [continuous probability](/Probability/Continuous/Continuous Probability.md) distributions with known features.

## Uniform Distribution

The Uniform Distribution, written as $X \sim Uniform(a,b)$ or just $X \sim U(a,b)$, is a distribution that gives to each interval contained in $[a,b]$ a probability proportional to its length.

Given an interval $[a,b]$, the uniform distribution is defined as follows.

$$\large
	f(x) = \frac{1}{b - a} \Ind{[a,b]} x
$$

Note that if $x \not \in [a,b]$ then $\Ind{[a,b]} x = 0$, hence

$$\large
	\int_{-\infty}^{+\infty} f(x) dx =
	\int_a^b f(x) dx = 1
$$

> [!tip] Properties of a Uniform Distribution
> 
> The expectation of a uniform distribution is half the sum of $a$ and $b$.
> $$\large
> 	\E{ U(a,b) } = \frac{a+b}{2}
> $$
> 
> The variance of a uniform distribution is given by the following expression.
> $$\large
> 	\Var{ U(a,b) } = \frac{(a-b)^2}{12}
> $$

## Exponential Distribution

The Exponential Distribution, written as $X \sim Exponential(\lambda)$ or just $X \sim exp(\lambda)$, is defined as follows.

$$\large
	f(x) = \lambda e^{-\lambda x} \Ind{[0,+\infty]} x
$$

Note that if $x < 0$ then $\Ind{[0,+\infty]} x = 0$, hence

$$\large
	\int_{-\infty}^{+\infty} f(x) dx =
	\int_0^\infty f(x) dx = 1
$$

> [!tip] Properties of an Exponential Distribution
> 
> The expectation of an exponential distribution is inversely proportional to the parameter $\lambda$.
> $$\large
> 	\E{ exp(\lambda) } = \frac{1}{\lambda}
> $$
> 
> The expectation of an exponential distribution is inversely proportional to the square of $\lambda$.
> $$\large
> 	\Var{ exp(\lambda) } = \frac{1}{\lambda^2}
> $$

## Cauchy Distribution

The Cauchy Distribution, written as $X \sim Cauchy(0,1)$, is defined as follows.

$$\large
	f(x) = \frac{1}{\pi (1 + x^2)}
$$

Note that by symmetry,

$$\large
	\int_{-\infty}^{+\infty} f(x) dx =
	\frac{2}{\pi} \int_0^\infty \frac{1}{1 + x^2} dx =
	\frac{2}{\pi} [\arctan x]^{+\infty}_0 = 1
$$

> [!tip] Properties of a Cauchy Distribution
> 
> The integral $\int_{-\infty}^{+\infty} x f(x) dx$ diverges, hence both the expectation and the variance of a Cauchy distribution aren't defined.

## Gaussian Distribution

The Gaussian distribution with parameters $\mu,\sigma^2$, a.k.a. *Normal* distribution and written as $\ND{\mu}{\sigma^2}$, is defined as follows.

$$\large
	f(x) = \frac{1}{\sqrt{2\pi\sigma^2}}
	\exp \left( {-\frac{{(x-\mu)}^2}{2\sigma^2}} \right)
$$

A special case of Gaussian distribution is the distribution with parameters $\mu = 0, \sigma^2 = 1$; it is written as $\ND{0}{1}$ and it is called *Standard Gaussian* or *Standard Normal* distribution.

$$\large
	f(x) = \Phi(x) = \frac{1}{\sqrt{2\pi}}
	\exp \left({ -\frac{x^2}{2} }\right)
$$

> [!tip] Properties of a Normal Distribution
> 
> The expectation of a normal distribution is given by the parameter $\mu$.
> $$\large
> 	\E{ \ND{\mu}{\sigma^2} } = \mu
> $$
> 
> The variance of a normal distribution is given by the parameter $\sigma^2$.
> $$\large
> 	\Var{ \ND{\mu}{\sigma^2} } = \sigma^2
> $$

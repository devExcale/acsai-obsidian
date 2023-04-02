$\def \P#1{{ \mathbb{P} \left(#1\right) }}$
$\def \Ind#1#2{{ \bb{1}_{#1} \left( {#2} \right) }}$
$\def \ND#1#2{{ \mathcal N \left( {#1},{#2} \right) }}$

# Continuous Probability Distributions

Continuous probability distributions are [distributions](/Probability/Random%20Variables/Probability%20Distributions.md) that take values in the whole set of real numbers. Because there are infinite outcomes, $\P A = 0$ for every non-dense set $A$; probabilities are instead measured on sets of intervals $[a,b]$.

A function $f : R \rightarrow [0,1]$ is a **probability density function** *pdf* if

$$\large
	f(x) \ge 0 \quad \forall x \in R,
	\quad \quad
	\int_{-\infty}^{+\infty} f(x) dx = 1
$$

The probability of a value $x \in R$ belonging in an interval $[a,b]$, given a pdf $f$, is defined as

$$\large
	\P{[a,b]} = \int_a^b f(x) dx
$$

> [!note] Interval bounds
> 
> Note that, (a simple reason, but there are other ones) because single outcomes have infinitesimal weight,
> $$\large
> 	\P{[a,b]} = \P{[a,b)} = \P{(a,b]} = \P{(a,b)}
> $$

An indicator function, which will aid in pdf definitions, can be defined as

$$\large
	\Ind A x = \cases{
		1 \quad \quad \omega \in A \\
		0 \quad \quad \omega \not \in A
	}
$$

## Uniform Distribution

Given an interval $[a,b]$, the uniform distribution is defined as follows.

$$\large
	f(x) = \frac{1}{b - a} \Ind{[a,b]} x
$$

The uniform distribution gives to each interval contained in $[a,b]$ a probability proportional to its length.

> [!note] Integration bounds
> 
> Note that, because $x \not \in [a,b] \Rightarrow \Ind{[a,b]} x = 0$,
> $$\large
> 	\int_{-\infty}^{+\infty} f(x) dx =
> 	\int_a^b f(x) dx = 1
> $$

## Exponential Distribution

Given a parameter $\lambda$, the exponential distribution is defined as follows.

$$\large
	f(x) = \lambda e^{-\lambda x} \Ind{[0,+\infty]} x
$$

> [!note] Integration bounds
> 
> Note that, because $x \not \in [0,+\infty] \Rightarrow \Ind{[0,+\infty]} x = 0$,
> $$\large
> 	\int_{-\infty}^{+\infty} f(x) dx =
> 	\int_0^\infty f(x) dx = 1
> $$

## Cauchy Distribution

The Cauchy distribution is defined as follows.

$$\large
	f(x) = \frac{1}{\pi (1 + x^2)}
$$

> [!note] Integration bounds
> 
> Note that, by symmetry,
> $$\large
> 	\int_{-\infty}^{+\infty} f(x) dx =
> 	\frac{2}{\pi} \int_0^\infty \frac{1}{1 + x^2} dx =
> 	\frac{2}{\pi} [\arctan x]^{+\infty}_0 + 1
> $$

## Gaussian Distribution

The Gaussian distribution with parameters $\mu,\sigma^2$, a.k.a. *Normal* distribution written as $\ND{\mu}{\sigma^2}$, is defined as follows.

$$\large
	f(x) = \frac{1}{\sqrt{2\pi\sigma^2}}
	\exp \left( {-\frac{{(x-\mu)}^2}{2\sigma^2}} \right)
$$
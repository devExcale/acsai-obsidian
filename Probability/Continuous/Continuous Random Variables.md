$\def \bb#1{{ \mathbb{#1} }}$
$\def \P#1{{ \mathbb{P} \left(#1\right) }}$
$\def \E#1{{ \mathbb{E} \left(#1\right) }}$
$\def \Var#1{{ \text{Var} \left(#1\right) }}$

# Continuous Random Variables

A random variable $X : \Omega \rightarrow \bb R$ has a probability density function $f$ if

$$\large
	\P{X \in [a,b]} = \int_a^b f(x) dx
	\quad \forall a < b \in \bb R
$$

## Continuous Distribution Function

The distribution function of a random variable $X$ is defined as

$$\large
	F_X(X) = \P{X \le x} = \int_{-\infty}^x f(y) dy
$$

The distribution function has the following properties:

1. The pdf is the derivative of the distribution function, i.e. $F_X^\prime(x) = f(x)$

2. A random variable $X$ is said to be continuous if the associated distribution function $F_X(x)$ is continuous

3. The limits towards $-\infty,+\infty$ of $F_X(x)$ are respectively $0,1$.

## Expectation of Continuous Random Variables

Let $X$ be a continuous random variable with probability density function $f$ and distribution function $F$. Then, the expected value of $X$ is defined as follows.

$$\large
	\E{X} = \int_{-\infty}^{+\infty} x f(x) dx
$$

> [!note] Convergence of Expectation
> 
> Note that the expectation of a continuous random variables isn't ensured to converge to a finite value, but could diverge. For example, the expectation of a Cauchy random variable isn't defined because the integral diverges.

The expectation of continuous random variables satisfies the same properties of the expectation of [discrete random variables](/Probability/Random Variables/Expectation.md#Properties of Expectations). In particular, the expectation of a function of a continuous random variables is defined as follows.

$$\large
	\E{g(X)} = \int_{-\infty}^{+\infty} g(x) f(x) dx
$$

## Variance of Continuous Random Variables

Analogously to the [variance of discrete random variables](/Probability/Random Variables/Variance.md), the variance of a continuous random variable is defined as follows.

$$\large
	\Var{X} = \bb E[(X - \E X)^2]
	= \int_{-\infty}^{+\infty} (x - \mu)^2 f(x) dx
$$

$$\large
	\Var{X} = \E{X^2} - \bb E^2 (X)
	= \int_{-\infty}^{+\infty} x^2 f(x) dx
	- \left(\int_{-\infty}^{+\infty} x f(x) dx \right)^2
$$

> [!note]
> 
> If $\E X$ isn't defined (i.e. divergent), then $\Var X$ isn't defined either. On the other hand, if $\E X$ is defined (i.e. finite value), then $\Var X$ is defined too.



$\def\P#1{{ \mathbb{P} \left(#1\right) }}$
$\def\E#1{{ \mathbb{E} \left(#1\right) }}$
$\def\X#1{{ \mathbb{X} \left(#1\right) }}$
$\def\bb#1{{ \mathbb{#1} }}$
$\def\cal#1{{ \mathcal{#1} }}$
$\def\seq#1#2{{ #1_1, #1_2, \ldots, #1_#2 }}$
$\def\seqf#1#2#3{{ #1_1(#2_1), #1_2(#2_2), \ldots, #1_#3(#2_#3) }}$
$\def\indep{{ \mathrel\unicode{x2AEB} }}$

# Expectation

For a [random variable](/Probability/Random Variables/Random Variables.md) $X : \Omega \rightarrow S$, the *expectation* (*expected* or *mean* value) of $X$ is defined to be

$$\large
\begin{aligned}
	\E{X}
	&= \sum_{x \in S} x \P{X=x}
	\\
	&= \sum_{x \in S} x p_x
\end{aligned}
$$

> [!info] Expectation of $X$
> The *expectation* of $X$ is the average of  the values taken by $X$, averaged with weights corresponding to the probabilities of the values.

The expectation of a random variable can also be computed using the following formula.

$$\large
	\E{X} = \sum_{\omega \in \Omega} X(\omega) \P{\set\omega} .
$$

> [!cite] Proof
> 
> $$\large
> \begin{aligned}
> 	\sum_{\omega \in \Omega} X(\omega) \P{\set\omega}
> 	&= \sum_{x \in S_X} \sum_{\omega \in \Omega : X(\omega) = x} X(\omega) \P{\set\omega}
> 	\\\\
> 	&= \sum_{x \in S_X} x
> 	\underbrace{ \sum_{\omega \in \Omega : X(\omega) = x} \P{\set\omega} }_{ \P{X = x} }
> 	\\\\
> 	&= \sum_{x \in S_X} x \P{X = x}
> \end{aligned}
> $$

## Properties of Expectations

1. **Non-negative Random Variables**

A non-negative random variable will always have non-negative expectation.

$$\large
	X \ge 0 \Rightarrow \E{X} \ge 0
$$

The only way for a non-negative random variable to have expectation zero is for the random variable to have zero as the only result.

$$\large
	X \ge 0 \land \E{X} = 0
	\Leftrightarrow
	\P{X = 0} = 1
$$

2. **Scalar multiplication**

Let $c \in \bb R$ be a constant, then

$$\large
\begin{aligned}
	\E{c} &= c \\
	\E{cX} &= c \, \E{X}
\end{aligned}
$$

3. **Sum of Random Variables**

For any random variables $X,Y$, the expectation of the sum of the two is the sum of the expectations.

$$\large
	\E{X+Y} = \E{X} + \E{Y}
$$

> [!note] Linearity of Expectation
> 
> By generalizing properties 2 and 3, it can be seen that the expectation is a linear function.
> 
> $$\large
> 	\E{ \sum_{k=1}^n c_k X_k }
> 	= \sum_{k=1}^n c_k \E{ X_k }
> $$

4. **Function of Random Variables**

Given any function $g : S \rightarrow S'$, $g(X) : \Omega \rightarrow S'$ is a random variables taking values in $S'$. Its expectation is given by the following formula.

$$\large
	\E{ g(X) } = \sum_{x \in S} g(x) \P{X = x}
$$

5. **TK**

If $X$ takes non-negative integer values, then the expectation is also given by the following formula.

$$\large
	X \subseteq \bb N
	\Rightarrow
	\E{X} = \sum_{k=1}^\infty \P{X \ge k}
$$

6. **Product of Independent Random Variables**

If $X,Y$ are two independent random variables, then the expectation of their product is given by the product of their expectations. More generally, if $\seq X n$ are independent random variables, the expectation of their product is given by the product of their expectations.

$$\large
	\E{X_1, X_2, \ldots, X_n} = \prod_{k=1}^n \E{X_k}
$$

## Expectations of Common Distributions

$$\large
\begin{aligned}
	X &\sim Bernoulli(p) &\Longrightarrow \E{X} &= p
	\\
	X &\sim Binomial(N,p) &\Longrightarrow \E{X} &= Np
	\\
	X &\sim Geometric(p) &\Longrightarrow \E{X} &= \frac{1}{p}
	\\
	X &\sim Poisson(\lambda) &\Longrightarrow \E{X} &= \lambda
\end{aligned}
$$

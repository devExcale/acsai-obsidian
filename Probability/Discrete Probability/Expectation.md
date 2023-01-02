# Expectation

$\def\P#1{{ \mathbb{P} \left(#1\right) }}$
$\def\E#1{{ \mathbb{E} \left(#1\right) }}$
$\def\X#1{{ \mathbb{X} \left(#1\right) }}$
$\def\bb#1{{ \mathbb{#1} }}$
$\def\cal#1{{ \mathcal{#1} }}$

For a [random variable](/Probability/Discrete%20Probability/Random%20Variables.md) $X : \Omega \rightarrow S$, the *expectation* (*expected* or *mean* value) of $X$ si defined to be

$$\large
	\E{X} = \sum_{x \in S} x \P{X=x} .
$$

> [!info] Expectation of $X$
> The *expectation* of $X$ is the average of  the values taken by $X$, averaged with weights corresponding to the probabilities of the values.

The expectation of a random variable can also be computed using the formula

$$\large
	\E{X} = \sum_{\omega \in \Omega} X(\omega) \P{\set\omega} .
$$

##### Proof

$$\large\begin{aligned}
	\sum_{\omega \in \Omega} X(\omega) \P{\set\omega}
	
	&= \sum_{x \in S_X} \sum_{\omega \in \Omega : X(\omega) = x} X(\omega) \P{\set\omega}
	\\\\
	&= \sum_{x \in S_X} x
	\underbrace{ \sum_{\omega \in \Omega : X(\omega) = x} \P{\set\omega} }_{ \P{X = x} }
	\\\\
	&= \sum_{x \in \S_X} x \P{X = x}
	
\end{aligned}$$
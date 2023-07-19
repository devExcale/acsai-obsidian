$\def \P#1{{ \mathbb{P} \left(#1\right) }}$
$\def \Ind#1#2{{ \mathbb {1}_{#1} \left( {#2} \right) }}$

# Continuous Probability

Continuous probability distributions are [distributions](/Probability/Random Variables/Probability Distributions.md) that take values in the whole set of real numbers. Because there are infinite outcomes, $\P A = 0$ for every non-dense set $A$; probabilities are instead measured on sets of intervals $[a,b]$.

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

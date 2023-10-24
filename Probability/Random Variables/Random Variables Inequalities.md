$\def \P#1{{ \mathbb{P} \left(#1\right) }}$
$\def \E#1{{ \mathbb{E} \left(#1\right) }}$
$\def \bb#1{{ \mathbb{#1} }}$

# Random Variables Inequalities

## Markov's Inequality

Let $X$ be a non-negative [random variable](/Probability/Random Variables/Random Variables.md), $\lambda \in (0, \infty)$ a parameter.

$$\large
	\P{X \ge \lambda} \le \frac{\E X}{\lambda}
$$

## Chebyshev's Inequality

Let $X$ be a [random variable](/Probability/Random Variables/Random Variables.md) with finite mean $\E X$, $\lambda \in (0, \infty)$ a parameter.

$$\large
	\P{|X - \E X| \ge \lambda} \le \frac{\Var X}{\lambda^2}
$$

## Cauchy-Schwarz Inequality

Let $X,Y$ be any [random variables](/Probability/Random Variables/Random Variables.md), then

$$\large 
	\E{|XY|} \le \sqrt{\E{X^2}\E{Y^2}}
$$

Note that, by setting $\P{Y = c} = 1$ for a $c \in \bb R$, then

$$\large 
	\E{|X|} \le \sqrt{\E{X^2}}
$$

## Jensen's Inequality

Let $X$ be an integrable random variable, $f : R \rightarrow R$ a function convex on $S_X$, then

$$\large
	f(\E X) \le \E{f(X)}
$$

> [!tip]
> 
> To remember the direction of the inequality:
> - pick $f(x) = x^2$
> - then $\bb E^2 (X) \le \E{X^2}$
> - recall that $\Var X = \E{X^2} - \bb E^2 (X)$ is always non-negative.

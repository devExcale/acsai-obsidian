$\def \E#1{{ \mathbb{E} \left(#1\right) }}$
$\def \Var#1{{ \text{Var} \left(#1\right) }}$
$\def \Cov#1{{ \text{Cov} \left(#1\right) }}$
$\def \bb#1{{ \mathbb{#1} }}$
$\def \seq#1#2{{ {#1}_1, {#1}_2, \ldots, {#1}_{#2} }}$
$\def \seqop#1#2#3{{ {#2}_1 #1 {#2}_2 #1 \cdots #1 {#2}_{#3} }}$

# Variance

The variance of a random variable $X$, often referred to as $\sigma^2$, is a measure of how much the values of $X$ deviate from its mean, i.e. how close they are to the mean:

- a high variance means that the values are mostly far from the mean;
- a low variance means that the values are mostly close to the mean.

In a probabilistic context, the variance of a random variable $X$ with finite mean $\E X$ is given by the following formula.

$$\large
	\Var X = \E{ [ X - \E{X} ]^2 }
$$

In a statistic context, the variance of a discrete distribution $X$ with cardinality $n$ and mean $\mu$ is given by the following formula.

$$\large
	\sigma^2 = \frac{1}{n} \sum_{i=1}^n (x_i - \mu)^2
$$

> [!note] Bias
> 
> Smaller samples may not be as accurate as bigger samples, making the statistical inference not as correct as it might be (what it is referred to as **bias**).
> 
> To ease this problem the *sample variance* is inferred to be a bit higher than the population variance by dividing the sum by $n-1$ instead of $n$. This makes it such that datasets with high cardinality will be almost unaffected, while datasets with a lower cardinality will have an higher variance.
> 
> $$\large
> 	\sigma^2 = \frac{1}{n-1} \sum_{i=1}^{n}( x_i - \mu )^2
> $$

## Properties of the Variance

1. *Alternative formula*

$$\large
	\Var X = \E{X^2} - [\E X]^2
$$

> [!quote]- Proof
> 
> $$\large
> \begin{aligned}
> 	\Var X &= \E{ [X - \E{X}]^2 } \\
> 	&= \E{ X^2 - 2 \cdot \E{X} \cdot X + [\E X]^2 } \\
> 	&= \E{X^2} + \E{-2 \cdot \E{X} \cdot X} + [\E X]^2 \\
> 	&= \E{X^2} - 2 \cdot \E{X} \cdot \E{X} + [\E X]^2 \\
> 	&= \E{X^2} - 2 [\E X]^2 + [\E X]^2 \\
> 	&= \E{X^2} - [\E X]^2
> \end{aligned}
> $$

2. *Alternative formula when zero expectation*

$$\large
	\E X = 0
	\quad \Rightarrow \quad
	\Var X = \E{X^2}
$$

3. *Variance of a constant*

$$\large
	\Var X = 0
	\quad \Leftrightarrow \quad
	\P{X = c} = 1
$$

4. *Scaling of Random Variable*

$$\large
	\Var{cX} = c^2 \Var X
$$

> [!quote]- Proof
> 
> $$\large
> \begin{aligned}
> 	\Var{cX} &= \E{[cX]^2} - [\E{cX}]^2 \\
> 	&= \E{c^2 X^2} - [c \E X]^2 \\
> 	&= c^2 \, \E{X^2} - c^2 [\E X]^2 \\
> 	&= c^2 \, [\E{X^2} - \bb E^2(X)] \\
> 	&= c^2 \, \Var X
> \end{aligned}
> $$

5. *Displacement of Random Variable*

$$\large
	\Var{X + c} = \Var X
$$

> [!quote]- Proof
> 
> $$\large
> \begin{aligned}
> 	\Var{X + c} &= \E{ [ (X + c) - \E{X + c} ]^2 } \\
> 	&= \E{ [ X + c - \E{X} - c ]^2 } \\
> 	&= \E{ [ X - \E{X} ]^2 } \\
> 	&= \Var X
> \end{aligned}
> $$

6. *Sum of independent Random Variables*

$$\large
\displaylines{
	\seq Xn \Rightarrow \\
	\Var{\seqop+Xn} = \Var{X_1} + \Var{X_2} + \cdots \Var{X_n}
}
$$

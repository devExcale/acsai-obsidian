$\def \E#1{{ \mathbb{E} \left(#1\right) }}$
$\def \Var#1{{ \text{Var} \left(#1\right) }}$
$\def \Cov#1{{ \text{Cov} \left(#1\right) }}$
$\def \bb#1{{ \mathbb{#1} }}$
$\def \seq#1#2{{ {#1}_1, {#1}_2, \ldots, {#1}_{#2} }}$
$\def \seqop#1#2#3{{ {#2}_1 #1 {#2}_2 #1 \cdots #1 {#2}_{#3} }}$

# Variance

The variance of a random variable $X$ is a measure of how much the values of $X$ deviate from its mean.

The variance of any random variable $X$, with finite mean $\E X$, is given by the following formula.

$$\large
	\Var x = \E{ ( X - \E{X} )^2 }
$$

> [!tip] Variance of a Distribution
> 
> The variance of a distribution is a measure of how much a distribution is concentrated around the mean: the smaller it is, the more concentrated the distribution is towards its center.

## Properties of the Variance

1. $\Var X = \E{X^2} - [\E X]^2$

2. $\Var X = 0 \Rightarrow \Var X = \E{X^2}$

3. $\Var X = 0 \Leftrightarrow \P{X = c} = 1$

4. $\Var{cX} = c^2 \Var X$

5. $\Var{X + c} = \Var X$

6. For any independent $\seq X n \Rightarrow$
$$\Var{\seqop +Xn} = \Var{X_1} + \Var{X_2} + \cdots \Var{X_n}$$


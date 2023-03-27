# Expectation

$\def\P#1{{ \mathbb{P} \left(#1\right) }}$
$\def\E#1{{ \mathbb{E} \left(#1\right) }}$
$\def\X#1{{ \mathbb{X} \left(#1\right) }}$
$\def\bb#1{{ \mathbb{#1} }}$
$\def\cal#1{{ \mathcal{#1} }}$
$\def\seq#1#2{{ #1_1, #1_2, \ldots, #1_#2 }}$
$\def\seqf#1#2#3{{ #1_1(#2_1), #1_2(#2_2), \ldots, #1_#3(#2_#3) }}$

For a [random variable](Probability/Random%20Variables/Random%20Variables.md) $X : \Omega \rightarrow S$, the *expectation* (*expected* or *mean* value) of $X$ si defined to be

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

## Properties of the Expectation


> [!note] 1. Non-negative RV
> 
> If $X \ge 0$ then $\E{X} \ge 0$, and $\E{X} = 0$ iff $\P{X = 0} = 1$

> [!note] 2. Multiplying by Constants
> 
> If $c \in \bb R$ is a constant, then $\E{c} = c$ and $\E{cX} = c\,\E{X}$

> [!note] 3. Sum of RV
> 
> For any random variables $X,Y$ it holds $\E{X+Y} = \E{X} + \E{Y}$

> [!tip] Linearity of Expectation
> By generalizing by induction properties 2 and 3, given any constants $c_1, c_2, \ldots, c_n$ and any random variables $X_1, X_2, \ldots, X_n$, it holds
> $$\large
> 	\E{ \sum_{k=1}^n c_k X_k }
> 	= \sum_{k=1}^n c_k \E{ X_k }
> $$

> [!note] 4. Function of RV
> 
> For any function $g : S \rightarrow S'$, $g(X) : \Omega \rightarrow S'$ is a random variable taking values in $S'$, and
> $$\large
> 	\E{ g(X) } = \sum_{x \in S} g(x) \P{X = x}
> $$

> [!note] 5. TK
> 
> If $X \ge 0$ takes integer values, then
> $$\large
> 	\E{X} = \sum_{k=1}^\infty \P{X \ge k}
> $$

> [!note] 6. Product of Independent RV
> 
> If $X,Y$ are two independent random variables, then $\E{XY} = \E{X}\E{Y}$.
> Generally, if $X_1, X_2, \ldots, X_n$ are independent random variables, then
> $$\large
> 	\E{X_1, X_2, \ldots, X_n} = \prod_{k=1}^n \E{X_k}
> $$

> [!note] 7. Independence of Functions of RV
> 
> If $X : \Omega \rightarrow S_X$ and $Y : \Omega \rightarrow S_Y$ are two independent random variables, and $f : S_X \rightarrow S'_X$ and $g : S_Y \rightarrow S'_Y$ are two functions, then $f(X)$ and $g(Y)$ are two independent random variables. Generally,
> $$\large
> 	\seq{X}{n} \text{ ind.}
> 	\Rightarrow \seqf{f}{X}{n}
> $$

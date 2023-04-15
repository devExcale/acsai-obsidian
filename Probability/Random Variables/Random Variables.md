$\def\bb#1{{ \mathbb{#1} }}$
$\def\bbP{{ \mathbb P }}$
$\def\bbId{{ \mathbb 1 }}$
$\def\calF{{ \mathcal F }}$
$\def\P#1{{ \bb{P} \left( {#1} \right) }}$
$\def\Pid#1#2{{ \bb{1}_{#1} \left( {#2} \right) }}$
$\def \seq#1#2{{ {#1}_1, {#1}_2, \ldots, {#1}_{#2} }}$
$\def \seqf#1#2#3{{ {#1}_1({#2}_1), {#1}_2({#2}_2), \ldots, {#1}_{#3}({#2}_{#3}) }}$

# Random Variables

**Random Variables** are functions of the outcome of an experiment.

A *random variable* on $(\Omega, \cal F)$ taking values in a discrete set $S$ is a function $X : \Omega \rightarrow S$.

> [!example]
> Toss two dice, then $\Omega = \set{ (i,j) : 1 \le i,j \le 6 }$.
> 
> Define $X(\omega) = X(i,j) = i+j$
> $\quad \Longrightarrow \quad$
> $X : \Omega \rightarrow \set{2, \ldots, 12}$
> 
> $X$ is the sum of the outcome of the two dice.

## Probability Distribution of a RV

Since $X$ takes values in a discrete set $S$, let

$$\large
	p_x = \P{X = x} \quad \forall x \in S.
$$

The collection $(p_x)_{x \in S}$ is referred to as the **[probability distribution](Probability/Random%20Variables/Probability%20Distributions.md#Probability%20Distributions) of $X$**.

> [!info] Distribution Notation
> If the distribution of $X$ is well known (e.g. [Bernoulli](Probability/Random%20Variables/Probability%20Distributions.md#Bernoulli%20Distribution)), then we can also write $X \sim Bernoulli(p)$.

The function $F_X : \bb R \rightarrow [0,1]$ given by

$$\large
	F_X(x) = \P{X \le x}
$$

is called **distribution function of $X$**.

> [!note] Properties of Distribution Function
> Note that:
> 1. $F_X$ is piecewise constant, non-decreasing, right-continuous
> 2. The jumps are given by the weights of the distribution
> 3. $\large \lim\limits_{x \rightarrow -\infty}{ F_X(x) } = 0$
> 4. $\large \lim\limits_{x \rightarrow +\infty}{ F_X(x) } = 1$

Knowing the probability distribution function $F_X$ is equivalent to knowing the collection of weights $(p_x)_{x \in S}$ such that $p_x = \P{X = x}$, hence it is equivalent to knowing the probability distribution of $X$.

## Independence of RV

Two random variables $X,Y$, taking values in $S_X,S_Y$ respectively, are said to be independent if

$$\large
	\P{X = x, Y = y} = \P{X = x} \P{Y = y}
	\quad \forall (x,y) \in S_X \times S_Y.
$$

In general, the random variables $X_1, X_2, \ldots, X_n$ taking values in $S_1, S_2, \ldots, S_n$ are said to be independent if

$$\large \displaylines{
	\P{X_1 = x_1, X_2 = x_2, \ldots, X_n = x_n}
	= \prod_{i=1}^n \P{X_i = x_i} \\
	\forall (x_1, x_2, \ldots, x_n) \in \bigtimes_{i=1}^n S_i.
}$$

> [!info] Sub-independence
> If $\sigma = \set{X_1, X_2, \ldots, X_n}$ is a set of independent random variables, then any subset $\sigma' \subseteq \sigma$ with $|\sigma'| \ge 2$ is a set of independent random variables.

Moreover, given any number of independent random variables $\seq X n$ and functions $\seq f n$ such that $f_i : S_i \rightarrow S_i'$, then the random variables $\seqf f X n$ are independent.

## Identity RV

For a given probability space $( \Omega, \calF, \bbP )$ and $A \in \calF$, define

$$\large
	\Pid{A}{\omega} = \cases{
		1 \quad \text{if } \omega \in A \\
		0 \quad \text{otherwise}
	}
$$

$\bbId_A : \Omega \rightarrow \set{0, 1}$ tells us whether the outcome is in $A$ or not.

> [!note] Properties of $\Pid{}{\omega}$
> 1. $\large \bbId_{A^c} = 1 - \bbId_A$
> 2. $\large \bbId_{A \cap B} = \bbId_A \bbId_B$
> 3. $\large \bbId_{A \cup B} = 1 - (1-\bbId_A) (1-\bbId_B)$

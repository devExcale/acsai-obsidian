# Probability Distributions

$\def\P#1{{ \mathbb{P} \left(#1\right) }}$
$\def\bb#1{{ \mathbb{#1} }}$
$\def\cal#1{{ \mathcal{#1} }}$

TK !uniform

A **probability distribution**, or simply *distribution*, is a [probability measure](/Probability/Discrete%20Probability/Probability%20Space.md#Probability%20Measure) $\bb{P}$ on some [sample space](/Probability/Discrete%20Probability/Probability%20Space.md#Sample%20Space) and [sigma algebra](?TK) $(\Omega, \cal{F})$.

> [!abstract] Discrete Distribution
> A probability distribution is called *discrete* if the sample space $\Omega$ is a discrete set.

A distribution defines a **weight** $p_\omega$ for each outcome, which can also be seen as the probability of that single outcome occurring; the sequence of weights $(p_\omega)_{\omega \in \Omega}$ uniquely defines $\bb{P}$.

$$\large
	p_\omega = \P{\set\omega}
$$


> [!note] Sum of weights
> Note that all the outcomes are disjoint between themselves and, by definition of probability measure $\P{\Omega} = 1$, hence
> 
> $$\large
> 	\P{\Omega} = \sum_{\omega \in \Omega} p_\omega = 1
> $$

## Bernoulli Distribution

Take $\Omega = \set{0,1}$ and define $\bb{P}$ to be the probability distribution given by the weights

$$\large
	p_0 = 1-p, \quad p_1 = p
$$

$\bb P$ is called **Bernoulli distribution of parameter $p$**, it is denoted by $Bernoulli(p)$.

> [!example] Biased Coin Toss
> 
> $\bb P$ models the number of *heads* obtained in one biased coin toss: *heads* with probability $p$ and *tails* with probability $1-p$.

## Geometric Distribution

Let $\Omega = \set{1,2,\ldots}$, define $\bb P$ to be the probability distribution given by the weights

$$\large
	p_k = (1-p)^{k-1} p, \quad k \ge 1.
$$

$\bb P$ is called **Geometric distribution of parameter $p$**, it is denoted by $Geometric(p)$.

> [!example] Biased Coin Tosses until Head
> 
> $\bb P$ models the number of biased coin tosses up to (and including) the first *head*; the weight $p_k$ indicates the probability of getting *tails* from the first toss to the $(k-1)^\text{th}$ and *head* at the $k^\text{th}$.

## Binomial Distribution

Fix an integer $N \ge 1$ and let $\Omega = \set{1,2,\ldots,N}$. Define $\bb P$ to be the probability distribution given by the weights

$$\large
	p_k = \binom{N}{k} p^k (1-p)^{N-k},
	\quad 0 \le k \le N.
$$

$\bb P$ is called **Binomial distribution of parameters $N, p$**, it is denoted by $Binomial(N,p)$.

> [!example] Biased Coin Tosses
> 
> $\bb P$ models the number of *heads* obtained in $N$ biased coin tosses; the weight $p_k$ indicates the probability of getting $k$ *heads*.

## Poisson Distribution

Let $\Omega = \bb N$, and for a fixed parameter $\lambda > 0$ let $\bb P$ be the probability distribution given by the weights

$$\large
	p_k = \frac{ e^{-\lambda} \lambda^k }{ k!}, \quad k \ge 0.
$$

$\bb P$ is called **Poisson distribution of parameter $\lambda$**, it is denoted by $Poisson(\lambda)$.

> [!tip]
> 
> This distribution arises as the limit of a [Binomial Distribution](#Binomial%20Distribution) with parameters $N, \frac{N}{\lambda}$ as $N \rightarrow \infty$.

> [!example]
> 
> *A small business receives, on average, 12 customers per day. What is the probability that the business will receive exactly 8 customers in day?*
> 
> The question models a **Poisson Distribution**, where:
> - the days are the basis for sampling, i.e. $N \rightarrow \infty$;
> - the average of customers is the parameter $\lambda$;
> - the exact number we're looking for is the parameter $k$.
> 
> $$\large
> 	\P{customers=8} =
> 	\frac{ e^{-\lambda} \lambda^k }{ k!} =
> 	\frac{ e^12 \lambda^8 }{ 8! } \approx
> 	0.065523
> $$

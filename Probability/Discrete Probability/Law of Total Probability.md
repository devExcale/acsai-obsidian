# Law of Total Probability

$\def\P#1{{ \mathbb{P} \left(#1\right) }}$
$\def\seq#1#2{{ \left( #1_#2 \right)_{#2 \ge 1} }}$

From [conditional probability](/Probability/Discrete%20Probability/Conditional%20Probability.md), it can be seen that the probability of two events happening simultaneously can be derived calculating two consecutive probabilities: the probability that $B$ occurs, then the probability that $A$ occurs given that $B$ has occurred.

$$\large
	\P{A \cap B} = \P{A|B} \P{B}
$$

The same formula applies to $A$ and $B^c$,

$$\large
	\P{A \cap B^c} = \P{A|B^c} \P{B^c}
$$

Then, since $B$ and $B^c$ are disjoint,

$$\large\begin{aligned}
	\P{A}
	&= \P{A \cap B} + \P{A \cap B^c} \\
	&= \P{A|B} \P{B} + \P{A|B^c} \P{B^c}
\end{aligned}$$


**Law of Total Probability**
---

Let $\seq{B}{n}$ be a sequence of disjoint events of positive probability, whose union is the sample space $\Omega$. Then, for all events $A$

$$\large
	\P{A} = \sum_{n \ge 1}{ \P{A|B_n} \P{B_n} }
$$
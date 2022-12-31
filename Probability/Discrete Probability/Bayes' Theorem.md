# Bayes' Theorem

$\def\P#1{{ \mathbb{P} \left(#1\right) }}$

From [conditional probability](/Probability/Discrete%20Probability/Conditional%20Probability.md), if $A,B$ are two events with positive probabilities, we have

$$\large
	\P{A \cap B} = \P{A|B} \P{B} = \P{B|A} \P{A}
$$

**Bayes' theorem** states how to reverse the conditioning, i.e. how compute $\P{A|B}$ from $\P{B|A}$:

$$\large
	\P{A|B} = \frac{ \P{B|A} \P{A} }{ \P{B} }
$$

> [!tip] Proof
> $$\large \begin{aligned}
> 	\P{A|B} &= \frac{ \P{A \cap B} }{ \P{B} } \\
> 	&= \frac{ \P{B|A} \P{A} }{ \P{B} }
> \end{aligned}$$

$\def \P#1{{ \mathbb{P} \left(#1\right) }}$

# Conditional Distribution

The conditional probability of a [random variable](/Probability/Random Variables/Random Variables.md) $X$, given an event $\set{Y = y}$ with positive probability, is defined to be the collection of probabilities

$$\large
	\P{X = x | Y = y} = \frac{ \P{X = x, Y = y} }{ \P{Y = y} }
	\quad \forall x \in S_X
$$

The marginal distributions can be recovered by the [total probability law](/Probability/Introduction/Total Probability Law.md).

$$\large
	\P{X = x} = \sum_{y \in S_Y} \P{X = x | Y = y} \P{Y = y}
$$

$$\large
	\P{Y = y} = \sum_{x \in S_X} \P{Y = y | X = x} \P{X = x}
$$

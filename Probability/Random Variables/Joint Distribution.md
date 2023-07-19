$\def \P#1{{ \mathbb{P} \left(#1\right) }}$

# Joint Distribution

Given two [random variables](/Probability/Random Variables/Random Variables.md) $X : \Omega \rightarrow S_X$ and $Y : \Omega \rightarrow S_Y$, their joint distribution is defined as the collection of probabilities

$$\large
	\P{X = x, Y = y} \quad \forall (x,y) \in S_X \times S_Y
$$

The marginal distributions can be recovered by the [total probability law](/Probability/Introduction/Total Probability Law.md).

$$\large
	\P{X = x} = \sum_{y \in S_Y} \P{X = x, Y = y}
$$

$$\large
	\P{Y = y} = \sum_{x \in S_X} \P{X = x, Y = y}
$$

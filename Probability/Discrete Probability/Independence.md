# Independence

%%
$\def\P#1{{ \mathbb{P} \left(#1\right) }}$
$\def\indep{{ \mathrel{\unicode{x2AEB}} }}$
%%

Independence is a property of two or more [events](/Probability/Discrete%20Probability/Probability%20Space.md#Events), it indicates whether the [probability](Probability/Discrete%20Probability/Probability%20Space.md#Probability%20Measure) of the events is influenced by one of the events happening first.

## Pairwise Independence

Two events $A,B$ are said to be *independent* if

$$\large
	\P{A \cap B} = \P{A}\P{B}
$$

It can be proven that, if $A \indep B$, then $A \indep B^c$, $A^c \indep B$ and $A^c \indep B^c$.

$$\large
	\P{A \cap B^c} = TK
$$

## General Independence

A notion of general independence can also be defined: $n$ events $A_1, A_2, \ldots, A_n$ are said to be independent if, for any $k \ge 2$ and any collection of distinct indices $1 \le i_1 < \cdots < i_k \le n$,

$$\large
	\P{ \bigcap_{i_k}{ A_{i_k} } } = \prod_{i_k}{ \P{ A_{i_k} }}
$$

> [!warning] General and Pairwise Independence
> If the $n$ events are independent, then every subset of the $n$ events must be independent. Beware, though, that the converse does not apply: if three events are all pairwise-independent, then the three events could and could not be independent.



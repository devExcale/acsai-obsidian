# Inclusion-Exclusion Formula

%%
$\def\P#1{{ \mathbb{P} \left(#1\right) }}$
$\def\bb#1{{ \mathbb{#1} }}$
$\def\cal#1{{ \mathcal{#1} }}$
%%

It is known that, for any two events $A, B$,

$$\large
	\P{A \cup B} = \P{A} + \P{B} - \P{A \cap B}
$$

For any 3 events,

$$\large\displaylines{
	\P{A \cup B \cup C} = \\
	\P{A} + \P{B} + \P{C}
	- \P{A \cap B} - \P{A \cap C} - \P{B \cap C}
	+ \P{A \cap B \cap C}
}$$

In general, for any $n$ events $A_1, A_2, \ldots, A_n$,

$$\large
	\P{ \bigcup_{i=1}^n A_i }
	= \sum_{k=1}^n{ (-1)^{k+1} }
	\sum_{ 1 \le i_1 < \cdots < i_k \le n }{ \P{ \bigcap_{i_k} A_{i_k}} }
$$
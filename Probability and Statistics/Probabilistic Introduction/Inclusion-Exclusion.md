$\def\P#1{{ \mathbb{P} \left({#1}\right) }}$
$\def \seq#1#2{{ {#1}_1, {#1}_2, \ldots, {#1}_{#2} }}$

# Inclusion-Exclusion

- For any two events $A,B$,

$$\large
	\P{A \cup B} = \P{A} + \P{B} - \P{A \cap B}
$$

- For any three events $A,B,C$,

$$\large
\begin{aligned}
	\P{A \cup B \cup C}
	&= \P{A} + \P{B} + \P{C} \\
	&- \P{A \cap B} - \P{A \cap C} - \P{B \cap C} \\
	&+ \P{A \cap B \cap C}
\end{aligned}
$$

- In general, for any $n$ events $\seq A n$,

$$\large
	\P{ \bigcup_{i=1}^n A_i }
	= \sum_{k=1}^n{ (-1)^{k+1} }
	\sum_{ 1 \le i_1 < \cdots < i_k \le n }{ \P{ \bigcap_{i_k} A_{i_k}} }
$$

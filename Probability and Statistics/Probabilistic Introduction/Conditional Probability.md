$\def\P#1{{ \mathbb{P} \left(#1\right) }}$
$\def\indep{{ \mathrel{\unicode{x2AEB}} }}$

# Conditional Probability

**Conditional Probability** is a concept closely related to [event](/Probability/Introduction/Probability Space.md#Events) [independence](Probability%20and%20Statistics/Probabilistic%20Introduction/Independence.md).

Let $A,B$ be two events with $\P{B}>0$. Then, the conditional probability of $A$ *given* $B$ is

$$\large
	\P{A|B} = \frac{ \P{A \cap B} }{ \P{B} }
$$

The interpretation of $\P{A|B}$ is the probability of the event $A$, knowing that the event $B$ occurred first.

> [!tip] Independent Events
> 
> If $A \indep B$,
> $$\large
> 	\P{A|B} = \frac{ \P{A \cap B} }{ \P{B} }
> 	= \frac{ \P{A}\P{B} }{ \P{B} }
> 	= \P{A}
> $$
> Indeed, if $A,B$ are independent, then $B$ occurring first shouldn't change the likelihood of $A$ happening.

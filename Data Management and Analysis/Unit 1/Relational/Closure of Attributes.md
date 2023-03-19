$\def \clj#1#2{{ #1_#2^+ }}$

# Closure of Attributes

The closure of a set of attributes $X$ with respect to $F$, denoted by $X^+$ or more explicitly $\clj X F$, is the set that contains every attribute $A$ determined by $X$, i.e.

$$\large
	\clj X F = \set{ A \st X \rightarrow A \in F^A }
$$

> [!tip] Trivial Dependency
> 
> By the reflexivity axiom, $X \rightarrow X \Rightarrow X \in \clj X F$

## Finding the Closure of Attributes

There exists an algorithm to find the closure of a set of attributes $X$.

> [!quote] Algorithm
> 
> $\text{Begin}$
> 
> $\quad \text{Let } Z = X$
> 
> $\quad \text{Let } S = \set{A \in V \mid Y \rightarrow V \in F \ \land \ Y \subseteq Z}$
> 
> $\quad \text{While } S \not\subseteq Z \text{ then:}$
> 
> $\quad \quad Z = Z \cup S$
> 
> $\quad \quad S = \set{A \in V \mid Y \rightarrow V \in F \ \land \ Y \subseteq Z}$
> 
> $\quad \text{Endwhile}$
> 
> $\text{End}$

The algorithm takes in input the set of attributes $X$, its closure at the end of the algorithm is given by the set $Z$.

The logic of the algorithm is to start with the attributes of $X$, and iteratively find attributes, contained in $S$, such that they're defined by transitive dependencies of $X$, i.e. (during an iteration) by a subset of the set $Z$. The algorithm stops when no more attributes are found (i.e. no more attributes are added to $S$, which means that after $Z = Z \cup S$ the loop will end).

## Checking Keys with Closure

The closure of a set of attributes $X$ can be used to determine if $X$ is a [key](/Data%20Management%20and%20Analysis/Unit%201/Relational/Functional%20Dependencies.md#Keys) of a relation:

1. if the closure $X^+$ equals to $R$, then $X \rightarrow R$ and $X$ is a **superkey**;
1. if there's no proper subset $X' \subset X$ such that $X' \rightarrow R$, then $X$ is a **candidate key**.

> [!tip] Tip
> 
> If one or more attributes aren't functionally determined (i.e. don't appear on the right side of any functional dependency), then they must be part of a key.
> 
> This can help reduce the set of all possible keys to check.


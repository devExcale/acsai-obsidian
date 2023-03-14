# Closure of Functional Dependencies

A legal instance $r$ of $R$ is ensured to satisfy all the [functional dependencies](/Data%20Management%20and%20Analysis/Unit%201/Relational/Functional%20Dependencies.md) in $F$, but it could satisfy additional functional dependencies that aren't included in $F$.

> [!note] Closure of $F$
> 
> The set of all functional dependencies satisfied by **each legal** instance of $R$, even the ones not in $F$, is called the **closure of $F$**, which is denoted by $F^+$.

> [!tip] $F \subseteq F^+$
> 
> Because $F^+$ contains every functional dependency satisfied by legal instances of $R$, then $F^+$ must satisfy every functional dependency contained in $F$, i.e.
> 
> $$\large
> 	XY \in F^+ \quad
> 	\forall XY \in F
> 	\Rightarrow
> 	F \subseteq F^+
> $$

## Trivial Functional Dependencies

Given two subsets $X, Y$ such that $Y \subset X \subseteq R$, every legal instance $r$ of $R$ must satisfy the (so called) **trivial functional dependency** $X \rightarrow Y$.

Even if not defined, trivial functional dependencies are satisfied by any relation, hence if $Y \subset X$ then $X \rightarrow Y \in F^+$.
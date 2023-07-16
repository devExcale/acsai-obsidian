$\def \clj#1{{ #1^+ }}$
$\def \clj#1#2{{ #1_#2^+ }}$

# Closure of Functional Dependencies

A legal instance $r$ of $R$ is ensured to satisfy all the [functional dependencies](/Data Management and Analysis/Unit 1/Relational/Functional Dependencies.md) in $F$, but it could satisfy additional functional dependencies that aren't included in $F$.

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

## Equivalence of Functional Dependencies

Two sets of functional dependencies are said to be equivalent ($F \equiv G$) if their closures are the same, i.e. $F^+ = G^+$.

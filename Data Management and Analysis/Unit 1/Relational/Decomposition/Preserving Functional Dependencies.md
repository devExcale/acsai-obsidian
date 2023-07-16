$\def \clj#1{{ #1^+ }}$
$\def \clj#1#2{{ #1_#2^+ }}$

# Preserving the Functional Dependencies

A decomposition $\rho = R_1, R_2, \cdots, R_n$ is said to preserve $F$ if the set of functional dependencies $F$ and a decomposition $G$ are equivalent, i.e.

$$\large
	F \equiv G = \bigcup_{i=1}^n \pi_{R_i}(F)
$$

where $\pi_{R_i}(F) = \set{X \rightarrow Y \in F^+ \mid XY \subseteq R_i}$.

## Checking Equivalence

To check that $F \equiv G$ (i.e. $F^+ = G^+$), it could also be checked that $F^+ \supseteq G^+$ and $F^+ \subseteq G^+$.

> [!question] $F^+ \supseteq G^+$
> 
> By the definition of the [decomposition](/Data Management and Analysis/Unit 1/Relational/Decomposition/Decomposition of Relations.md), it follows that $F \supseteq G$, so naturally $F^+ \supseteq G^+$.

> [!question] $F^+ \subseteq G^+$
> 
> Assume that $F \subseteq G^+$, then
> 
> 1. any $f \in F$ could be found by applying Armstrong's Axioms to some $g\in G^+$;
> 2. any $f' \in F^+$ could be found by applying Armstrong's Axioms to some $f \in F^+$.

By the previous statements, given a set of functional dependencies $F$ and a decomposition $G$, it can be checked that the two are equivalent if $F \subseteq G^+$, otherwise they're not equivalent.

$G^+$ is exponentially hard to compute, but:

1. $F \subseteq G^+ \Leftrightarrow f \in G^+ \quad \forall f \in F$
2. $X \rightarrow Y \in G^+ \Leftrightarrow Y \subseteq \clj X G$

Hence, if $F \subseteq G^+$, then $Y \subseteq \clj X G$ $\forall X \rightarrow Y \in G^+$ and the two sets of functional dependencies are equivalent. Conversely, if a functional dependency can be found such that $Y \nsubseteq \clj X G$, then $F \not\equiv G$.

## Computing $\clj X G$

Given a decomposition $\rho = R_1, R_2, \cdots, R_n$, the closure $\clj X G$ can be computed using the following algorithm, where the final result is stored in the variable $Z$.

> [!quote] Algorithm: $\clj X G$
> 
> $\text{Begin}$
> 
> $\quad \text{Let } Z = X$
> 
> $\quad \text{Let } S = \bigcup_{i=1}^n \clj{(Z \cap R_i)}{G} \cap R_i$
> 
> $\quad \text{While } S \not\subset Z \text{ then:}$
> 
> $\quad \quad Z = Z \cup S$
> 
> $\quad \quad S = \bigcup_{i=1}^n \clj{(Z \cap R_i)}{G} \cap R_i$
> 
> $\quad \text{Endwhile}$
> 
> $\text{End}$

The algorithm iteratively computes the union of the closures of $X$ w.r.t. every sub-relation $R_i$, until no more attributes in the closure can be found (i.e. the closure is complete). The closure of $X$ is computed w.r.t. $F$, so intersecting at every iteration with $R_i$ makes sure to eliminate every original dependency not included in $G$.

$\def \clj#1#2{{ {#1}_{#2}^+ }}$

# Minimal Cover

A minimal cover of a set $F$ of [functional dependencies](/Data%20Management%20and%20Analysis/Unit%201/Relational/Functional%20Dependencies.md) is an equivalent set $G$ of functional dependencies such that some of the original ones are *reduced* or *removed*. Minimal covers are the starting point to compute a preserving-lossless [decomposition](/Data%20Management%20and%20Analysis/Unit%201/Relational/Decomposition/Decomposition%20of%20Relations.md).

Formally, a minimal cover of a set $F$ of functional dependencies is an equivalent set $G$ such that

1. $|Y| = 1 \quad \forall X \rightarrow Y \in G$
2. $\nexists X' \subset X : G \equiv (G \setminus \set{X \rightarrow A}) \cup \set{X' \rightarrow A} \quad \forall X \rightarrow A \in G$
3. $\nexists X \rightarrow A \in G : G \equiv G \setminus \set{X \rightarrow A}$

or, verbally,

1. all dependants are singletons;
2. all determinants are not redundant (determinants can't be reduced);
3. all dependencies are not redundant (dependencies can't be removed).

> [!info] Existence of Minimal Covers
> 
> For any set of functional dependencies, there could exist more than one minimal cover (all equivalent), but at least one minimal cover is guaranteed to exist (which could be the set itself, if it is already in minimal cover form).

## Minimal Cover Algorithm

There exists an algorithm to find a minimal cover:

1. **Decouple dependants**

Decompose all dependencies $X \rightarrow Y$ with $|Y| > 1$, using the *decomposition rule*, into the dependencies $X \rightarrow A : A \in Y$.

2. **Reduce redundant determinants**

Try to reduce any dependency $X \rightarrow A \in F$ into a dependency $X' \rightarrow A \in F^+: X' \subset X$. In other words, check if $A \in \clj{(X')}{F}$.

If a $X' \subset X$ can be found such that $A \in \clj{(X')}{F}$, then $X \rightarrow A$ can be reduced (replaced) to $X' \rightarrow A$, otherwise it can't be reduced.

> [!tip]
> 
> First of all, check if there exists any couple of dependencies $X \rightarrow A, B \rightarrow A \in F$ such that $B \in X$. If such a couple exists, then $X \rightarrow A$ can be removed because $A$ is determined by a subset of $X$, i.e. $X \rightarrow A$ is redundant.

> [!tip]
> 
> TK Closures don't need to be computed again for every step, but closures persist thru the step (determinants are being reduced in such a way that doesn't alter the closure of $G$)

3. **Remove redundant dependencies**

Try to remove any dependency $X \rightarrow A$ such that $G \equiv G \setminus \set{X \rightarrow A}$.

If, for any $X \rightarrow A$, $A \in \clj{X}{G \setminus \set{X \rightarrow A}}$, then the dependency can be removed because it is redundant (i.e. $X$ determines $A$ through other transitive dependencies), otherwise it can't be removed.

> [!tip]
> 
> If, for a dependency $X \rightarrow A$, there are no other dependencies such that $A$ is determined or is a determinant, then the dependency can't be removed, because then $A$ wouldn't be determined anymore.

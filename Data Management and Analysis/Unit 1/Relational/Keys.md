# Keys

A key is a subset of attributes $K \subseteq R$ such that every tuple instance of $K$ [**uniquely determines**](/Data Management and Analysis/Unit 1/Relational/Functional Dependencies.md) every tuple of a relation $R$.

> [!example] Example
>
> | ID      | Name       | Surname   | DateOfBirth | ... |
> | ------- | ---------- | --------- | ----------- | --- |
> | **200** | *Emanuele* | *Scaccia* | 11/05/2002  | ... |
> | **146** | *Mario*    | *Rossi*   | 11/05/2002  | ... |
>
> In this case, by imposing [unique](/Data Management and Analysis/Unit 1/Database/Constraints.md#Uniqueness constraints) on $\set\text{Name, Surname}$, both
> - $\set\text{ID} \rightarrow R$
> - $\set\text{Name, Surname} \rightarrow R$
> 
> are candidate keys of $R$, while $\set\text{ID, Name, Surname} \rightarrow R$ is a superkey.

## Types of Keys

There are three types of keys, ordered in a hierarchy.

### Superkey

A superkey is a set of attributes $K \in R$ such that every instance of $K$ uniquely determines every instance of the relation $R$.  Using functional dependencies, the definition can be written as follows.

$$\large
	K \rightarrow R \in F^+
$$

### Candidate Key

A candidate key (or minimal superkey) is a [superkey](#Superkey) that can't both be reduced to a subset of itself and be a key.

$$\large
	K \rightarrow R \in F^+
	\quad \land \quad
	\nexists K' \subset K
	\text{ s.t. }
	K' \rightarrow R
$$

### Primary Key

A primary key is chosen [candidate key](#Candidate Key). In a relation where there are multiple valid candidate keys, one is picked to consistently identity all the tuples.

## Uniqueness Test

There exists a test to check whether there exists only one key in a relation.

Let $F$ be a set of functional dependencies on a relation $R$, define

$$\large
\displaylines{
	X = R \setminus \bigcup
	\set{ W \setminus V \mid V \rightarrow W \in F} \\
	\text{or} \\
	X = \bigcap \set{R \setminus (W \setminus V)
	\mid V \rightarrow W \in F}
}
$$

i.e. the set of all attributes that aren't explicitly determined by any functional dependency in $F$.

- If $X \rightarrow R$, then there is one candidate key only;
- there are multiple candidate keys otherwise.

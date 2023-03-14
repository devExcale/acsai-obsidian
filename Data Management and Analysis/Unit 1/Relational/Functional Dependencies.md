# Functional Dependencies

Given a relation schema $R$, a *functional dependency* on $R$ is an ordered pair of non-empty subsets $X,Y \in R$, with notation $X \rightarrow Y$ (sometimes $XY$), such that

$$\large
	t_1[X] = t_2[X] \Rightarrow t_1[Y] = t_2[Y]
	\quad\quad \forall t_1, t_2 \in r
$$

where $r$ is an instance of $R$.

> [!example] Example
> If two tuples have the same matriculation number (so they refer to the same student), then they must also contain the same name and surname.
> 
> | ID      | Name       | Surname   | ... | Grade |
> | ------- | ---------- | --------- | --- | ----- |
> | **200** | *Emanuele* | *Scaccia* | ... | 28    |
> | **146** | *Mario*    | *Rossi*   | ... | 30    |
> | **200** | *Emanuele* | *Scaccia* | ... | 29    |
> 
> In this case, $\set\text{ID} \rightarrow \set{ \text{Name}, \text{Surname} }$.

- The set of all functional dependencies defined on $R$ is called $F$ ;
- $r$ is said to be legal if it satisfies all the functional dependencies in $F$.

> [!tip] Constraints
> Functional dependencies are another way to express some types of [constraints](/Data%20Management%20and%20Analysis/Unit%201/Database/Constraints.md).

## Armstrong's Axioms

Armstrong's axioms define new functional dependencies from the ones that already exist.

The three axioms are:

- reflexivity axiom;
- augmentation axiom;
- transitivity.

Moreover, three additional rules can be derived from the axioms:

- union rule;
- decomposition rule;
- pseudo-transitivity rule.

By iteratively applying the axioms and rules to $F$, a new set of functional dependencies $F^A$ can be constructed, which will contain additional functional dependencies that were not contained in $F$.

> [!tip] Closure of $F$
> 
> When $F^A$ is complete and no other functional dependencies can be found, then $F^A$ is equal to the [closure](/Data%20Management%20and%20Analysis/Unit%201/Relational/Closure%20of%20Functional%20Dependencies.md) of $F$.


> [!note] Reflexivity Axiom
> 
> *All functional dependencies $X \rightarrow Y$, defined for every $Y \subset X$, belong to $F^A$.*
> 
> $$\large
> 	X \rightarrow Y \in F^A
> 	\quad \quad
> 	\forall Y \subset X
> $$

> [!note] Augmentation Axiom
> 
> *All functional dependencies $XZ \rightarrow YZ$, defined for every $X \rightarrow Y \in F$, belong to $F^A$.*
> 
> $$\large
> 	XZ \rightarrow YZ \in F^A
> 	\quad \quad
> 	\forall X \rightarrow Y \in F,\ Z \in R
> $$

> [!note] Transitivity Axiom
> 
> *All functional dependencies $X \rightarrow Z$, defined for every couple $X \rightarrow Y, Y \rightarrow Z \in F$, belong to $F^A$.*
> 
> $$\large
> 	X \rightarrow Z \in F^A
> 	\quad \quad
> 	\forall X \rightarrow Y,\ Y \rightarrow Z \in F
> $$

> [!note] Union Rule
> 
> *All functional dependencies $X \rightarrow YZ$, defined for every couple $X \rightarrow Y, X \rightarrow Z \in F$, belong to $F^A$.*
> 
> $$\large
> 	X \rightarrow YZ \in F^A
> 	\quad \quad
> 	\forall X \rightarrow Y,\ X \rightarrow Z \in F
> $$

> [!note] Decomposition Rule
> 
> *All functional dependencies $X \rightarrow Z$, defined for every $Z \subset Y \text{ s.t. } X \rightarrow Y \in F$, belong to $F^A$.*
> 
> $$\large
> 	X \rightarrow Z \in F^A
> 	\quad \quad
> 	\forall Z \subset Y \text{ s.t. } X \rightarrow Y \in F
> $$

> [!note] Pseudo-transitivity Rule
> 
> *All functional dependencies $XW \rightarrow Z$, defined for every couple $X \rightarrow Y, WY \rightarrow Z \in F$, belong to $F^A$.*
> 
> $$\large
> 	WX \rightarrow Z \in F^A
> 	\quad \quad
> 	\forall X \rightarrow Y,\ WY \rightarrow Z \in F
> $$

## Keys

Given a relation schema $R$ and a set of functional dependencies $F$ defined on $R$, a subset $K \subseteq R$ is a key of $R$ if:

1. $K \rightarrow R \in F^+$
2. There is no proper subset $K' \subset K$ such that $K' \rightarrow R$

If condition 2. isn't satisfied, but the subset $K$ determines $R$, then $K$ is said to be a **superkey**.

A relation can have multiple distinct keys, usually in a [database](/Data%20Management%20and%20Analysis/Unit%201/Database/Databases.md) just one is chosen as a **primary key**.

> [!example] Example
>
> | ID      | Name       | Surname   | DateOfBirth | ... |
> | ------- | ---------- | --------- | ----------- | --- |
> | **200** | *Emanuele* | *Scaccia* | 11/05/2002  | ... |
> | **146** | *Mario*    | *Rossi*   | 11/05/2002  | ... |
>
> In this case, by imposing unique on $\{ \text{Name}, \text{Surname} \}$ both
> - $\{ \text{ID}\} \rightarrow R$
> - $\{ \text{Name}, \text{Surname} \} \rightarrow R$
> 
> are keys of $R$.

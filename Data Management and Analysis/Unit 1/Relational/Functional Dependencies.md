# Functional Dependencies

Given a relation schema $R$, a *functional dependency* on $R$ is an ordered pair of non-empty subsets $X,Y \in R$, with notation $X \rightarrow Y$ (sometimes $XY$), such that

$$\large
	\forall t_1, t_2 \in r :
	t_1[X] = t_2[X] \Rightarrow t_1[Y] = t_2[Y]
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
> In this case, $\{ \text{ID} \} \rightarrow \{ \text{Name}, \text{Surname} \}$.

> [!info] Constraints
> Functional dependencies are just another type of [constraint](/Data%20Management%20and%20Analysis/Unit%201/Database/Constraints.md).

The set of all functional dependencies defined on $R$ is called $F$; $r$ is said to be legal if it satisfies all the functional dependencies in $F$.

## Closure of F

A legal instance $r$ of $R$ satisfies all the functional dependencies in $F$, but it could have additional functional dependencies that are not included in $F$.

The set of all functional dependencies satisfied by **each legal** instance of $R$, even the ones not in $F$, is called the **closure of $F$** (denoted by $F^+$).

> [!note] Note
> Note that $F \subseteq F^+$, because $F^+$ contains every functional dependency satisfied by legal instances of $R$, which by definition satisfy every functional dependency in $F$. This implies that every functional dependency in $F$ is contained in $F^+$.

> [!tip] Trivial Functional Dependencies
> Given two subsets $X, Y$ such that $Y \subset X \subseteq R$, we have that every legal instance $r$ of $R$ must satisfy the (so called) **trivial functional dependency** $X \rightarrow Y$.
> 
> Even if not defined, trivial functional dependencies are satisfied by any relation, hence if $Y \subset X$ then $X \rightarrow Y \in F^+$.

## Armstrong's Axioms

Let $F^A$ be a set of functional dependencies defined on $R$, such that $F \subseteq F^A$. Using **Armstrong's Axioms**, we can build $F^A$.

TK

### Reflexivity Axiom

$$\large
	Y \subset X \in R
	\Longrightarrow X
	\rightarrow Y \in F^A
$$

### Augmentation Axiom

$$\large
	X \rightarrow Y \in F^A
	\Longrightarrow
	XZ \rightarrow YZ \in F^A \quad \forall Z \in R
$$

### Transitivity Axiom

$$\large
	X \rightarrow Y, \ \ Y \rightarrow Z \in F^A
	\Longrightarrow
	X \rightarrow Z \in F^A
$$

### Union Rule

$$\large
	X \rightarrow Y, \ \ X \rightarrow Z \in F^A
	\Longrightarrow
	X \rightarrow YZ \in F^A
$$

### Decomposition Rule

$$\large
	X \rightarrow Y \in F^A \ \ \text{and} \ \ Z \subset Y
	\Longrightarrow
	X \rightarrow Z \in F^A
$$

### Pseudotransitivity Rule

$$\large
	X \rightarrow Y, \ \ WY \rightarrow Z \in F^A
	\Longrightarrow
	WX \rightarrow Z \in F^A
$$

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

# Relational Algebra

**Relational algebra** is a mathematical notation to query the contents of [relation](/Data%20Management%20and%20Analysis/Unit%201/Relational/Relational%20Model.md#Relation). Languages like [SQL](?) are founded on relational algebra.

It is a formal language to interrogate a relational database, consisting of a set of unary and binary operators that, if applied to one or two relation instances (sets of tuples), generate a new relation instance.

TK: logical operators

The operators are:
- [Projection](#Projection)
- [Selection](#Selection)
- [Union](#Union)
- [Difference](#Difference)
- [Intersection](#Intersection)
- [Cartesian Product](#Cartesian%20Product)
- [Join](#Join)
- Renaming

## Projection

It is a unary operator. A projection performs a *vertical cut* on a relation, selecting a subset of the relation's attributes.

It is represented by the symbol $\large\pi$.

Let $R(X)$ be a relation, where $X = \{A_1, \cdots, A_n\}$ . Then $\pi_Y(R)$ where $Y \subseteq X$ is a projection of R. The result of the operation will be a set with all the tuples of the operand, but the tuples will contains only the attributes specified by $Y$.

$\text{Customer}$

| Name    | Code  | Town   |
| ------- | --- | ------ |
| Rossi   | C1  | Roma   |
| Rossi   | C2  | Milano |
| Rossi   | C3  | Roma   |
| Bianchi | C4  | Roma   |
| Verdi   | C5  | Roma   |

$\pi_\text{Name}(\text{Customer})$

| Name    |
| ------- |
| Rossi   |
| Bianchi |
| Verdi   |

$\pi_\text{Name, Code}(\text{Customer})$

| Name    | Code  |
| ------- | --- |
| Rossi   | C1  |
| Rossi   | C2  |
| Rossi   | C3  |
| Bianchi | C4  |
| Verdi   | C5  |

> [!warning] Duplicates
> Note how there aren't duplicates in the resulting table, because every table is actually a set of tuples.

## Selection

It is a unary operator. A selection performs a *horizontal cut* on the relation, that is, it selects a subset including all the tuples that meet some constraint(s).

It is represented by $\sigma$.

Let $R(X)$ be a relation.
<br>
Then $\sigma_C(R) \subseteq R,$ where $C$ is a boolean condition. $C$ must be in form $A\ \theta\ B$ or $A\ \theta\ a$, where:
- $A, B$ are attributes of the same domain ($dom(A) = dom(B)$)
- $a$ is a literal (constant) belonging to the domain of A ($a \in dom(A)$)
- $\theta$ is a comparison operator ($\theta \in \{=, \lt, \gt, \leq, \geq \}$)

Multiple conditions can be joined using logical operators ($\lor, \land, \lnot$).

$\text{Customer}$

| Name    | Code  | Town   |
| ------- | --- | ------ |
| Rossi   | C1  | Roma   |
| Rossi   | C2  | Milano |
| Rossi   | C3  | Roma   |
| Bianchi | C4  | Roma   |
| Verdi   | C5  | Roma   |

$\sigma_\text{Town='Roma'}(\text{Customer})$

| Name    | Code  | Town |
| ------- | --- | ---- |
| Rossi   | C1  | Roma |
| Rossi   | C3  | Roma |
| Bianchi | C4  | Roma |
| Verdi   | C5  | Roma |

$\sigma_{ \text{Town='Roma'} \land \text{Name='Rossi'} }(\text{Customer})$

| Name    | Code  | Town |
| ------- | --- | ---- |
| Rossi   | C1  | Roma |
| Rossi   | C3  | Roma |

## Union

It is a binary commutative operator. A union creates a new relation instance containing all the tuples belonging to at least one of the of the operands. The two operands must be compatible.

It is represented by the symbol $\cup$.

Let $R_1(X),\ R_2(Y)$ be two relations such that $X = Y$.
<br>
Then $R = R_1 \cup R_2 = R_2 \cup R_1$ such that $R \supseteq R_1, R_2$.

$\text{Teachers}$

| Name    | Code | Department |
| ------- | ---- | ---------- |
| Rossi   | D1   | Math       |
| Rossi   | D2   | Italian    |
| Bianchi | D3   | Math       |
| Verdi   | D4   | English    |

$\text{Admins}$

| Name     | Code | Department |
| -------- | ---- | ---------- |
| Esposito | A1   | English    |
| Riccio   | A2   | Math       |
| Pierro   | A3   | Italian    |
| Verdi    | A4   | English    |
| Bianchi  | A5   | English    |

$\text{AllStaff} = \text{Teachers} \cup \text{Admins}$

| Name     | Code | Department |
| -------- | ---- | ---------- |
| Rossi    | D1   | Math       |
| Rossi    | D2   | Italian    |
| Bianchi  | D3   | Math       |
| Verdi    | D4   | English    |
| Esposito | A1   | English    |
| Riccio   | A2   | Math       |
| Pierro   | A3   | Italian    |
| Verdi    | A4   | English    |
| Bianchi  | A5   | English    |

> [!warning] Duplicates
> The resulting table is always a set, so it **must not** contain any duplicate tuple. Duplicate ones will be discarded!

$\text{Teachers}$

| Name    | Code | Department |
| ------- | ---- | ---------- |
| Rossi   | D1   | Math       |
| Rossi   | D2   | Italian    |
| Bianchi | D3   | Math       |
| Verdi   | D4   | English    |

$\text{Admins}$

| Name     | Code | Department | Salary |
| -------- | ---- | ---------- | ------ |
| Esposito | A1   | English    | 1250   |
| Riccio   | A2   | Math       | 2000   |
| Pierro   | A3   | Italian    | 1000   |

$\text{AllStaff} = \text{Teachers} \cup \pi_{\text{Name, Code, Department}}(\text{Admins})$

| Name     | Code | Department |
| -------- | ---- | ---------- |
| Rossi    | D1   | Math       |
| Rossi    | D2   | Italian    |
| Bianchi  | D3   | Math       |
| Verdi    | D4   | English    |
| Esposito | A1   | English    |
| Riccio   | A2   | Math       |
| Pierro   | A3   | Italian    |

## Difference

It is a binary operator. A difference creates a new relation instance containing all the tuples of the first operand that are **not** in the second operand. The two operands must be compatible.

It is represented by the symbol $-$.

Let $R_1(X),\ R_2(Y)$ be two relations such that $X = Y$.
<br>
Then $R_1 - R_2 = \{ t : t \in R_1 \land t \notin R_2\}$

$\text{Students}$

| Name    | TaxCode | Department |
| ------- | ------- | ---------- |
| Rossi   | C1      | Math       |
| Rossi   | C1      | Italian    |
| Bianchi | C3      | Math       |
| Verdi   | C4      | English    |

$\text{Admins}$

| Name     | TaxCode | Department |
| -------- | ------- | ---------- |
| Esposito | C5      | Italian    |
| Riccio   | C6      | Math       |
| Pierro   | C7      | English    |
| Bianchi  | C3      | Math       |

$\text{Students} - \text{Admins}$

| Name    | TaxCode | Department |
| ------- | ------- | ---------- |
| Rossi   | C1      | Math       |
| Rossi   | C1      | Italian    |
| Verdi   | C4      | English    |

$\text{Admins} - \text{Students}$

| Name     | TaxCode | Department |
| -------- | ------- | ---------- |
| Esposito | C5      | Italian    |
| Riccio   | C6      | Math       |
| Pierro   | C7      | English    |

## Intersection

It is a binary commutative operator. An intersection creates a new relation instance containing all the tuples that are both in operands. The two operands must be compatible.

It is represented by the symbol $\cap$.

Let $R_1(X),\ R_2(Y)$ be two relations such that $X = Y$.
<br>
Then $R_1 \cap R_2 = \{ t : t \in R_1, R_2\} = R_1 - (R_1 - R_2)$

$\text{Students}$

| Name    | TaxCode | Department |
| ------- | ------- | ---------- |
| Rossi   | C1      | Math       |
| Rossi   | C1      | Italian    |
| Bianchi | C3      | Math       |
| Verdi   | C4      | English    |

$\text{Admins}$

| Name     | TaxCode | Department |
| -------- | ------- | ---------- |
| Esposito | C5      | Italian    |
| Riccio   | C6      | Math       |
| Pierro   | C7      | English    |
| Bianchi  | C3      | Math       |

$\text{Students} \cap \text{Admins} = \text{Admins} \cap \text{Students}$

| Name     | TaxCode | Department |
| -------- | ------- | ---------- |
| Bianchi  | C3      | Math       |

## Cartesian Product

It is a binary commutative operator. A cartesian product creates a relation with tuples obtained by combining all the tuples in the first operand with all the tuples in the second operand. It is usually used when the information needed is partitioned in multiple tables.

It is represented by the symbol $\times$.

$\text{Customer}$

| Name    | Code | Town   |
| ------- | ---- | ------ |
| Rossi   | C1   | Roma   |
| Rossi   | C2   | Milano |
| Bianchi | C3   | Roma   |
| Verdi   | C4   | Roma   |

$\text{Order}$

| Code | A   | Pieces |
| ---- | --- | ------ |
| C1   | A1  | 100    |
| C2   | A2  | 200    |
| C3   | A2  | 150    |
| C4   | A3  | 200    |
| C1   | A2  | 200    |
| C1   | A3  | 100    |

To list every customer with their orders we can use the cross product. A cross product will result in all combinations of all tuples, so we have to filter the resulting set to match the codes using the [selection](#Selection) operator. But to do this, we have to be able to distinguish between `Code of Customer` and `Code of Order`, we can use the [renaming](#Renaming) operator. In the end, we project only the attributes we want, ignoring duplicates.

$$\large
\pi_\text{Name, Code, Town, A, Pieces}(
	\sigma_\text{Code = OCode} (
		\text{Customer} \times \rho_{\text{OCode} \gets \text{Code}}(
			\text{Order}
		)
	)
)
$$

| Name    | Code | Town   | A   | Pieces |
| ------- | ---- | ------ | --- | ------ |
| Rossi   | C1   | Roma   | A1  | 100    |
| Rossi   | C1   | Roma   | A2  | 200    |
| Rossi   | C1   | Roma   | A3  | 100    |
| Rossi   | C2   | Milano | A2  | 200    |
| Bianchi | C3   | Roma   | A2  | 150    |
| Verdi   | C4   | Roma   | A3  | 200    |

## Join

A **natural join** performs a [cartesian product](#Cartesian%20Product) of two relations $R_1(X), R_2(Y)$ and selects only some tuples that satisfy the condition $R_1[A_1] = R_2[A_1] \land R_1[A_2] = R_2[A_2] \land \cdots \land R_1[A_k] = R_2[A_k]$ where $A_1, \cdots, A_k \in X, Y$ are the attributes the two relations have in common.

It is represented by the symbol $\Join$.

$$\large R_1 \Join R_2 = \pi_{X \cup Y}( \sigma_C( R_1 \times R_2 ) )$$

The attributes $A_1, \cdots, A_k$ in the condition must have the same name to perform a join on it.

$\text{Customer}$

| Name    | Code | Town   |
| ------- | ---- | ------ |
| Rossi   | C1   | Roma   |
| Rossi   | C2   | Milano |
| Bianchi | C3   | Roma   |
| Verdi   | C4   | Roma   |

$\text{Order}$

| Code | A   | Pieces |
| ---- | --- | ------ |
| C1   | A1  | 100    |
| C2   | A2  | 200    |
| C3   | A2  | 150    |
| C4   | A3  | 200    |
| C1   | A2  | 200    |
| C1   | A3  | 100    |

$\text{Customer} \Join \text{Order}$

| Name    | Code | Town   | A   | Pieces |
| ------- | ---- | ------ | --- | ------ |
| Rossi   | C1   | Roma   | A1  | 100    |
| Rossi   | C1   | Roma   | A2  | 200    |
| Rossi   | C1   | Roma   | A3  | 100    |
| Rossi   | C2   | Milano | A2  | 200    |
| Bianchi | C3   | Roma   | A2  | 150    |
| Verdi   | C4   | Roma   | A3  | 200    |

*Note* if two relations have no attributes in common, the join condition cannot be evaluated and the operation will default to a normal cartesian product!

Another type of join is the **theta join**, which is the same as the natural join but with customizable condition: it selects the tuples resulting from the cartesian product of two relations that satisfy the condition $A \theta B$, where:
- $\theta$ is a comparison operator ($\theta \in \{ =, \lt, \gt, \le, \ge \}$)
- $A, B$ are two attributes attributes of the first and second relations respectively
- $dom(A) = dom(B)$

$$\large R_1 \Join R_2 = \sigma_{A \theta B}(R_1 \times R_2)$$


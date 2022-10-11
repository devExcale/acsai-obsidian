# Relational Algebra

**Relational algebra** is a mathematical notation to query the contents of [relation](/Data%20Management%20and%20Analysis/Unit%201/Relational%20Model.md#Relation). Languages like [SQL](?) are founded on relational algebra.

It is a formal language to interrogate a relational database, consisting of a set of unary and binary operators that, if applied to one or two relation instances (sets of tuples), generate a new relation instance.

The operators are:
- [Projection](#Projection)
- [Selection](#Selection)
- [Union](#Union)
- [Difference](#Difference)
- [Intersection](#Intersection)
- Cartesian Product
- Join
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

*Note* that there aren't duplicates in the resulting table, because it is actually a set.

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

*Note:* the resulting table is always a set, so it **must not** contain any duplicate tuple (duplicate ones will be discarded).

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
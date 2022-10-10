# Databases

[//]: # (TODO: intro)

## Schemas

Databases use files to store data, but hide this fact implementing an abstraction layer that facilitate storage and manipulation of [data](/Data%20Management%20and%20Analysis/Unit%201/Information%20Systems.md#Information%20vs%20Data).

### External Schema

It's the outer layer of a database, the one a normal user interacts with. It is a portion of the database, with structure equal to or similar (**views**)

## Constraints

**Integrity constraints** are properties that must be satisfied by every instance of the [relation](/Data%20Management%20and%20Analysis/Unit%201/Relational%20Model.md#Relation)/database. A database instance is *correct* if it satisfies *every* constraint associated with its schema.

There are two categories of constraints:
- **intra-relational:** defined on the domain of a single attribute, on the values of the same tuple or on tuples of the same relation;
- **inter-relational:** defined between multiple relations.

### Domain constraints

Defined on the domain of an attribute, bounds the domain to a subset of itself.

*Examples:*
-  `YEAR_BIRTH > 1980`
- `(GRADE >= 18) AND (GRADE <= 31)`

The **value existence** constraint is a special type of domain constraint, it forbids the use of [NULL values](/Data%20Management%20and%20Analysis/Unit%201/Relational%20Model.md#Null%20values).
- `GRADE NOT NULL`

### Tuple constraints

Defined on the values of the same tuple, bounds the possible combinations the tuple can assume.

*Examples:*
-  `(GRADE = 31) OR NOT (HONOUR = true)`

### Uniqueness constraints

Defined on an attribute, it makes it so that when a tuple's specified attribute assumes a value, any other tuple can't assume the same value under the same attribute.

*Examples:*
-  `USER_ID UNIQUE`

### Primary key constraint

It is a shorthand to include both [uniqueness constraint](#Uniqueness%20constraints) and [value existence constraint](#Domain%20constraints), based on the concept of [key](/Data%20Management%20and%20Analysis/Unit%201/Relational%20Model.md#Keys).

### Referential constraint

Also called *[foreign key](/Data%20Management%20and%20Analysis/Unit%201/Relational%20Model.md#Keys) constraint*. It is defined on a domain of an attribute, it makes it so that the domain of an attribute $A$ of a relation $R$ is the set of all values assumed by an attribute $A'$ of an instance on a relation $R'$.

*Examples:*
-  `DEPT REFERENCES DEPARTMENT.NUMBER`

	$A = \texttt{DEPT},\ R' = \texttt{DEPARTMENT},\ A' = \texttt{NUMBER}$

A referential integrity constraint between the $X$ attributes of a relation $R$ and another relation $R'$ forces the values on $X$ in $R$ to appear as values of the [primary key](/Data%20Management%20and%20Analysis/Unit%201/Relational%20Model.md#Keys) of $R$.

---

By allowing [null values](/Data%20Management%20and%20Analysis/Unit%201/Relational%20Model.md#Null%20values), some constrains can be made less restrictive (e.g. uniqueness).

It is possible to define certain behaviours to mitigate violations of constraints, e.g. what to do when a tuple referenced by another tuple (foreign key) is removed.
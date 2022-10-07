# Relational Model

The **Relational Model** is a a mathematical data model proposed by *Edgar Codd* in 1970. Information is represented by values stored into **records** (or tuples), which are grouped into uniform **tables**.

The whole model is based on the notion of **relationship**. Relations in math help to give a way of establishing a connection between any two objects or things. A relation describes the relationship between two objects that are usually represented as an ordered pair (a, b), in this case the objects are the records.

Another important notion is the **domain**: a (possibly infinite) [set](/Linear%20Algebra/Sets.md) of values (e.g. all the integers, strings of length 5, $\{0, 1\}$).

In the relational model:
- a **relation** is any [subset](Linear%20Algebra/Sets.md#Subsets) of the Cartesian product of one or more domains;
- a relation that is a subset of the Cartesian product of $k$ domains is said to be of **degree** $k$;
- the number of tuples of a relation is called **cardinality**;
- the tuples of a relation are all *distinct*, as a relation is a set.

*example:* The following is a relation with a tuple of 4 elements with the specified domain.

| String | String  | Integer | Real |
| ------ | ------- | ------- | ---- |
| Mario  | Bianchi | 10      | 28.5 |
| Paolo  | Rossi   | 2       | 26.5 |



## Relational Algebra


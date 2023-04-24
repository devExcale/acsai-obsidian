# Relational Model

The **Relational Model** is a a mathematical [data](/Data%20Management%20and%20Analysis/Unit%201/Data.md) model proposed by *Edgar Codd* in 1970. Information is represented by values stored into **records** (or tuples), which are grouped into uniform **tables**.

The whole model is based on the notion of **relationship**. Relations in math help to give a way of establishing a connection between any two objects or things. A relation describes the relationship between two objects that are usually represented as an ordered pair (a, b), in this case the objects are the records.

In the relational model:
- the **domain** is a (possibly infinite) [set](/Linear%20Algebra/Sets.md) of values (e.g. all integers, strings of length 5, $\{0, 1\}$);
- a **relation** is any [subset](/Linear%20Algebra/Sets.md#Subsets) of the Cartesian product of one or more domains;
- a relation that is a subset of the Cartesian product of $k$ domains is said to be of **degree** $k$;
- the number of tuples of a relation is called **cardinality**;
- the tuples of a relation are all *distinct*, as a relation is a set.

A relation can be regarded as a table in which:
- each **row** is a *distinct* tuple that represent an instance of information;
- each **column** corresponds to a component of information and contains homogeneous values (same domain).

> [!example] Context to Information
> 
> The following table is a relation with two tuples of 4 elements with the specified domain, but it provides no information: there's no context.
> 
> | String | String  | Integer | Real |
> | ------ | ------- | ------- | ---- |
> | Mario  | Bianchi | 10      | 28.5 |
> | Paolo  | Rossi   | 2       | 26.5 |

## Relation

A relation has a fixed structure:
- the *columns* must each have a unique, self-explanatory name within a table, called **attribute name**;
- the pair (column name, column domain) is called **attribute**, which represents a piece of information;
- the set of all attributes of a relation is called [relational schema](/Data%20Management%20and%20Analysis/Unit%201/Database/Schemas.md).

If a relation $R$ has attributes $A_1, \ldots, A_k$, then the schema is represented as $R(A_1, \ldots, A_k)$ or $R = A_1, \ldots, A_k$ .

> [!note] Aspects
> In a relation we can define two properties:
> - **intentional aspect,** the schema of a relation should remain *unchanged over time*, because it describes its structure;
> - **extensional aspect,** values in a relation (instance of a relation) can change, and change very quickly.

Tuples between relations can be linked: references between data in different relations are represented by values that are included in the tuples. This whole behaviour is defined with [foreign keys](?).

> [!note] Tuples
> Every tuple $t$ of an instance of a relation $R$ can be seen as a function that associates each attribute $A_i$ to a value $t[A_i] \in dom(A_i)$.

### Null values

**NULL** values represent lack of information or the fact that the information is not applicable (e.g. phone number).

Null does not belong to any domain, but it can be used as a *wildcard* to replace values in **any** domain. Be aware, though, that two null values are always considered different, even on the same domain.

### Accessing attributes

The components of a relation are indicated by the names rather than their position: $t[A_i]$ indicates the value of the attribute with name $A_i$ of the tuple $t$.

If $Y$ is a subset of attributes of the schema $X$ of a relation $(Y \subseteq X)$ then $t_Y = (t[y_1], \cdots, t[y_i]) \text{ s.t. } y_i \in Y$ is the tuple composed only of the values of $t$ that correspond to the attributes contained in $Y$. $t_Y$ is also called a **restriction** of $t$.

### Keys

There is a method to uniquely identify the tuples of an instance of a relation: keys. A **relation key** is one or more subsets of attributes that uniquely identify a tuple; it can be used to reference tuples from a different relation (**foreign key**).

A subset $X$ of attributes of a relation $R$ is a key of $R$ iff:
1. for each instance of $R$, there do not exist two distinct tuples $t_1,\ t_2$ such that the two tuples have the same values for all attributes of $X$, i.e.
$$\large t_1[a] \neq t_2[a] \quad \forall a \in X$$
2. there does not exist a proper subset of $X$ satisfying condition 1.

A relation could have several alternative keys (valid subsets of attributes), usually the best choice would be most used one or the one composed of a smaller number of attributes (**primary key**). A primary key *does not* allow for [null values](#Null%20values).

There always is at least one key in every relation, because there can't be identical tuples (in this case, the key is the whole set of attributes).

# Schemas

A schema is the base structure of relations and databases, it defines what types of data are stored.

There are two types of schemas: the **internal schema**, the one databases use to store data on files (unknown to the end user), and the **external schema**, the outer layer of databases (the one end users use).

## External Schema

It's the outer layer of a database, the one a normal user interacts with; it is a portion of the database which is coincident to [relations](Data%20Management%20and%20Analysis/Unit%201/Relational/Relational%20Model.md#Relation), it is also called **relation schema**.

> [!abstract] Notation
> - $R = \{A_1, A_2, \ldots, A_n\}$
> - The first letters of the alphabet $A, B, \ldots$ denote single attributes
> - The last letters of the alphabet $X, Y, \ldots$ denote subsets of attributes
> - If $X, Y$ denote two set of attributes, then $XY$ defines the union of the two

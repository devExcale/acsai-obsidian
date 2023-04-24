# Sets

A set is a collection of homogeneous elements, with no order and every elements is unique in the set. A set can have finite or infinite elements.

## Defining a set

#### Roster Notation

The literal elements are separated by comma:
$$ \large \{ 1, 2, 3, 4 \} $$

We can also include infinite elements with three dots like this (all numbers from 1 to infinity):
$$ \large \{ 1, 2 ,3, \cdots \} $$

Or, to include a large number of sequential elements (all numbers from 1 to 100):
$$ \large \{ 1, 2, \cdots, 99, 100 \} $$

#### Semantic Notation

A sentence is used to describe the elements:
$$ \large \text{Let S be the set of whole numbers from 1 to 4} $$

#### Builder Notation

A special syntax is used to generate elements, or to "select" them from another set:
$$ \large \{ n \in \mathbb{R} \mid 1 \le n \le 4 \} $$
The first part is the "generator function", which takes one or more values and gives back an element; the second part is the condition for selection. The vertical bar means "such that".

***Ex.*** | Defining the set of rational numbers $\mathbb{Q}$

$$ \large \mathbb{Q} = \{ \frac{a}{b} \mid b \ne 0 \quad a,b \in \mathbb{Z}\} $$

## Properties of Sets

#### Membership

If a Set $S$ contains an element $x$, it is said that element *belongs* to $S$.
$$ \large x \in S $$

On the contrary, if $x$ isn't an element of $S$, it is said that element *doesn't belong to $S$*.
$$ \large x \notin S $$

***Ex.*** | Membership relative to the set of integer numbers $\mathbb{Z}$

$$ \large
2 \in \mathbb{Z} \quad
2.5 \notin \mathbb{Z} $$

#### Subsets

If $A$ and $B$ are two sets and every elements in $A$ is in $B$, then $A$ is a *subset* of $B$.

$$ \large A \subseteq B $$

On the other hand, it is said that $B$ is a *superset* of $A$, because it contains every element of $A$.

$$ \large B \supseteq A $$

If $A$ is a subset of $B$, then $A = B$ could be true, because every set includes every its own element in itself. The same can be said for the superset.
If this is not expected behaviour, we can define the proper subset and superset:

$$ \large \begin{gather}
A \subseteq B,\ A \neq B \rightarrow A \subset B \\
B \supseteq A,\ A \neq B \rightarrow B \supset A
\end{gather} $$

***Ex.*** | Relationship between the naturals set $\mathbb{N}$, the integers set $\mathbb{Z}$ and the reals set $\mathbb{R}$:

$$ \large \mathbb{N} \subset \mathbb{Z} \subset \mathbb{R}$$


## Set Operations

#### Union

Two sets can be joined, the new set contains all the members of both $A$ and $B$, repeted once.

$$ \large A \ \cup \ B = C $$

***Ex.*** | Union examples

$$ \large \begin{align}
\{1,2\} \ \cup \ \{3,4\} &= \{1,2,3,4\} \\
\{1,2\} \ \cup \ \{2,3\} &= \{1,2,3\} \\
\end{align} $$

#### Intersection

The intersection of two sets is a new set with the elements $A$ and $B$ have in common. If there are no elements in common, an empty set is returned.

$$ \large A \ \cap \ B = C $$

***Ex.*** | Intersection examples

$$ \large \begin{align}
\{1,2,3\} \ \cup \ \{2,3,4\} &= \{2,3\} \\
\{1,2,3\} \ \cup \ \{4,5,6\} &= \varnothing \\
\end{align} $$

#### Cartesian Product

The cartesian product of two sets $A$ and $B$ is the set of all ordered pairs $(a,b)$ such that $a$ is a member of $A$ and $b$ is a member of $B$.

$$ \large A \times B = \{ (a,b) \mid a \in A,\ b \in B \} $$

***Ex.*** | Cartesian Product example

$$ \large \{x_1, x_2\} \times \{y_1, y_2\}
= \{(x_1, y_1), (x_1, y_2), (x_2, y_1), (x_2, y_2)\} $$

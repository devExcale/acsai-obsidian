# Sets
---

A set is a collection of omogeneous elements, with no order and every elements is unique in the set. A set can have finite or infinite elements.


## Defining a set

#### Roster Notation

The literal elements are separated by comma:
$$ \large \{ 1, 2, 3, 4 \} $$

We can also write infinite elements with three dots like this (all numbers from 1 to infinity):
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


## Set Properties

#### Membership

If a Set $S$ contains an element $x$, it is said that element *belongs* to $S$.
$$ \large x \in S $$

On the contrary, if $x$ isn't an element of $S$, it is said that element *doesn't belong to $S$*.
$$ \large x \notin S $$
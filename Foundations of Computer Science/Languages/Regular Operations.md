# Regular Operations

A regular operation on a [language](Foundations%20of%20Computer%20Science/Languages/Languages.md) $L$ is an operation on one or two strings $w$ such that applying the operation on all strings $w \in L$ results in a [regular language](Foundations%20of%20Computer%20Science/Languages/Languages.md#Regular%20Languages). *(TK one or more languages)*

## List of Regular Operations

### Union

The union operation, denoted as $A \cup B$ for two languages $A$ and $B$, results in a new language that combines the elements of both languages. The union of two languages consists of all the strings that belong to either language $A$ or language $B$ (or to both).

$$\large
	A \cup B = \set{x \mid x \in A \lor x \in B}
$$

### Concatenation

Concatenation is a language operation, denoted as $A \circ B$ for two languages $A$ and $B$, results in a new language that contains all possible strings formed by taking one string from $A$ and attaching it to a string from $B$.

$$\large
	A \circ B = \set{xy \mid x \in A \land y \in B}
$$

### Kleene Star

The Kleene star, denoted as $A^*$ for a language $A$, is a regular language operation that represents the closure or repetition of the language $A$. It results in a new language consisting of all possible strings that can be formed by concatenating zero or more strings from $A$.

$$\large
	A^* = \set{
		x_1 x_2 \ldots x_n
		\mid
		n \geq 0 \land x_i \in A
	}
$$

> [!info] Empty string
> 
> The empty string $\varepsilon$ is a valid result of the star operation, i.e. $\varepsilon \in A^*$.

### Kleene Plus

The Kleene plus, denoted as $A^+$ for a language $A$, is a regular language operation that represents the positive closure or repetition of the language $A$. It results in a new language consisting of all possible strings that can be formed by concatenating one or more strings from $A$.

$$\large
	A^+ = \set{
		x_1 x_2 \ldots x_n
		\mid 
		n \geq 1 \land x_i \in A
	}
$$

> [!tip] Alternative representation
> 
> The plus operations could be represented using the star operator: $A^+ = AA^*$. The RHS makes sure that there is at least one string from $A$.

# Strings

An **alphabet** $\Sigma$ is any non-empty set, whose elements are called **symbols**, or **characters**, of the alphabet. A **string** $w$ over an alphabet $\Sigma$ is a finite sequence of symbols from $\Sigma$.

## Properties of Strings

> [!note] Length of a String
> 
> The length of a string $w$, written as $|w|$, is the number of symbols that it contains. A string of length zero (no characters) is called the **empty string**, written as $\varepsilon$.

> [!note] Reverse of a String
> 
> The reverse of a string $w$, written as $w^R$, is the string obtained by writing $w$ in the opposite order.

> [!note] Substring of a String
> 
> A string $z$ is a substring of another string $w$ is $z$ appears consecutively (with no breaks) within $w$.

#### Concatenation

The concatenation of two strings $x$ and $y$, written as $xy$, is the string obtained by appending $y$ to the end of $x$.

The notation $w^k$ is used to represent the concatenation of $w$ with itself $k$ times. ($k \in \mathbb N$)

> [!example] Self-concatenation
> 
> $w^0 = \varepsilon, w^1 = w, w^2 = ww, w^3 = www, \ldots$

#### Prefix

A string $x$ is a **prefix** of $y$ if there exists a string $z$ such that $xz = y$.

Moreover, $x$ is said to be a **proper prefix** of $y$ if, in addition, $x \neq y$; which implies $z \neq \varepsilon$,

#### Suffix

A string $x$ is a **suffix** of $y$ if there exists a string $z$ such that $zx = y$.

Moreover, $x$ is said to be a **proper suffix** of $y$ if, in addition, $x \neq y$; which implies $z \neq \varepsilon$,
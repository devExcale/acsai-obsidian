# Combinatorial Analysis

To compute the probability in a probability space with equally likely outcomes, it is important to know the number of outcomes included in an event.

## Multiplication Rule

Take $N$ finite sets $\Omega_1, \Omega_2, \ldots, \Omega_N$ with cardinalities $|\Omega_k| = n_k$. How many ways are there to pick exactly one element from each set?

Logically, there are $n_1$ choices from the first set. Chosen the first element, there are other $n_2$ choices from the second set, leading to $|\Omega_1 \times \Omega_2| = n_1 n_2$. The same logic can then be applied iteratively to the other sets, giving the so called **multiplication rule**:

$$\large
	| \Omega_1 \times \Omega_2 \times \ldots \times \Omega_N |
	= n_1 n_2 \ldots n_N
$$

## Permutations

A permutation of a set is a bijection from the set to another ordering of the same set. How many permutations are there for a set of cardinality $n$?

There are $n$ possible elements for the first choice, then $n-1$ possible elements for the second choice (because one has been selected as first choice), $n-2$ possible elements for the third choice and so on. So, by the multiplication rule,

$$\large
	n (n-1) (n-2) \cdots 1 = n!
$$

Hence, there are $n!$ different orderings, or permutations, for a set of $n$ elements. Equivalently, there are $n!$ different bijections from any set of length $n$ to another set of the same length.

## Subsets

How many ways there are to choose $k$ elements from a set of $n$ elements? Remember that when choosing elements, one could care for the order in which the elements are being chosen or not.

### Subsets with Ordering

A formula can be obtained using the same logic as the permutations: there are $n$ possibile elements for the first choice, $n-1$ possibile elements for the second choice, until we get to the $k^{th}$ choice with $n-(k-1) = n-k+1$ possible elements.

$$\large
	n (n-1) \cdots (n-k+1) = \frac{ n! }{ (n-k)! }
$$

### Subsets without Ordering

To count how many ways there are to choose $k$ unordered elements from $n$, one could first choose $k$ ordered elements and then forget about the ordering.

There are $\frac{n!}{(n-k)!}$ ways to choose $k$ ordered elements from $n$, and we know there are $k!$ permutations (orderings) for these elements. Hence,

$$\large
	\binom{n}{k} = \frac{ n! }{ k! (n-k)! }
$$

> [!info] Binomial Coefficient
> The notation $\binom{n}{k}$ is called **binomial coefficient**, and it is read $n$ *choose* $k$. Literally, it indicates the number of possibile ways there are to choose $k$ unordered elements from $n$ elements.

Moreover, a more general question can be posed: how many ways there are to partition $n$ elements into unordered groups of sizes $n_1, n_2, \ldots, n_k$ (with $\sum{n_i} = n$)?

$$\large
	\binom{n}{n_1 \quad n_2 \quad \ldots \quad n_k}
	= \frac{ n! }{ n_1! n_2! \cdots n_k!}
$$

> [!info] Multinomial Coefficient
> The notation TK is called **multinomial coefficient**, it is read the same as the binomial coefficient.

> [!note] Choosing and Partitioning
> $$
> \frac{ n! }{ k! (n-k)! }
> = \binom{n}{k}
> = \binom{n}{n-k}
> = \binom{n}{ k \quad n-k }
> $$
> In fact, choosing $k$ unordered elements from $n$ is the same as choosing the remaining $n-k$, which is the same as partitioning $n$ elements into two groups of sizes $k$ and $n-k$.

## Subsets with Repetition

How many ways there are to choose $k$ elements from a set of $n$ elements, allowing repetitions?

### Subsets with Repetition and Ordering

Simply, there are $n$ possibilities for the first choice, $n$ possibilities for the second and so on,

$$\large
	\underbrace{n \cdot n \cdots n}_{k \text{ times}} = n^k
$$

### Subsets with Repetition without Ordering

TK

$$\large
	\binom{n+k-1}{k} = \frac{ (n+k-1)! }{ k! (n-1)! }
$$

## Combinatorics Formulas

| **Multiplication Rule**                                        | **Permutations** |
| -------------------------------------------------------------- | ---------------- |
| $\lvert \bigtimes_{k=1}^N \Omega_k \rvert = \prod_{k=1}^N n_k$ | $n!$             |

| **Subsets**      | `Ordering`              | `No ordering `                                      |
| ---------------- | ----------------------- | --------------------------------------------------- |
| `No repetitions` | $\frac{ n! }{ (n-k)! }$ | $\binom{n}{k} = \frac{ n! }{ k! (n-k)! }$           |
| `Repetitions`    | $n^k$                   | $\binom{n+k-1}{k} = \frac{ (n+k-1)! }{ k! (n-1)! }$ |

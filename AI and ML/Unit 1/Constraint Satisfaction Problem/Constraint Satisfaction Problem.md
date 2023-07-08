$\def \seq#1#2{{ {#1}_1, {#1}_2, \ldots, {#1}_{#2} }}$

# Constraint Satisfaction Problem

A Constraint Satisfaction Problem (CSP) is a computational problem defined by variables, their domains, and some constraints that must the variables must satisfy. Solving a CSP involves finding values for the variables that satisfy all the given constraints.

A CSP can be defined as a tuple with three components: variables, domains, constraints.

$$\large
	\text{csp} = (\mathcal X, D, \mathcal C)
$$

Solving a constraint satisfaction problem typically involves using algorithms and techniques, such as backtracking, constraint propagation and search heuristics to efficiently explore the search space and find a valid solution or determine that no solution exists.

## Variable

Variables represent the unknowns or decision variables in the problem, each variable has a specific role and represents an aspect of the problem that needs to be determined or assigned a value.

> [!example] Sudoku
> 
> In sudoku, a variable is a single cell that contains a number (both solved and unsolved).

A variable $X_i$ is a symbol which can take value $v_i \in D_i$, $D_i$ being the set of possible values that $v_i$ can take.

$$\large
	\mathcal X := \set{\seq X n}
$$

## Domain

A domain defines the allowable values for a variable, which can either be discrete or continuous (both non-dense and dense).

$$\large
	D := \set{\seq D n}
$$

Domains don't need to be homogeneous between themselves and aren't limited to numerical values only, but they could also be sets of symbols.

> [!example] Sudoku
> 
> In sudoku, the domains of all variables (the cells) are the same, i.e. $\set {1,2,\ldots,9}$.

## Constraints

Constraints represent the restrictions or relationships among the variables. They define the conditions that must be satisfied for a valid solution of the problem.

$$\large
	\mathcal C := \set{\seq C m}
$$

Constraints can be unary (involving a single variable), binary (relating two variables), or higher-order (involving more than two variables). A constraint $C_k$ is defined as follows.

$$\large
\begin{aligned}
	C_k
	&= (Y_k, R_k) \\
	&= \langle
		\set{X_1, X_2},
		\set{(3,1), (3,2), (2,1)}
	\rangle \\
	&= \langle
		\set{X_1, X_2},
		\set{X_1 > X_2}
	\rangle
\end{aligned}
$$

- $Y_k \subseteq \mathcal X$ is the set that contains the attributes involved in the constraint, it is called *scope*; 

- $R_k \subseteq \bigtimes_{D_i \in Y_k} D_i$ is the set of all tuples of values that attributes in $Y_k$ can assume at the same time, it is called *relation*. It is the actual constraint that defines the problem to solve.

Constraints can be:

- **unary,** involving a single variable;
- **binary,** relating two variables;
- **global,** or *higher-order*, involving more than two variables.

> [!example] Sudoku
> 
> In sudoku, the most obvious constraints are:
> - all cells in a row must be different;
> - all cells in a column must be different;
> - all cells in a box must be different.

If a CSP contains no global constraints (i.e. unary and binary only), then it is called a *binary CSP*. Some global constraints can be decomposed into multiple binary ones, but not all of them.

> [!example] Sudoku
> 
> Apparently, the main constraints of a sudoku may seem global (involving 9 variables), but they can be decomposed into multiple binary constraints: every combination of two cells in a row, column or box must be different.
> 
> Another constraint may be the already initialized cells: we can either restrict their domain to respective value or put a constraint on the variable that they must be equal to their value (latter is a unary constraint).
> 
> If considering these constraints only, then a sudoku may be considered a binary CSP.
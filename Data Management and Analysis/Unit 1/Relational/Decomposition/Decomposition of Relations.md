# Decomposition of Relations

If a relations isn't in [3rd normal form](/Data Management and Analysis/Unit 1/Relational/Third Normal Form.md), there is always be a way to decompose $R$ into a collection $\rho$ (called a *decomposition*) of subsets $R_1, R_2, \cdots, R_n$ such that

- $R = \bigcup_{i=1}^n R_i$;
- every subschema $R_i$ is in 3NF;
- all [functional dependencies](/Data Management and Analysis/Unit 1/Relational/Functional Dependencies.md) are preserved;
- the [natural join](/Data Management and Analysis/Unit 1/Relational/Relational Algebra.md#Join) of all $R_i$ should return the original instance of $R$ (*lossless join*).

> [!info] Projecting Functional Dependencies and Relation Instances
> 
> By decomposing a schema, we are projecting each functional dependency (and relation instance) over the set of attributes defined by each subschema.
> 
> $$\large
> \begin{aligned}
> 	F_i &= \pi_{R_i}(F) \\
> 	r_i &= \pi_{R_i}(r)
> \end{aligned}
> $$

1. [Preserving functional dependencies](/Data Management and Analysis/Unit 1/Relational/Decomposition/Preserving Functional Dependencies.md)
2. [Lossless Join](/Data Management and Analysis/Unit 1/Relational/Decomposition/Lossless Join.md)

## Finding a Decomposition

1. Compute a [minimal cover](/Data Management and Analysis/Unit 1/Relational/Decomposition/Minimal Cover.md) $G$ of $F$, set $\rho = \emptyset$ ;

2. If there are any, set all attributes $X$ which do not appear in any dependency as a first sub-relation ($\rho = \set X$) and discard them from $R$ ($R' = R \setminus X$);

3. If there is a dependency in $G$ such that all attributes in $R'$ are in the dependency, then add $R'$ as a sub-relation ($\rho = \rho \cup \set{R'}$);

4. Otherwise, for each $X \rightarrow A \in G$ add $XA$ as a sub-relation ($\rho = \rho \cup \set{XA}$);

5. If the decomposition doesn't have a lossless join, then add a key as a sub-schema ($\rho = \rho \cup \set K$).

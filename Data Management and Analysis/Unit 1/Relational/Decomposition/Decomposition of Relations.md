# Decomposition of Relations

If a relations isn't in [3rd normal form](/Data%20Management%20and%20Analysis/Unit%201/Relational/Third%20Normal%20Form.md), there is always be a way to decompose $R$ into a collection $\rho$ (called a *decomposition*) of subsets $R_1, R_2, \cdots, R_n$ such that

- $R = \bigcup_{i=1}^n R_i$;
- every subschema $R_i$ is in 3NF;
- all [functional dependencies](/Data%20Management%20and%20Analysis/Unit%201/Relational/Functional%20Dependencies.md) are preserved;
- the [natural join](/Data%20Management%20and%20Analysis/Unit%201/Relational/Relational%20Algebra.md#Join) of all $R_i$ should return the original instance of $R$ (*lossless join*).

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

1. [Preserving functional dependencies](/Data%20Management%20and%20Analysis/Unit%201/Relational/Decomposition/Preserving%20Functional%20Dependencies.md)
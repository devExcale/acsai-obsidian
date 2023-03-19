# Decomposition of Relations

If a relations isn't in [3rd normal form](/Data%20Management%20and%20Analysis/Unit%201/Relational/Third%20Normal%20Form.md), there is always be a way to decompose $R$ into a collection $\rho$ (called a *decomposition*) of subsets $R_1, R_2, \cdots, R_n$ such that

- $R = \bigcup_{i=1}^n R_i$;
- every subschema $R_i$ is in 3NF;
- all functional dependencies are preserved;
- the natural join of all $R_i$ should return the original instance of $R$.

A decomposition $\rho = R_1, R_2, \cdots, R_n$ is said to preserve $F$ if

$$\large
	F \equiv G = \bigcup_{i=1}^n \pi_{R_i}(F)
$$

where $\pi_{R_i}(F) = \set{X \rightarrow Y \in F^+ \mid XY \subseteq R_i}$.

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
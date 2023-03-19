# Third Normal Form

The third normal form (shortened as **3NF**) of a [schema](/Data%20Management%20and%20Analysis/Unit%201/Database/Schemas.md) is a property that ensures that no [anomalies](/Data%20Management%20and%20Analysis/Unit%201/Database/Schema%20Anomalies.md) can occur in the schema.

> [!quote] Interpretation of 3NF
> 
> Given a schema $R$ and a set of functional dependencies $F$, $R$ is in 3NF iff there are neither *partial dependencies* nor *transitive dependencies* in $F$.

A schema is said to be in 3NF if, for all [functional dependencies](/Data%20Management%20and%20Analysis/Unit%201/Relational/Functional%20Dependencies.md) $X \rightarrow A$ such that $A \notin X$:

- either $A$ belongs to a [key](/Data%20Management%20and%20Analysis/Unit%201/Relational/Functional%20Dependencies.md#Keys) ($A$ is also called **prime**);
- or $X$ contains a key ($X$ is also said **superkey**).

> [!tip] $A \notin X$
> 
> The condition $A \notin X$ is present ignore some trivial functional dependencies in $F^+$ to which the 3NF can't possibly be applied.
> 
> For example, given $R = \set{A,B}$ and $F = \set{A \rightarrow B}$, the functional dependency $B \rightarrow B$ **doesn't respect** the criteria for 3NF: $B$ isn't neither prime nor superkey, even though $R$ could be considered in 3NF.

> [!example] Example: 3NF
> 
> TK.

> [!example] Example: not 3NF
> 
> TK

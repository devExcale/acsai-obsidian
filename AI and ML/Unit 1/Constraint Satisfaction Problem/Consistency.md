# Consistency

Consistency is an important concept in CSP that refers to the property of assignments satisfying the constraints imposed by the problem. It ensures that the assigned values adhere to the defined relationships and constraints among the variables.

In a CSP, consistency can be evaluated at different levels:

1. **Node consistency,** involving one node;
2. **Arc consistency,** involving two nodes;
3. **Path consistency,** involving three nodes;
4. **$k$-consistency,** which involves $k$ nodes.

> [!note] $k$-consistency
> 
> $k$-consistency is a generalization of consistency on $k$ nodes, all the previous consistency properties are specific cases of $k$-consistency.

By enforcing consistency in a CSP, we reduce the search space and improve the efficiency of finding valid solutions. It allows us to make informed decisions during the search process, prune inconsistent assignments early, and guide the search towards more promising areas of the solution space.

Various algorithms, such as backtracking with constraint propagation or arc consistency algorithms like AC-3, can be employed to enforce consistency and solve CSPs efficiently. The choice of consistency level depends on the complexity of the problem and the desired trade-off between computational cost and solution optimality.

## Node Consistency

Node consistency ensures that the values assigned to a single variable satisfy the constraints associated with that variable. In other words, it ensures that the assigned value is consistent with the unary constraints specific to that variable.

## Arc Consistency

Arc consistency extends node consistency to consider binary constraints between pairs of variables. It ensures that for every pair of variables connected by a constraint, each value in the domain of one variable has a compatible value in the domain of the other variable. By enforcing arc consistency, we reduce the search space and eliminate inconsistent assignments early on.

Given two variables $X_i, X_j \in \mathcal X$, $X_i$ is said to be **arc-consistent** w.r.t $X_j$ iff

1. for every value in $D_i$
2. there exists some value in $D_j$
3. such that all binary constraints on $(X_i, X_j)$ are satisfied.

A variable $X_i \in \mathcal X$ is said to be **arc-consistent** iff

1. for every binary constraint $C \in \mathcal C$ with space $(X_i, X_j)$
2. and every value in $D_i$
3. there exists some value in $D_j$
4. such that $C$ is satisfied.

Looking at another perspective, it could also be said that a variable is said to be arc-consistent if is it is arc-consistent w.r.t. every variable.

---

*Python implementation of the AC-3 algorithm, that checks whether a node is arc-consistent.*

```python
def ac3(csp):
    queue = []
    for arc in csp.get_all_arcs():
        queue.append(arc)

    while queue:
        arc = queue.pop(0)
        if revise(csp, arc):
            if len(csp.get_domain(arc[0])) == 0:
	            # Inconsistent assignment
                return False

            # Add neighboring arcs to the queue
            for neighbor in csp.get_neighbors(arc[0]):
                if neighbor != arc[1]:
                    queue.append((neighbor, arc[0]))

    # Consistent assignment
    return True


def revise(csp, arc):
    revised = False
    for value in csp.get_domain(arc[0]):
        if not any(satisfies_constraint(value, assignment[arc[1]]) for assignment in csp.get_consistent_assignments(arc)):
            csp.remove_value_from_domain(arc[0], value)
            revised = True

    return revised
```

## Path Consistency

Path consistency goes beyond arc consistency and considers the transitive closure of binary constraints. It ensures that if a constraint exists between variable A and B, and a constraint exists between variable B and C, then there must exist a consistent assignment for the variables A, B, and C. Path consistency is more powerful than arc consistency and helps in pruning inconsistent assignments.

Given three variables $X_i, X_j, X_k \in \mathcal X$, $X_i$ and $X_k$ are said to be **path-consistent** w.r.t $X_j$ iff

1. for every assignment $\set{X_i = v_i, X_k = v_k}$ with $(v_i, v_k) \in D_i \times D_k$
2. that is consistent with every binary constraint with space $(X_i, X_k)$
3. there exists some assignment $X_j = v_j$ with $v_j \in D_j$
4. such that all binary constraints on $(X_i, X_j)$ and $(X_k, X_j)$ are satisfied.

## Global Consistency (also known as Constraint Propagation)

Global consistency refers to a higher level of consistency that considers all the constraints in the problem. It ensures that the assigned values satisfy all the constraints simultaneously. Achieving global consistency typically involves using algorithms such as constraint propagation, forward checking, and intelligent variable and value ordering techniques.

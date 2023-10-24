# Backtracking

Backtracking is the most used algorithm for solving CSP. It is an efficient method for systematically exploring the search space of possible solutions and finding a valid assignment of values to the variables.

The backtracking algorithm follows a depth-first search approach, systematically trying different values for the variables and backtracking whenever a partial assignment violates a constraint. It explores the search space by recursively traversing through the variable assignments, making choices at each step.

Here's a python (with pseudo-types) overview of the backtracking algorithm.

```python
# Backtracking:
# - either return a valid solution (list of values)
# - or failure
def backtracking_search(csp) -> list[val] | None:
	return backtrack({}, csp)

# Recursive backtracking
def backtrack(
		assignment: dict[var, val],
		csp: tuple[dict[var, dom], list[con]]
):
    # Check if assignment is complete
    if is_complete(assignment, csp):
        return assignment

    # Select an unassigned variable
    variable = select_unassigned_variable(assignment, csp)

    # Iterate through the domain values of the variable
    for value in order_domain_values(variable, assignment, csp):
        # Check if the value satisfies the constraints
        if is_consistent(value, variable, assignment, csp):
            # Assign the value to the variable
            assignment[variable] = value

            # Recursive call to continue the search
            result = backtrack(assignment, csp)

            # Check if a valid assignment is found
            if result is not None:
                return result

            # If no valid assignment found,
            # remove the value from assignment
            del assignment[variable]

	# End of consistent branch
    return None
```

Backtracking allows for an efficient exploration of the solution space by pruning branches that are guaranteed to lead to invalid solutions. It leverages the concept of depth-first search combined with backtracking to find a valid assignment while minimizing the number of assignments and constraint checks required.

Backtracking can be enhanced with various optimization techniques, such as variable and value ordering heuristics, constraint propagation, and forward checking, to improve the efficiency of finding a valid solution.

## Forward Checking

Forward checking is a technique used to reduce the search space and enforce consistency during the assignment process. It is an efficient form of constraint propagation that narrows down the possible values for variables by considering the constraints between variables and their domains.

Whenever a value is assigned to a variable, the domains of the neighbouring variables are reduced to only the values that are still compatible with the assigned value. This reduction is based on the constraints between the variables. By performing this local consistency check, we eliminate values from the domains of neighbouring variables that are not compatible with the assigned value, thus reducing the branching factor in the search space.

The main steps involved in forward checking are as follows:

1. **Initial assignment**: Start with an initial assignment of values to some variables in the CSP.

2. **Assign a value**: Select a variable and assign a value to it.

3. **Forward checking**: For each unassigned neighbouring variable, check the constraints between that variable and the assigned variable. Remove any values from the domain of the neighbouring variable that are inconsistent with the assigned value.

4. **Repeat**: Repeat steps 2 and 3, selecting variables and assigning values, and performing forward checking, until either a valid assignment is found or it is determined that no valid assignment exists.

# Best-First Search

Best-First Search is an informed search algorithm that explores a graph or state space by prioritizing nodes based on a heuristic evaluation function. It selects the most promising node to expand next, without considering the actual cost of reaching that node from the start.

The heuristic function, denoted as $h(n)$, provides an evaluation of how close a node is to the goal or how likely it is to lead to a solution. The algorithm selects the node with the highest heuristic value as the next node to expand.

Here is a high-level overview of the Best-First Search algorithm:

1. **Initialization**: Set the start node as the current node and initialize the open set to contain only the start node.

2. **Main Loop**: While the open set is not empty, perform the following steps:

    - Select the node with the highest heuristic value from the open set as the current node.
    - If the current node is the goal node or satisfies the desired condition, the search is complete. Return the solution or output the desired information.
    - Expand the current node by generating its neighboring nodes.
    - For each neighboring node, calculate its heuristic value using the heuristic function.
    - If the neighboring node is not in the open set or the heuristic value is higher than the existing value, update its heuristic value and add it to the open set.
3. **Termination**: If the open set becomes empty without finding a goal node or meeting the desired condition, the search fails. In this case, there is no solution.


Best-First Search is a greedy algorithm that prioritizes the most promising nodes based solely on their heuristic values. It does not consider the actual cost of reaching a node from the start, which means it may not always find the optimal solution. However, it can be highly efficient when the heuristic function provides accurate guidance towards the goal.

The choice of heuristic function is crucial in Best-First Search, as it directly affects the search behavior and solution quality. The heuristic should be admissible (never overestimating the true cost) and consistent (monotonic with respect to the actual cost) to ensure desirable search properties.

---

# Best First Search

The best first search is an algorithm that shares similarities with [breadth first search ](?TK) and [depth first search](?TK).

Given a function $h(n)$, where $n$ is a node, the algorithm will always try to explore first the nodes with the smallest $h(n)$ $min_{h(n)}\set n_i$

## Greedy Best First Search

TK informed w/heuristic

> [!info] Informed Algorithm
> 
> An informed algorithm has some kind of information such that the algorithm can follow some criteria (*heuristic*)

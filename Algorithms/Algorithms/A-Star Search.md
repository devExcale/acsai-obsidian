# A* Search Algorithm

A\* (pronounced "A-star") is a popular informed search algorithm used for finding the shortest path between a start node and a goal node in a graph or a weighted state space. It combines the advantages of both uniform cost search and greedy best-first search by considering both the actual cost from the start node, i.e. $g(n)$, and the estimated cost to the goal node, i.e. $h(n)$.

The A\* algorithm uses a heuristic function to estimate the cost of reaching the goal from a given node. The heuristic function, denoted as $h(n)$, provides an admissible and consistent estimate of the remaining cost to the goal. The key idea behind A\* is to prioritize expanding nodes with lower total estimated cost, i.e. $f(n) = g(n) + h(n)$.

Here is a high-level overview of the A* search algorithm:

1. **Initialization**: Set the start node as the current node and initialize the open set to contain only the start node.

2. **Main Loop**: While the open set is not empty, perform the following steps:
   - Select the node with the lowest $f(n)$ value from the open set as the current node.
   - If the current node is the goal node, the search is complete. Return the path from the start node to the goal node.
   - Expand the current node by generating its neighbouring nodes.
   - For each neighbouring node, calculate its $g(n)$ value (the cost of reaching that node from the start) and its $h(n)$ value (the estimated cost to the goal).
   - If the neighbouring node is not in the open set, add it to the open set and set its parent as the current node. Otherwise, update its $g(n)$ value if the new path has a lower cost.
   - Update the $f(n)$ value of the neighbouring node.
   
3. **Termination**: If the open set becomes empty before reaching the goal node, there is no path from the start to the goal. In this case, the search fails.

> [!info] Heuristic Function
> 
> The effectiveness of A* heavily relies on the choice of heuristic function. A good heuristic should be admissible (never overestimating the true cost) and consistent (monotonic with respect to the actual cost).
> 
> Common heuristics include Manhattan distance, Euclidean distance, and the number of misplaced tiles (in the case of puzzle-solving problems).


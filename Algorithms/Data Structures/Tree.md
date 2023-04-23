# Tree

A *tree* is a [directed](/Algorithms/Data%20Structures/Graphs.md#Directed%20or%20Undirected%20Graphs) [connected](/Algorithms/Data%20Structures/Graphs.md#Connected%20or%20Disconnected%20Graphs) [graph](/Algorithms/Data%20Structures/Graphs.md) such that:  

- there exists one and only one node from which every node is reachable (called *root*);  
- there exists one and only one [path](/Algorithms/Data%20Structures/Graphs.md#Path) from the root to every other node (i.e. no loops or overlapping paths).

The nodes with no outgoing edges are called **leaves**.

## Binary Tree

A *binary tree* is a [tree](#Tree) in which the root is connected to at most two nodes, and the other nodes are connected to at most three other nodes.

## Chain

A *chain* is a [tree](#Tree) in which there exists one and only one leaf. This implies that every node, except for the root and the leaf, must be connected to two other nodes (with one ingoing and one outgoing edges).

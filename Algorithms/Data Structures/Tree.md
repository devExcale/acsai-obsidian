# Tree

A *tree* is a [directed](/Algorithms/Data Structures/Graphs.md#Directed or Undirected Graphs) [connected](/Algorithms/Data Structures/Graphs.md#Connected or Disconnected Graphs) [graph](/Algorithms/Data Structures/Graphs.md) such that:  

- there exists one and only one node from which every node is reachable (called *root*);  
- there exists one and only one [path](/Algorithms/Data Structures/Graphs.md#Path) from the root to every other node (i.e. no loops or overlapping paths).

The nodes with no outgoing edges are called **leaves**.

## Binary Tree

A *binary tree* is a [tree](#Tree) in which the root is connected to at most two nodes, and the other nodes are connected to at most three other nodes.

## Chain

A *chain* is a [tree](#Tree) in which there exists one and only one leaf. This implies that every node, except for the root and the leaf, must be connected to two other nodes (with one ingoing and one outgoing edges).

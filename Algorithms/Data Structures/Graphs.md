# Graphs

A graph is a pair $G = (V, E)$ where
- $V$ is a set whose elements are called *vertices*,
- $E$ is a set of pairs of vertices such that $E \subseteq V ^2$, the elements are called *edges*.

## Types of Graphs

### Directed  or Undirected Graphs

> [!abstract] Undirected Graph
> 
> An undirected graph does not have an order, i.e. a single edge $(v_1, v_2)$ connects both $v_1$ to $v_2$ and $v_2$ to $v_1$, without order of traversing.
> 
> $$\large e = (v_1, v_2) = (v_2, v_1)$$

> [!abstract] Directed Graph
> 
> A directed graph has an order, i.e. a single edge $(v_1, v_2)$ connects the vertex $v_1$ to $v_2$, but $v_2$ may or may not be connected to $v_1$.
> 
> $$\large e = (v_1, v_2) \neq (v_2, v_1)$$

### Connected or Disconnected Graphs

> [!abstract] Connected or Disconnected Graphs
> 
> A graph is said to be *connected* if there exists a path from any vertex $x$ to another vertex $y$, otherwise the graph is said to be *disconnected*.

## Walk

A **walk** of a [graph](#graphs) from $v_0$ to $v_n$ is a sequence $v_0, v_1, \ldots, v_n$ such that $(v_{i-1}, v_i) \in E$.

> [!note] Length
> 
> The *length* of the walk is $n$.

If $v_0 = v_n$, then the walk is said to be a *closed walk*.

## Trail

A **trail** of a [graph](#graphs) is a [walk](#walk) in which the edges are not traversed more than once, i.e. $(v_{i-1}, v_i) \neq (v_{j-1}, v_j)$ $\forall i \neq j$.

## Path

A **path** is a [walk](#walk) in which every node is not traversed more than once. Exceptionally, the starting node may be the ending node, in this case the path is said to be a **cycle**.

$$\large
	v_0 \neq \cdots \neq v_{n-1}
$$

## Directed Acyclic Graph

If a [graph](#graphs) presents no [cycles](#path), then the graph is said a **Directed Acyclic Graph**.

## Labelled Graph

A **vertex-labelled graph** is a tuple $(V, E, L_V, \mathcal l_V)$ where
- $V, E$ are the sets of vertices and edges of a graph,
- $L_V$ is a finite set of symbols (*labels*),
- $\mathcal l_V$ is a function $\mathcal l_V : V \rightarrow L_V$.

A **edge-labelled graph** is a tuple $(V, E, L_E, \mathcal l_E)$ where
- $V, E$ are the sets of vertices and edges of a graph,
- $L_E$ is a finite set of symbols (*labels*),
- $\mathcal l_E$ is a function $\mathcal l_E : E \rightarrow L_E$.

A **labelled graph** is a tuple $(V, E, L_V, L_E, \mathcal l_V, \mathcal l_E)$ where everything is as defined as above.

> [!note] Weighed Graph
>
> When the labels $L_V, L_E$ belong to an ordered set, then the labelled graph is also said **weighted graph**.
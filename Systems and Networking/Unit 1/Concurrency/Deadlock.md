# Deadlock

Whenever two or more thread are competing for a fixed number of resources, some threads may block waiting for a resource to be freed. If all threads block while waiting for resources occupied by the other threads, no thread can continue: it's a **deadlock**.

A deadlock can happen if *all* of the following conditions hold,

1. **Mutual Exclusion:** at least one thread must hold a non-shareable resource;
2. **Hold and Wait:** at least one thread is holding a non-shareable resource and it's waiting for other resource(s) to become available;
3. **No Preemption:** a thread can only release a resource voluntarily, neither another thread nor the OS can force it to release the resource;
4. **Circular Wait:** there's a set of threads $t_1, \ldots, t_n$, where $t_i$ is waiting on resource(s) held by $t_{(i+1)\%5}$.

## Deadlock Detection

To detect deadlock, a certain type of graph (**Resource Allocation Graph**) can be used.

Let $G=(V,E)$ be a directed graph, where
- $V$ is the set containing both the resources $\set{r_1, \ldots, r_m}$ and the threads $\set{t_1, \ldots, t_n}$;
- $E$ is the set of edges connecting threads and resources.

Edges can be of two types,
- **Request Edge:** a directed edge $(t_i, r_j)$, it indicates that the thread $t_i$ has requested the resource $r_j$, but hasn't acquired it yet;
- **Assignment Edge:** a directed edge $(r_j, t_i)$, it indicates that the OS has assigned the resource $r_j$ to thread $r_i$.

![Example of RAG](?TK)

A deadlock might exists if the graph contains cycles.

## Deadlock Prevention

A deadlock might happen only if *all* the previous conditions hold: a deadlock may be prevented by ensuring that at least one of the conditions doesn't hold anymore.

1. **Mutual Exclusion:** make resources shareable;
2. **Hold and Wait:** a thread may not make sequential requests for resources while holding some, requests must all be made at once;
3. **No Preemption:** if a thread makes a request for a resource that cannot be satisfied yet, all the resources held by the thread will be temporary released;
4. **Circular Wait:** impose an ordering on resources and enforce to request them in such an order.

## Deadlock Avoidance

TK (& Banker)
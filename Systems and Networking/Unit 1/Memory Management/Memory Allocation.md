# Memory Allocation

There are different ways to allocate memory to processes, from simpler ones to the more complex ones.

## Contiguous Memory Allocation

One of the most reasonable ways to allocate memory, is to keep track of the unused memory spaces (called *holes*) and allocate holes to processes that need memory. Contiguous means that the process memory space isn't broken into smaller pieces, but the process is assigned a single continuous block of memory.

> [!question] Allocation Algorithms
> Between the following algorithms, simulations show that the ranking of efficiencies is as follows (from most efficient to least):
> 1. First-Fit
> 2. Best-Fit
> 3. Worst-Fit

### First-Fit Memory Allocation

Scan the list of holes until one big enough for the process is found, then allocate the hole to the process. Subsequent requests for memory could start scanning from the start or from the position of the last hole.

> [!tip] Complexity
> First-Fit allocation has a time complexity of $O(n)$. $n$ is the number of holes.

### Best-Fit Memory Allocation

Allocate the smallest hole that is big enough to satisfy the request, this way larger holes could be used for processes that may require more memory.

> [!tip] Complexity
> Best-Fit allocation has a time complexity of $O(n)$ normally, but could be $O(\log n)$ if the list of holes is kept sorted. $n$ is the number of holes.

### Worst-Fit Memory Allocation

Allocate the largest hole available, which may seem counterintuitive but increase the likelihood that the remaining portion from the allocation could be used in future requests.

> [!tip] Complexity
> Worst-Fit allocation, like Best-Fit, has a time complexity of $O(n)$ normally, but could be $O(\log n)$ if the list of holes is kept sorted. $n$ is the number of holes.

## Fragmentation

Memory allocation suffers a big problem: *fragmentation*. When allocating a memory segment, a smaller segment might remain that can't be useful to other processes because it's too small.

There are two types of fragmentation,
- **External Fragmentation:** when there's enough space to load a process in memory, but the space isn't contiguous (it's composed of smaller sparse holes);
- **Internal Fragmentation:** when it's more efficient to allocate a whole hole to a process rather than keeping track of a tinier hole (e.g. some bytes).

> [!cite] Wasted Memory
> Simulations show that for every $2N$ allocated blocks, $N$ are lost due to external fragmentation, i.e. one third of memory space is wasted on average because of fragmentation.

Fragmentation could be solved by either
- **Full Compaction:** moving all processes "up", removing any hole between allocated memory spaces and making one big hole;
- **Partial Compaction:** moving as less processes as possible, so to make a hole big enough for the new process to fit;
- **Swapping:** processes currently not in execution (i.e. in waiting state) could be *swapped out* of the memory and saved in the disk to free space, then when they go back to a ready state they are *swapped in* the memory.

Both fragmentation and swapping are good management techniques that unfortunately require much overhead, so if the possibility arises it'd be better to turn to more efficient techniques (e.g. *[paging](/Systems%20and%20Networking/Unit%201/Memory%20Management/Paging.md)*).
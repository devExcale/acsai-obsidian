# Segmentation

Segmentation is a memory management technique applied by some (if not most) programming languages (e.g. C). With segmentation, the code is divided into few *memory segments*, each with a specific logic meaning and memory location (memory is supposed contiguous and fixed).

> [!example] C Segmentation
> A C compiler usually generates 5 segments: *code*, *libraries*, *static variables*, *stack*, *heap*.

Segmentation is invisible to the program: the logic address is divided into two parts:
- A few bits which indicate the segment;
- The rest of the address is the offset in the segment.

The segment index is translated, using a segment table, into the base address of the segment in the memory; then the offset is added to the base address to get the actual memory address. The segment table, because it has few entries, could be stored in normal hardware registers.

> [!note] Base-Limit
> Segmentation implements the base-limit registers security feature: each segment's entry in the segmentation table has a base and a limit addresses.
> 
> Before accessing the actual memory address, the Control Unit checks if `base` + `offset` > `limit`, if it is then a trap is issued.  


> [!warning] Fragmentation
> Normal segmentation supposes that the segments are allocated in a contiguous block of memory, which means that internal and external fragmentations are still a problem.

# Paging

Paging is a memory management technique that provides the illusion of a contiguous logical address space, divided into fixed-size block called **pages**. These pages can then be mapped to non-contiguous physical frames (physical blocks in the memory).

> [!tip] Fragmentation
> With paging, external fragmentation is eliminated because pages have a fixed size, even though internal fragmentation may still occur (the whole page has to be allocated).

Paging is a combination of efforts from both the OS and the HW:
- the OS must map logical pages to physical frames;
- the HW must translate virtual addresses to physical ones.

The OS can map pages to frames using a **Page Tabe**, which is a table with just two columns: the *page number* and the associated *frame number*.

![Page Table](?TK)

Processes still use virtual/logical addresses to refer to memory, the paging construct is invisible to processes. The virtual address space created by the paging construct is a contiguous address space that stars from 0.

> [!note] Virtual to Physical Address
> Addresses are divided into two parts:
> - The LSBs are the *offset*, used to identify cells inside pages and frames
> - The remaining MSBs are the page/frame identifier
> 
> The page's and frame's offset bust be the same size, because pages and frames have the same size. Identifiers, though, don't need to be the same size, because the only requirement is for pages to have a corresponding frame.

> [!tip] Page/Frame Size
> The usual page/frame size is a power of 2, usually between 512B and 8192B (i.e. 8KiB). This is because there's no need for `div` and `mod` operations is powers of 2, the results are MSBs and LSBs, respectively.
> 
> ![Powers images](?TK)

## Translation Look-aside Buffer

The Page Table must still be stored somewhere, caches are too small to fit it and the main memory is too slow to permit fast access. To solve this problem, **Translation Look-aside Buffers** are born.

The TLB is (generally) a L1 cache that stores a part of the page/frame mappings for fast access, while the full page table resides in memory (**Page Table Base Register**).

When dealing with multiple processes, the TLB needs to reflect the mappings of the current process. This can be done in two ways:
- The TLB is reset at every context-switch, possibly losing time later (the first accesses after a context-switch are all misses):
- The content of the TLB is saved on each context-switch and then loaded back.

> [!tip] Memory Access Time
> With no TLB, access to memory would take $T_\text{MA} = 2 \cdot t_\text{MA}$ (one access to translate the virtual address, one access to retrieve data).
> 
> With TLB, access to memory would take 
> $$\large
> 	T_\text{MA} = p ( t_\text{MA} + t_\text{TLB} )
> 	+ (1-p) ( 2 \cdot t_\text{MA} + t_\text{TLB} )
> $$
> 
> where:
> - $T_\text{MA}$ is the total time to access the corresponding physical address from a virtual address;
> - $t_\text{MA}$ is the physical memory access time;
> - $t_\text{TLB}$ is the lookup time on TLB;
> - $p$ is the probability of a TLB cache hit (or hit ratio).

## Memory Handling TK

Whenever a process starts:

1. The process asks for $N$ Bytes (equivalent to $k$ pages);
2. If $k$ frames are free then those are allocated to the process, otherwise frames no longer needed are swapped-out;
3. Each page is associated to one of the frames, the PTBR is updated accordingly;
4. The TLB is flushed and ready to use for the process;
5. As the process runs, the OS loads the missed lookups into the TLB, possibly replacing existing entries if full.

Each process will have a different TLB and page table, so the address of the PTBR and a copy of the TLB will be saved in the PCB.

## Page Sharing

If two or more processes share the same code, the pages with the code could be shared among the processes, to save up space in memory. This can be done by pointing the pages (supposedly) holding the code to the same frames.

> [!warning] Reentrant Code
> Pages could be shared only if the code is *reentrant*:
> - The code doesn't change nor it overwrites itself;
> - Each process running the code has its own set of registers and data.


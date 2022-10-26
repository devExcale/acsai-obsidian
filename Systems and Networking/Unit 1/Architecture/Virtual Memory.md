# Virtual Memory

Virtual memory is an abstraction of the physical [memory](/Systems%20and%20Networking/Unit%201/Architecture/Memory.md). Its reason is to give each process the illusion that the physical memory is a contiguous address space, called **virtual address space**.

It allows programs to be run without them being entirely loaded in the physical memory, instead loading them piece by piece when needed. Note, though, that in the virtual memory the program is considered loaded in its entirety (as a single block) in a single memory space.

A virtual memory is implemented by both hardware ([MMU](#Memory%20Management%20Unit)) and software ([OS](/Systems%20and%20Networking/Unit%201/Operating%20System/Operating%20System.md)).

An advantage of virtual memory is the range of the memory: the [CPU](/Systems%20and%20Networking/Unit%201/Architecture/CPU.md) can address 2<sup>64</sup> addresses, which equal to 2<sup>64</sup> bytes (16 exbibytes)! Approximately, this is a billion times more than the physical memory capacity.

## Page

Pages are blocks of [memory](/Systems%20and%20Networking/Unit%201/Architecture/Memory.md) that partition the virtual address space, they have the same size (e.g. 4 KiB).

They are either loaded in main memory or stored on disk:
- if the page is being used then it's loaded in the main memory, mapped to an address different than the one in the virtual address space;
- if the page isn't being used then it's stored on disk, to free up space in the main memory. If needed, the page can be loaded again in the main memory.

## Memory Management Unit

A physical unit that converts virtual addresses to physical ones using a **page table**, which is managed by the [OS](/Systems%20and%20Networking/Unit%201/Operating%20System/Operating%20System.md). The OS must manage the loading and unloading of the pages.

For quick lookups, the MMU uses a [cache](/Systems%20and%20Networking/Unit%201/Architecture/Cache.md) called [Translation Look-aside Buffer](?TK), instead of searching the page in the page table.
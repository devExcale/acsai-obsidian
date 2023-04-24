# Virtual Memory

Virtual memory is an abstraction of the physical [memory](/Systems%20and%20Networking/Unit%201/Architecture/Memory.md). Its reason is to give each process the illusion that the physical memory is a contiguous address space, called [Virtual Address Space](#Virtual%20Address%20Space).

It allows programs to be run without them being entirely loaded in the physical memory, instead loading them piece by piece when needed. Note, though, that in the virtual memory the program is considered loaded in its entirety (as a single block) in a single memory space.

A virtual memory is implemented by both hardware ([MMU](#Memory%20Management%20Unit)) and software ([OS](/Systems%20and%20Networking/Unit%201/Operating%20System/Operating%20System.md)).

An advantage of virtual memory is the range of the memory: the [CPU](/Systems%20and%20Networking/Unit%201/Architecture/CPU.md) can address $2^{64}$ addresses, equivalent to $2^{64}$ bytes (16 exbibytes)! Approximately, this is a billion times more than the physical memory capacity.

## Page

Pages are blocks of [memory](/Systems%20and%20Networking/Unit%201/Architecture/Memory.md) that partition the virtual address space, they have the same size (e.g. 4 KiB).

They are either loaded in main memory or stored on disk:
- if the page is being used then it's loaded in the main memory, mapped to an address different than the one in the virtual address space;
- if the page isn't being used then it's stored on disk, to free up space in the main memory. If needed, the page can be loaded again in the main memory.

## Memory Management Unit

A physical unit that converts virtual addresses to physical ones using a **page table**, which is managed by the [OS](/Systems%20and%20Networking/Unit%201/Operating%20System/Operating%20System.md). The OS must manage the loading and unloading of the pages.

For quick lookups, the MMU uses a [cache](/Systems%20and%20Networking/Unit%201/Architecture/Cache.md) called [Translation Look-aside Buffer](?TK), instead of searching the page in the page table.

## Virtual Address Space

The virtual address space is a virtual memory block used by [processes](/Systems%20and%20Networking/Unit%201/Operating%20System/Process.md). Every process can use a fixed contiguous amount of *virtual* addresses in the memory, which are translated into real addresses by the [MMU](#Memory%20Management%20Unit).

The amount of addresses user programs can use are dependant on the hardware and on the [OS](/Systems%20and%20Networking/Unit%201/Operating%20System/Operating%20System.md). For example, on a 32-bit architecture, the virtual addresses range from $0$ to $2^{32}-1$.

The layout is as follows (from top to bottom):
1. Kernel Space
2. Stack (growing towards bottom)
3. Heap (growing towards top)
4. BSS
5. Data
6. Text

TK

#### Text

Contains executable instructions.

#### Data

Static variables.

#### BSS

Global variables (non-initialized).

#### HEAP

Used for dynamic allocation.

#### Stack

LIFO structure used to store all the data needed by a function call ([stack frame](?TK))

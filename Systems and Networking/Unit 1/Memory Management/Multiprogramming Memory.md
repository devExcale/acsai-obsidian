# Multiprogramming Memory

The term *Multiprogramming Memory* means a memory that can host multiple programs that are executing. Some rules must regulate the memory, otherwise programs could corrupt themselves or even the OS.

**Sharing Goals:**
- Several processes can coexist in the main memory at the same time;
- Cooperating processes can share parts of the address space;

**Transparency Goals:**
- Processes shouldn't be aware that the memory is shared;
- Processes shouldn't know which part of the physical memory is them assigned.

**Security Goals:**
- Processes must not be able to corrupt each other or the OS;
- Processes must not be able to read data of other processes.

**Efficiency Goals:**
- CPU and memory performance should not degrade too much due to sharing:
- Keep memory fragmentation low.

## Static Relocation

Static relocation uses [Load Time Address Binding](/Systems and Networking/Unit 1/Memory Management/Address Binding.md#Load Time Address Binding). The OS is loaded at the highest memory address, while other processes are loaded contiguously below the OS (`memory_size` - `os_size` - 1).

> [!warning] Static Relocation Problems
> With static relocation no HW support is needed, but there are many problems:
> - Processes could corrupt other processes or the OS;
> - Processes are to be allocated contiguously, which implies assuming worst case stack and heap;
> - Processes can't be moved around in the memory once in has been allocated.

## Dynamic Relocation

Dynamic Relocation uses [Execution Time Address Binding](/Systems and Networking/Unit 1/Memory Management/Address Binding.md#Execution Time Address Binding). On each memory access request, the [MMU](/Systems and Networking/Unit 1/Architecture/Virtual Memory.md#Memory Management Unit) can check if the physical address associated to the virtual address belongs to the requesting process and block the request if needed.

![MMU Logic Diagram](?TK)

Dynamic Relocation offers many advantages that Static Relocation doesn't:
- Read/Write protection across processes' address spaces;
- Possibility to move processes during execution;
- Possibility to let processes' address space grow over time;
- Simple and fast hardware implementation (MMU), no software overhead;

but still has problems on its own:
- Contiguous allocation in physical memory (possible memory waste);
- No partial sharing of address space yet;
- The entirety of the program must be allocated in memory.

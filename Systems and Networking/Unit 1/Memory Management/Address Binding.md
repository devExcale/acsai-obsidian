# Address Binding

A program is composed of instructions and data, which are hardcoded into the program. For the program to be executed, it must be *translated* (converting all the symbolic names of the language into binary code) and loaded into the main memory, so that the CPU can access it.

> [!info] Compiling and Loading
> Translation is done by compilers, assemblers and linkers, loading is done by the OS loader.

If the CPU has to access a certain variable in a program, it must use the physical address for that variable: the variable must have an associated physical address (*address binding*).

## Compile Time Address Binding

Assuming the program knows the exact address where it will reside in the main memory, then the compiler can translate every variable to absolute physical addresses, that the CPU will use to access the variables.

The code is called *absolute code*, because the physical addresses will be equal to the *logical addresses* (addresses used by the program), as there's no translation from the address the program uses to the final one the CPU uses.

This type of address binding poses a lot of problems, e.g. if the program has to be loaded in a different memory location than the code has to be compiled again to relocate the addresses.

## Load Time Address Binding

Just like compile time address binding, the compiler assumes that the program is gonna be in a certain memory location, so all the addresses will be relative to that specific memory location. When the program is loaded into memory, the *loader* adds the offset from the actual memory location to the addresses, so that the calculated addresses are the real physical ones.

The code is called *statically relocatable code*, because the program can be run in any memory location, but it has to be restarted each time it needs to be moved. The logical addresses are still considered equal to the physical addresses, because a simple offset matches them up.

## Execution Time Address Binding

With execution time address binding, the logical addresses used by the program are translated in runtime in physical addresses. This requires special a hardware support called **[MMU](/Systems and Networking/Unit 1/Architecture/Virtual Memory.md#Memory Management Unit)**.

The logical addresses (also called virtual addresses) aren't equal to the physical addresses anymore, because each virtual address could be any physical address.

> [!note] Dynamically Relocatable Code
> The code is called *Dynamically Relocatable Code*, because the program can be moved around in the main memory during execution, without any problem.

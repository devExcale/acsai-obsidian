# Instructions

The collection of all the instructions the [CPU](/Systems%20and%20Networking/Unit%201/Architecture/CPU.md) can execute is called **Instruction Set**.

The CPU's architecture can be abstracted using only the instruction set and instruction cycle: the physical processor is then created by implementing the abstract architecture (e.g. Intel/AMD processors from [x86](https://en.wikipedia.org/wiki/X86), phones/Raspberry Pi processors from [ARM](https://www.arm.com/)).

An Instruction is composed of two parts:
- An operator (**opcode**)
- Zero or mode **operands** (representing either registers, memory addresses or literals)

## Protected Instructions

TK
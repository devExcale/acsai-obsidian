# Registers

Registers are small storages located in the [CPU](/Systems%20and%20Networking/Unit%201/Architecture/CPU.md), usually the size of a [word](?), used to store values the processor will use in a short time.

They can be of two types:
- **General purpose** (e.g. eax, ebx, ecx for the x86 arch.)
- **Special purpose**

## General Purpose

TK

## Special Purpose

- **Stack Pointer:** contains the address of the latest entry inserted in the [stack](?TK);
- **Program Counter:** contains the address of the next [instruction](/Systems%20and%20Networking/Unit%201/Architecture/Instructions.md) to execute;
- **Return Address:** contains the next instruction to execute when exiting a [function](?TK);
- **Zero:** a register whose value will *always* be zero.
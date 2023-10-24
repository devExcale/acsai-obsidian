# Operating System

There isn't a universal definition for an **Operating System**, but one could say that it is an implementation of a *virtual machine* which should be easier to program than bare [hardware](/Systems and Networking/Unit 1/High-Level Computer Architecture.md).

An **OS** stands between users (or application programs) and the underlying hardware, and it is the only mean to access the hardware.

## Design

An OS must be designed with some goals in mind.

It could be oriented towards the user (easy to use) or towards the system itself (easy to design and implement).

It is crucial to separate **policies** (what the OS will do) from **mechanisms** (how the OS will do something):
- (**flexibility**) addition and modification of policies can be easily supported;
- (**reusability**) existing mechanism can be reused to implement new policies;
- (**stability**) adding a new policy shouldn't destabilize the whole system.

## Features

The features of an OS are many:
- **Resource Manager:** manage physical resources ([CPU](/Systems and Networking/Unit 1/Architecture/CPU.md), [memory](/Systems and Networking/Unit 1/Architecture/Memory.md), [I/O](/Systems and Networking/Unit 1/Architecture/IO Devices.md), etc.) with efficiency;
- **Virtual Machine:** virtualize any physical resource, to give the user and programs the illusion of infinite resources (and for efficiency reasons);
- **Separate HW/SW:** provide a set of [API](?TK)'s, to control the access to physical hardware.

## Services

Which services an Operative System can offer is dictated by the underlying structure.

| **OS Service**          | **HW Support**                                                                                                                                                                                                  |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Protection and Security | [Kernel/User Mode](/Systems and Networking/Unit 1/Operating System/Protection and Security.md#Kernel-User Mode), Protected Instructions, Base/Limit Registers                                     |
| System Calls            | [Traps](/Systems and Networking/Unit 1/Operating System/Trap.md), Interrupt Vectors                                                                                                                     |
| Exception Handling      | [Traps](/Systems and Networking/Unit 1/Operating System/Trap.md), Interrupt Vectors                                                                                                                     |
| I/O Operations          | [Traps](/Systems and Networking/Unit 1/Operating System/Trap.md), Interrupt Vectors, [Memory Mapping](/Systems and Networking/Unit 1/Architecture/IO Devices.md#Communicating with Devices) |
| Scheduling              | [Timer](/Systems and Networking/Unit 1/Architecture/Timer.md)                                                                                                                                             |
| Synchronization         | Atomic Instructions                                                                                                                                                                                             |
| Virtual Memory          | Translation Look-Aside Buffer (TLB)                                                                                                                                                                             |

## Structure

Many OS have different structures, with a mixture of languages and techniques. An OS should be partitioned into separate subsystems, each with carefully defined tasks, inputs, outputs and performance characteristics.

| **Structure**                                                | **PROs**                                             | **CONs**                                           |
| ------------------------------------------------------------ | ---------------------------------------------------- | -------------------------------------------------- |
| [Simple Structure](#Simple Structure)                      | easy to implement                                    | rigidity, security                                 |
| [Traditional Monolithic](#Traditional Monolithic Kernel) | easy to implement, efficiency                        | rigidity, security                                 |
| [Layered](#Layered Structure)                              | easy to implement and debug, modularity, portability | communication overhead, duplicated functionalities |
| [Microkernel](#Microkernel Structure)                      | security, reliability, extendibility                 | efficiency (message passing)                       |

### Simple Structure

The main example being *MS-DOS*, it is the most simple OS structure, there is no modular subsystem whatsoever and no separation between [kernel and user mode](/Systems and Networking/Unit 1/Operating System/Protection and Security.md#Kernel-User Mode). Every functionality is implemented directly without decoupling of [policies and mechanisms](#Design).

![Diagram of Simple Structure](?TK)

### Traditional Monolithic Kernel

The main example being *UNIX systems*, it's one huge program run as one process in the same [address space](/Systems and Networking/Unit 1/Architecture/Virtual Memory.md#Virtual Memory).

Even though it's one big program, it's still kind of modular: the protected functionalities are run in [kernel mode](/Systems and Networking/Unit 1/Operating System/Protection and Security.md#Kernel-User Mode) (e.g. [I/O](/Systems and Networking/Unit 1/Architecture/IO Devices.md), [virtual memory](/Systems and Networking/Unit 1/Architecture/Virtual Memory.md), [scheduling](?TK)), while the other programs (e.g. shells, commands) are run in [user mode](/Systems and Networking/Unit 1/Operating System/Protection and Security.md#Kernel-User Mode).

![Diagram of Traditional Monolithic Kernel](?TK)

### Layered Structure

The OS is divided in $N$ layers, with the hardware being layer 0. Each layer L uses the functionalities implemented by the layer $L-1$ to expose new functionalities to layer $L+1$.

![Diagram of Layered Structure](?TK)

### Microkernel Structure

The microkernel opposes to the monolithic kernel because the kernel contains very basic functionalities, usually what's needed to communicate with the hardware (e.g. [scheduling](?TK), [memory management](/Systems and Networking/Unit 1/Architecture/Memory.md)), the rest (e.g. application programs, [file system](?TK)) runs in [user mode](/Systems and Networking/Unit 1/Operating System/Protection and Security.md#Kernel-User Mode).

In this structure there is a clear distinction between [policy](#Design) (user mode) and [mechanism](#Design) (microkernel) and it is very modular, but this modularity comes at a cost: processes use [message passing](/Systems and Networking/Unit 1/Operating System/System Calls.md#Message Passing) to communicate, which can slow down processing speed.

![Diagram of Microkernel Structure](?TK)

### Loadable Kernel Modules

Many modern systems implement this design for its flexibility, which is similar to the layered and microkernel structures:
- The main focus is on [object-oriented](?TK) for reusability;
- Each functionality is a module that can talk to others through some interface;
- Each module can be loaded when needed within the **kernel space** (memory space of the kernel).

![Diagram of LKM](?TK)

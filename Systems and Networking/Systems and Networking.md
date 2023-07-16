## Creating a Process

A process may create other processes through [System Calls](/Systems and Networking/Unit 1/Operating System/System Calls.md), the creator process is called **parent** while the created process is called **child**. Each new process is given a unique id (PID) and stores the parent process' id (PPID).

Regarding resources, there are two possibilities:
- The child is a perfect copy of the parent, sharing the same [text and data segments](/Systems and Networking/Unit 1/Architecture/Virtual Memory.md#Virtual Address Space) but in a different [address space](/Systems and Networking/Unit 1/Architecture/Virtual Memory.md#Virtual Address Space). This is the behaviour of the [`fork`](/Systems and Networking/Unit 1/Operating System/System Calls.md#Common System Calls) system call.
- The child is a brand new process, with a different program loaded into the address space. This can be done, after a fork, by using the [`exec`](/Systems and Networking/Unit 1/Operating System/System Calls.md#Common System Calls) system call.

The parent process, after creating the child, has two options:
- Wait for the child process to terminate and then continue executing. A process may wait for another process with the [`wait`](/Systems and Networking/Unit 1/Operating System/System Calls.md#Common System Calls) system call.
- Run concurrently with the child without being blocked.


# Systems and Networking

*Systems and Networking is a course that studies the hardware of machines and the interconnection of those machines.*

The course is divided in two courses:
- Unit 1, centred around the hardware and software of the single machine;
- Unit 2, centred around networks of multiple machines.

Unit 1 is focused more and the hardware/software of the single machine, while unit 2 is centred around networks and connectivity.

---

## Table of Contents

### Unit 1

- [High-Level Computer Architecture](/Unit 1/High-Level Computer Architecture.md)
- [Operating System](/Systems and Networking/Unit 1/Operating System/Operating System.md)

### Unit 2

- [Networks](/Systems and Networking/Unit 2/Networks.md)
- [Network Core](/Systems and Networking/Unit 2/Network Core.md)
- [Transport Means](/Systems and Networking/Unit 2/Transport Means.md)
- [Application Architecture](/Systems and Networking/Unit 2/Application Architecture.md)
- [Security](/Systems and Networking/Unit 2/Security.md)

[**Internet Protocol**](/Systems and Networking/Unit 2/Internet/Layered Structure.md)

- [Packet](/Systems and Networking/Unit 2/Internet/Packet.md)
- [ISO-OSI Model](/Systems and Networking/Unit 2/Internet/ISO-OSI Model.md)
- [Application Layer](/Systems and Networking/Unit 2/Internet/Application Layer.md)
- [Transport Layer](/Systems and Networking/Unit 2/Internet/Transport Layer.md)
- [Network Layer](/Systems and Networking/Unit 2/Internet/Network Layer.md)
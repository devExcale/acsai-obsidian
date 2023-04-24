## Creating a Process

A process may create other processes through [System Calls](/Systems%20and%20Networking/Unit%201/Operating%20System/System%20Calls.md), the creator process is called **parent** while the created process is called **child**. Each new process is given a unique id (PID) and stores the parent process' id (PPID).

Regarding resources, there are two possibilities:
- The child is a perfect copy of the parent, sharing the same [text and data segments](/Systems%20and%20Networking/Unit%201/Architecture/Virtual%20Memory.md#Virtual%20Address%20Space) but in a different [address space](/Systems%20and%20Networking/Unit%201/Architecture/Virtual%20Memory.md#Virtual%20Address%20Space). This is the behaviour of the [`fork`](/Systems%20and%20Networking/Unit%201/Operating%20System/System%20Calls.md#Common%20System%20Calls) system call.
- The child is a brand new process, with a different program loaded into the address space. This can be done, after a fork, by using the [`exec`](/Systems%20and%20Networking/Unit%201/Operating%20System/System%20Calls.md#Common%20System%20Calls) system call.

The parent process, after creating the child, has two options:
- Wait for the child process to terminate and then continue executing. A process may wait for another process with the [`wait`](/Systems%20and%20Networking/Unit%201/Operating%20System/System%20Calls.md#Common%20System%20Calls) system call.
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

- [High-Level Computer Architecture](/Unit%201/High-Level%20Computer%20Architecture.md)
- [Operating System](/Systems%20and%20Networking/Unit%201/Operating%20System/Operating%20System.md)

### Unit 2

- [Networks](/Systems%20and%20Networking/Unit%202/Networks.md)
- [Devices](/Systems%20and%20Networking/Unit%202/Devices.md)
- [Protocols](/Systems%20and%20Networking/Unit%202/Protocols.md)
- [Packet](/Systems%20and%20Networking/Unit%202/Packets/Packet.md)

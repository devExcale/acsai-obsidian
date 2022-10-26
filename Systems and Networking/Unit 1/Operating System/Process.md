# Process

A *process* is a particular instance of a program, it differs from a program because a program is static, saved in the [mass memory](/Systems%20and%20Networking/Unit%201/Architecture/Memory.md), while a process is the program that's running in the [main memory](/Systems%20and%20Networking/Unit%201/Architecture/Memory.md). Many processes may run the same program, but each process instance will have its own state!

## Process Control Block

The *Process Control Block* is the main structure used by the [OS](/Systems%20and%20Networking/Unit%201/Operating%20System/Operating%20System.md) to keep track of all the processes.

Every process has its own PCB. Every time a new process is created, a corresponding PCB is created and placed into a queue containing all the other PCBs. As soon as the corresponding process is terminated, the PCB is deallocated.

The PCB contains the following information:
- [Execution State](#Process%20Execution%20State)
- PID (process identifier, a unique number)
- [Registers'](/Systems%20and%20Networking/Unit%201/Architecture/Registers.md) values (e.g. program counter, stack pointer, general purpose)
- [Scheduling](?TK) information (priority, state)
- Memory management information ([page tables](/Systems%20and%20Networking/Unit%201/Architecture/Virtual%20Memory.md#Page))
- [I/O](/Systems%20and%20Networking/Unit%201/Architecture/IO%20Devices.md) status (list of open files/devices)
- General information ([CPU](/Systems%20and%20Networking/Unit%201/Architecture/CPU.md) time consumed, owner process)

## Process Execution State

Each process has an execution state, dictated by program actions (e.g. [system calls](/Systems%20and%20Networking/Unit%201/Operating%20System/System%20Calls.md)), [OS](/Systems%20and%20Networking/Unit%201/Operating%20System/Operating%20System.md) actions (e.g. [scheduling](?TK)) and external actions (e.g. [interrupts](/Systems%20and%20Networking/Unit%201/Operating%20System/Trap.md#Interrupt))

![Process Execution State Transitions Diagram](?TK)

### New

In *new* state, the process has just been successfully set up and it's waiting to be picked up for the first time by the [scheduler](?TK).

From here, the process can go in the following states:
- [Ready](#Ready) (admitted)

### Ready

In *ready* state, the process is ready to be executed by the [CPU](/Systems%20and%20Networking/Unit%201/Architecture/CPU.md).

From here, the process can go in the following states:
- [Running](#Running) (dispatched by scheduler)

### Running

In *running* state, the process is actually being executed by the [CPU](/Systems%20and%20Networking/Unit%201/Architecture/CPU.md).

From here, the process can go in the following states:
- [Ready](#Ready) (interrupted by scheduler)
- [Waiting](#Waiting) (interrupted by [I/O](/Systems%20and%20Networking/Unit%201/Architecture/IO%20Devices.md) or event)
- [Terminated](#Terminated) (exit)

### Waiting

In *waiting* state, the process is suspended while waiting for (usually) [I/O](/Systems%20and%20Networking/Unit%201/Architecture/IO%20Devices.md) events. Once the event is done, the process goes back to ready state to be resume execution.

Most of the events are **blocking**: the process can't do anything until the [system call](/Systems%20and%20Networking/Unit%201/Operating%20System/System%20Calls.md) returns. Meanwhile, the [OS](/Systems%20and%20Networking/Unit%201/Operating%20System/Operating%20System.md) sets the process to the waiting state and [schedules](^TK) another process right away, so to avoid the [CPU](/Systems%20and%20Networking/Unit%201/Architecture/CPU.md) being idle.

From here, the process can go in the following states:
- [Ready](#Ready) ([I/O](/Systems%20and%20Networking/Unit%201/Architecture/IO%20Devices.md) or event completion)

### Terminated

In *terminated* state, the process has finished executing and all the resources used by it have to be freed.

## Creating a Process

A process may create other processes through [System Calls](/Systems%20and%20Networking/Unit%201/Operating%20System/System%20Calls.md), the creator process is called **parent** while the created process is called **child**. Each new process is given a unique id (PID) and stores the parent process' id (PPID).

Regarding resources, there are two possibilities:
- The child is a perfect copy of the parent, sharing the same [text and data segments](/Systems%20and%20Networking/Unit%201/Architecture/Virtual%20Memory.md#Virtual%20Address%20Space) in the memory;
- The child is a brand new process, with a different program loaded into the [address space](/Systems%20and%20Networking/Unit%201/Architecture/Virtual%20Memory.md#Virtual%20Address%20Space).

The parent process, after creating the child, has two options:
- Wait for the child process to terminate and then continue executing;
- Run concurrently with the child without being blocked.
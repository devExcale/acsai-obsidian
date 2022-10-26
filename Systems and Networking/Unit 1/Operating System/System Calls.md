# System Calls

[User programs](?TK) cannot run [privileged instructions](/Systems%20and%20Networking/Unit%201/Architecture/Instructions.md#Protected%20Instructions) directly, but they can ask the [Operating System](/Systems%20and%20Networking/Unit%201/Operating%20System/Operating%20System.md) to run the instructions on their behalf in [Kernel mode](/Systems%20and%20Networking/Unit%201/Architecture/CPU.md#Kernel-User%20Mode).

A System Call is an interface to a service provided by the OS, typically written in C/C++. Most programs, though, access these services via a high-level [API](?TK) rather a direct system call.

Examples of high-level API for system calls are:
- GNU C library
- Win32 API
- Java API

## Categories

There are 6 main categories of system call, distinguished by the type of service they offer:
- [Process Control](#Process%20Control)
- [File Management](#File%20Management)
- [Device Management](#Device%20Management)
- [Information Management](#Information%20Management)
- [Communications](#Communications)
- *TK*

### Process Control

Process control system calls may be used to execute all those actions needed to control processes, such as create/execute/terminate processes or get/set process attributes.

It may also be used to allocate/deallocate memory, because memory is a resource needed by processes.

### File Management

File management system calls may be used to execute all those actions needed to operate on files, such as open/read/write/close files, create/move/delete files or get/set file attributes; file management also includes management of directories.

A program does not need to know how the [File System](?TK) works or how it is implemented, because file management system calls provide an abstract way to operate on it.

### Device Management

Device management system calls may be used to execute all those actions needed to operate on devices other than the CPU, such as request/read/write/release a device or get/set device attributes.

The devices may be physical (e.g. disk drives) or virtual (e.g. files, partitions). An OS may *attach* these devices as special files in the [File System](?TK), so that the [File Management](#File%20Management) system calls may be used too.

### Information Management

Information management system calls may be used to execute actions needed to get/set information about the system, such as time, date, system data and attributes.

Information management system calls may also be used to execute **debugging**: executing a program in such a way to halt execution after every instruction, to trace the operation and logic of the program.

### Communications

Communications system calls may be used to communicate with other devices by sending/receiving messages and transfer status information.

There are two main methods to communicate: **message passing** and **shared memory**.

#### Message Passing

The message passing method works by opening a connection between the processes/hosts and then transmitting messages along that connection.

This method must implement system calls to:
- Identify the process/host to communicate with;
- Establish a connection;
- Open and close the connection as needed;
- Transmit messages along the connection;
- Wait for incoming messages (either by [blocking or non-blocking](?TK));
- Delete the connection.

Between the two methods, the message passing method is easier and generally more appropriate for small amounts of data.

#### Shared Memory

The shared memory method works by writing and reading from the same memory space. This implies some restrictions, such:
- Communicating processes and threads must be able to access the same memory space;
- There must be a mechanism to restrict simultaneous access to memory locations;
- Allocate and deallocate memory as needed.

This method is a bit more tricky, but it's more appropriate for large amounts of data.

## System Call Handler

TK

## Parameter Passing

TK

## Common System Calls

| **Name** | **Parameters**                | **Return**       | **Notes** |
| -------- | ----------------------------- | ---------------- | --------- |
| fork     | *none*                        | New process' PID |           |
| execlp   | Path to executable, arguments | TK               |           |
| waitpid  | PID                           | TK               |           |
| sleep    | # of seconds                  | TK               |           |

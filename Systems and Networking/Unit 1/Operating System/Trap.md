# Trap

A *trap* is a signal that prompts the [CPU](/Systems%20and%20Networking/Unit%201/Architecture/CPU.md)/[OS](/Systems%20and%20Networking/Unit%201/Operating%20System/Operating%20System.md) to switch to [kernel mode](/Systems%20and%20Networking/Unit%201/Operating%20System/Protection%20and%20Security.md#Kernel-User%20Mode).

| Trap        | Reason             | Synchronous | Generator |
| ----------- | ------------------ | ----------- | --------- |
| System Call | Request OS service | Yes         | Software  |
| Exception   | Report some fault  | Yes         | Software  |
| Interrupt   | Notify an event    | No          | Hardware  |

## System Call

A [System Call](/Systems%20and%20Networking/Unit%201/Operating%20System/System%20Calls.md) is a trap that is used to request a service from the OS (e.g. read a file).

It's synchronous, in the sense that it is dependent on instructions (e.g. `ecall`), it's generated from user programs.

## Exception

An exception is a trap that is used to report faults in the execution of a program (e.g. division by zero).

It's synchronous, in the sense that it is dependent on instructions (e.g. `div TK`), it's generated from both OS and user programs.

## Interrupt

An interrupt is a trap that is used to notify of events external to the program (e.g. [network packet](?TK) arrived),

It's asynchronous, in the sense that it is independent of instructions and depends on external factors, in fact it's generated by the hardware when said events happen.
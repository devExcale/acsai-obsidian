# Protection and Security

An [Operating System](/Systems%20and%20Networking/Unit%201/Operating%20System/Operating%20System.md) must provide mechanisms to control which users and processes have access to which resources, especially nowadays that everything is connected to a network.

These mechanisms may be implemented by hardware (e.g. [Base-Limit](#Memory%20Protection)) or software (e.g. [System Calls](/Systems%20and%20Networking/Unit%201/Operating%20System/System%20Calls.md))

## Memory Protection

To protect [user programs](?TK) from accessing the [Operating System](/Systems%20and%20Networking/Unit%201/Operating%20System/Operating%20System.md)'s and other programs' memory space, some [processors](/Systems%20and%20Networking/Unit%201/Architecture/CPU.md) offer a simple security feature.

These processors have two dedicated registers:
- **Base,** which contains the address where the program's memory block starts;
- **Limit,** which contains the address where the program's memory block ends.

At program startup, the OS saves the base and limit values; the processor then, every time the program tries to access the memory, checks if the cells the program is trying to access to fall between the base and limit values.

> [!info] Note
> This strategy is applied real-time by the processor, so no software overhead is generated.


## Kernel-User Mode

To offer security and stability, the processor has two modalities: Kernel and User.

In **Kernel mode**, the [Operating System](/Systems%20and%20Networking/Unit%201/Operating%20System/Operating%20System.md) is unrestricted, and can execute any [instruction](/Systems%20and%20Networking/Unit%201/Architecture/Instructions.md), including privileged ones.

On the other hand, in **User mode** the CPU doesn't allow the execution of some **privileged instructions** (TK), to prevent the user from compromising the system. *Some* of actions the user cannot execute are:
- Address [I/O](/Systems%20and%20Networking/Unit%201/Architecture/IO%20Devices.md) directly
- Manipulate the content of the [main memory](/Systems%20and%20Networking/Unit%201/Architecture/Memory.md)
- Switch to kernel mode
- Halt the machine

Programs in user mode can sometimes execute these instructions through [System Calls](?TK).

Kernel and User mode are implemented by the CPU via a *hidden* [register](/Systems%20and%20Networking/Unit%201/Architecture/Registers.md), which uses one bit `{0: kernel, 1: user}` to distinguish between modalities.

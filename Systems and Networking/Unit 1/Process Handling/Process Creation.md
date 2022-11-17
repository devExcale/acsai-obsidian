# Process Creation

[Processes](/Systems%20and%20Networking/Unit%201/Operating%20System/Process.md) are created from other processes via [system calls](/Systems%20and%20Networking/Unit%201/Operating%20System/System%20Calls.md), which results in a hierarchy of processes. The process that has been created is called **child process**, while the creator is called **parent process**.

Each new process is given a new PID, but it also stores the parent's PID (PPID).

## Resources Handling

Regarding the new process' resources, there are two possibilities: *copying* and *spawn*.

- **Copying**

The child is a perfect copy of the parent, the text and data segments are copied into a new [address space](/Systems%20and%20Networking/Unit%201/Architecture/Virtual%20Memory.md#Virtual%20Address%20Space). 

This is the behaviour of the [`fork`](/Systems%20and%20Networking/Unit%201/Operating%20System/System%20Calls.md#Common%20System%20Calls) system call.

- **Spawn**

The child is a brand new process, with a different program loaded into the address space.

This is the behaviour of the `fork` and then [`exec`](/Systems%20and%20Networking/Unit%201/Operating%20System/System%20Calls.md#Common%20System%20Calls) system calls, or Window's `spawn` system call.

## Parent's Behaviour

After creating the child process, the parent process can procede in two ways.

One way is to wait for the child process (or processes) to exit (with the [`wait`](/Systems%20and%20Networking/Unit%201/Operating%20System/System%20Calls.md#Common%20System%20Calls) system call) and then proceed; the other is to run concurrently to the child without being blocked.

# Process Termination

A process usually terminates on its own using the [`exit`](?TK) system call.

The `exit` syscall takes in input an integer, which is the code of termination. The value 0 should indicate a successful completion of the process, while non-zero values indicate that the process has terminated with some kind of problem.

A process may also be terminated if the [OS](/Systems%20and%20Networking/Unit%201/Operating%20System/Operating%20System.md) cannot provide any more resources needed by the process.

A process may also be *killed*:
- by the parent, if no longer needed;
- by another process entirely (e.g. the `kill` command).

## On Process Termination

When a process terminates, all the system resources used by it are freed up (e.g. open files are flushed and closed).

When a parent process is terminated, it's up to the [Operating System](/Systems%20and%20Networking/Unit%201/Operating%20System/Operating%20System.md) to decide what to do with the child processes; the child processes may or may not be allowed to continue. Child processes without a parent are called **orphaned processes**.

> [!tip] Orphaned Processes on UNIX
> On UNIX Operative Systems, orphaned processes are generally inherited by `init`, which proceeds to kill them.

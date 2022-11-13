# Thread

A "thread of control" is the basic unit of CPU utilization, it represents a stream of execution of a sequence of instructions; meaning that every thread will have its own resources needed to execute instructions (i.e. program counter, stack, set of registers), while the associated process sets up everything else (i.e. address space, text, data, resources like files).

Implicitly, in single-thread OS, every process itself is a thread. In multi-thread OS, every process can have multiple threads that execute code while sharing the process' resources.

Threads can collaborate between themself in the same process, so no system calls are required to cooperate. Also, context-switch between threads is faster than 

| **Traditional Processes**                             | **Multi-threaded Processes**                                  |
| ----------------------------------------------------- | ------------------------------------------------------------- |
| Only 1 PC, stack, set of registers                    | 1 PC, stack, set of registers per thread                      |
| Can carry out one sequence of instructions            | Each thread can execute one sequence of instructions          |
| Processes cannot share certain resources (e.g. files) | Threads in a process can share certain resources (e.g. files) |

![Diagram single vs. multi thread](?TK)

Multi-thread programming is useful whenever a process has multiple independent tasks to perform, especially whenever some of the tasks are blocking. Blocking a thread does not preclude the concurrent execution of other threads.

	Example: Word processor
	- Check for spelling and grammar errors
	- Handle user input
	- Save file periodically

Each task could be executed independently using different CPUs to reach best efficiency and performance.
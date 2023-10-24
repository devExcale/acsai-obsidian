# Threads

A "thread of control" is the basic unit of CPU utilization, it represents a stream of execution of a sequence of instructions; meaning that every thread will have its own resources needed to execute instructions (i.e. program counter, stack, set of registers), while the associated process sets up everything else (i.e. address space, text, data, resources like files).

Implicitly, in single-threaded OS's, every process is a thread. In multi-thread OS, every process can have multiple threads that execute code while sharing the process' resources.

Threads can collaborate between themselves in the same process, so no [system calls](/Systems and Networking/Unit 1/Operating System/System Calls.md) are required to cooperate. Also, context-switch between threads is faster than between processes.

| **Traditional Processes**                             | **Multi-threaded Processes**                                  |
| ----------------------------------------------------- | ------------------------------------------------------------- |
| Only 1 PC, stack, set of registers                    | 1 PC, stack, set of registers per thread                      |
| Can carry out one sequence of instructions            | Each thread can execute one sequence of instructions          |
| Processes cannot share certain resources (e.g. files) | Threads in a process can share certain resources (e.g. files) |

![Diagram single vs. multi thread](?TK)

> [!tip] Multitasking
> Multi-thread programming is useful whenever a process has multiple independent tasks to perform, especially whenever some of the tasks are blocking. Blocking a process' thread does not preclude the concurrent execution of the other threads of the process.

	Example: Word processor
	- Check for spelling and grammar errors
	- Handle user input
	- Save file periodically
	(TK: move somewhere other)

Each task could be executed independently using different CPUs to reach best efficiency and performance.

## Advantages of Threads

- **Responsiveness:** a process' main thread could communicate with different processes while the other threads are blocked or slowed down by intensive computations;
- **Resource Sharing:** threads share code, data and address space, inter-thread communication isn't restrictive;
- **Economy:** creating, managing and context-switching threads is faster that performing the same for processes;
- **Scalability:** on multi-processor architectures, a single threaded process can be run on one CPU only, whereas a multi-threaded process may execute the threads parallelly on any available processor/core.

![Multi-core performance example](?TK)

## Thread Pools

Creating threads is less expensive than creating processes, but continuously creating threads in a single process might lead to problems:

- Overhead when creating each thread;
- No limit to the possible number of threads.

**Thread pools** resolve these problems. When the process starts up, a fixed number of threads is created (usually no more than logic units in a CPU) and are put in a waiting state. Whenever it is needed, a thread is picked up from the pool to execute what it is needed to do, and then put it back in the pool.


> [!info] Thread Pool Scheduling
> Thread Pools operate with a [FCFS](/Systems and Networking/Unit 1/Process Handling/Scheduling Algorithms.md#First Come First Serve) scheduling policy.
> 
> If there are no threads available when a new task comes in, the new task will be appended to a queue. When a thread frees up, the first task in the queue will be assigned to that thread.

## Types of Threads

Support for multi-threading can be provided in three ways:
- **Kernel Threads** at kernel level, where the OS itself manages the threads;
- **User Threads** at user level, where threads are managed in the user space with a *thread library*, which doesn't require OS intervention;
- **Lightweight Processes,** a hybrid mix of both kernel and user threads.

> [!info] Lightweight Processes
> Both threading methods have their pros and cons, so in reality threads are implemented using a mix of both.

### Kernel Threads

A *kernel thread* is actually the smallest unit of execution that can be scheduled by the OS. The OS is responsible for managing all threads, so system calls are provided to create and manage the threads from user space.

Kernel threads are schedulable by the CPU, so in addition to the PCB a **TCB** (*Thread Control Block*) is associated to each thread.

#### PROs

TK

#### CONs

TK

### User Threads

*User threads* are threads which are managed entirely by a user-level library, which means the OS doesn't know anything about these threads.

The OS runs these threads as if they were single-threaded processes, meaning most of the advantages of threads relative to the OS are lost

#### PROs

TK

#### CONs

TK

### Lightweight Processes

A better method to implement threads is a hybrid of both [kernel](#Kernel Threads) and [user](#User Threads) threads: mapping user threads to kernel threads.

A number of kernel threads is created by the OS, while user processes create user threads using a thread library; these user threads are then mapped to kernel threads, so that the CPU can actually run the user threads in a (true) multi-threading environment.

#### One to One

Distinct kernel threads handle one user thread each.

This model uses all the advantages of threads, but isn't really different from using all thread kernels.

![One to One Model Diagram](?TK)

#### Many to One

Many user threads are assigned to a single kernel thread.

A process' user threads are assigned to the same single kernel thread, so a single process can't use the real parallelism of multi-threading. Moreover, if a blocking system call is made, the executing user thread blocks the kernel thread, blocking all the other associated user threads.

![Many to One Model Diagram](?TK)

#### Many to Many

Many user threads are multiplexed between an equal or smaller amount of kernel threads.

The many to many model is an advantageous one that enables processes to most (if not all) features of multi-threading processing. User threads from the same process can be split among multiple processors, and blocking system calls do not block the entire process.

![Many to Many Model Diagram](?TK)

#### Two Level

The two level model is a variant of the many to many model with the restriction that certain kernel threads are mapped to a single user thread (one to one).

The only advantage this method provides is an increased flexibility of scheduling policies, so that certain threads have ensured execution time.

![Two Level Model Diagram](?TK)

## Contention Scope

Contention Scope how threads will compete with each other for the use of physical CPUs.

> [!abstract] Process Contention Scope
> Competition occurs between threads of the same process.
> 
> It is the case of user threads mapped to a single kernel thread, or threads managed by a thread library (e.g. *[many-to-one](#Many to One)*, *[many-to-many](#Many to Many)*).

> [!abstract] System Contention Scope
> Competition occurs between kernel threads and involves the [system scheduler](/Systems and Networking/Unit 1/Process Handling/Process Scheduling.md#Process Scheduler).
> 
> 

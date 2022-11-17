# Scheduling Algorithms

Scheduling processes is no easy task, there are multiple variables to keep track of and many criteria to account for.

| **TK**              | **Goal**    | **Description**                                                                                                                               |
| ------------------- | ----------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **CPU utilization** | 📈 Maximize | Ideally, the CPU should be busy 100% of the time. On real systems it should range from 40% (lightly loaded) to 90% (heavily loaded).          |
| **Throughput**      | 📈 Maximize | The number of processes is completed in a time unit. It is highly volatile (based on the [job](?TK) length).                                  |
| **Turnaround time** | 📉 Minimize | Time required for a process to complete from submission to completion, including waiting time (in the queue).                                 |
| **Waiting time**    | 📉 Minimize | Time spent by the processes in the ready queue waiting to run.                                                                                |
| **Response time**   | 📉 Minimize | Usually applicable to interactive processes, it's the time measured from the issuance of a command to the begin of a response to the command. |

> [!warning] Waiting time
> The waiting time mentioned above is **not** the waiting state! The [scheduler](Systems%20and%20Networking/Unit%201/Process%20Handling/Process%20Scheduling.md#Process%20Scheduler) doesn't have control over processes in waiting state, it can only manage the ones in ready and running states.

## Scheduling Policies

The goals mentioned above can't be reached together and there must be some kind of trade-off, based on the scheduling policy chosen.

The scheduling policy of an **interactive system** says to:
- Minimize the *average* response time, to provide output to the user as quickly as possible;
- Minimize the *maximum* response time, to relieve the worst-case scenario of a non-responding program;
- Minimize the *variance* of response time, because users prefer a predictable system rather than an inconsistent one.

The scheduling policy of a **batch system** says to:
- Maximize throughput, by minimizing overhead (i.e. context switches) and using system resources (CPU and I/O devices) in the most efficient way;
- Minimize waiting time, by giving time slices of the same size to all processes.

## First Come First Serve

**FCFS** is a simple scheduling algorithm composed of just one FIFO queue.

When the currently running process changes states, the scheduler looks for the first process in the queue. If it is ready it is scheduled for execution (the dispatcher is called for this process), otherwise it is put at the end of the queue (e.g. if it's in waiting state).

When the currently running process changes states, two things can happen:
- **it completes execution,** the scheduler won't have to do anything;
- **it goes into waiting state,** the scheduler will place it back at the end of the queue.



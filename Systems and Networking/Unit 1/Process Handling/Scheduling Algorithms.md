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

Some of these variables are dependent on other, so they can be computed through some formulas.

- $T_\text{arrival}=$ **arrival time** (in the scheduling system as a ready process)
- $T_\text{completion}=$ **completion time** (when the process completes its execution)
- $T_\text{burst}=$ **burst time** (time required by a process for CPU execution)
- $T_\text{turnaround} = T_\text{completion} - T_\text{arrival}$
- $T_\text{waiting} = T_\text{turnaround} - T_\text{burst}$

## List of Scheduling Algorithms

1. [First Come First Serve](#First%20Come%20First%20Serve)
2. [Round Robin](#Round%20Robin)
3. [Shortest Job First](#Shortest%20Job%20First)
4. [Priority Scheduling](#Priority%20Scheduling)
5. [Multilevel Queue](#Multilevel%20Queue)
6. [Multilevel Feedback Queue](#Multilevel%20Feedback%20Queue)

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

> [!info] Non-preemptive
> A process may continue running indefinitely until it waits or terminates by itself, which is why FCFS is a [non-preemptive](/Systems%20and%20Networking/Unit%201/Process%20Handling/Process%20Scheduling.md#Preemptive%20Scheduling) scheduling algorithm.

### PROs

- Very simple

### CONs

- Waiting time is highly variable (short jobs may sit behind long ones)
- CPU-bound jobs will force I/O-bound ones to wait (**convoy effect**)

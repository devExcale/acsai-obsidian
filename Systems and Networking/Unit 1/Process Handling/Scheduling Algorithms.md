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
4. [Priority](#Priority)
5. [Multilevel Queue](#Multilevel%20Queue)
6. [Multilevel Feedback Queue](#Multilevel%20Feedback%20Queue)
7. [Lottery Scheduling](#Lottery%20Scheduling)

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

- **PROs**
1. Very simple

- **CONs**
3. Waiting time is highly variable (short jobs may sit behind long ones)
4. CPU-bound jobs will force I/O-bound ones to wait (**convoy effect**)

## Round Robin

**Round Robin** is a simple scheduling algorithm that works just like [FCFS](#First%20Come%20First%20Serve), but [CPU-bursts](?TK) are assigned with a *time slice* (or *time quantum*) limit.

If the current job the CPU is executing finishes before the time slice ends, then the job is replaced with another one just like FCFS. If instead the time slice ends first, the job is switched with the next one and it is put in the ready queue again.

This scheduling algorithm makes extensive use of [timers](/Systems%20and%20Networking/Unit%201/Architecture/Timer.md): every time the time slice ends, the timer generates an interrupt that the [dispatcher](/Systems%20and%20Networking/Unit%201/Process%20Handling/Process%20Scheduling.md#Dispatcher) uses to switch the jobs.

> [!info] Preemptive
> Unless the time it takes to complete the job is less than the time slice, processes are interrupted at least one during execution, which is why Round Robin is a [preemptive](/Systems%20and%20Networking/Unit%201/Process%20Handling/Process%20Scheduling.md#Preemptive%20Scheduling) scheduling algorithm.

Round Robin is a *fair* scheduling algorithm, because it shares the CPU equally among the jobs, even though the average waiting time can be longer than other algorithms; once a job has been given a time slice, the dispatcher must give all the other jobs a time slice before giving it back to the initial job.

> [!warning] Performance
> The performance of Round Robin is dependant on the length of the time slice.
> - A large time slice turns RR to FCFS, because jobs will finish on their own and won't be ever interrupted out of the CPU.
> - A small time slice will result in more context switch, which is more overhead and less effective CPU utilization (*low throughput*).

## Shortest Job First

**Shortest Job First** is a scheduling algorithm that orders the jobs to be scheduled by the *expected* amount of work (CPU-burst) until the next I/O operation or completion, in an ascending way.

> [!info] Non-preemptive
> SJF is a non-preemptive scheduling algorithm, because it lets jobs block by themselves when needed. There's also a preemptive variant called **SRTF**: whenever a new job with a shorter CPU-burst than the current job arrives in the ready queue, that job is immediately scheduled, blocking the current one. 

It is optimal to minimize the average waiting time, but the difficulty is is found in predicting the amount of CPU utilization of a job. It could be simple if programs were linear, but most programs include conditional statements and jumps, which makes it close to impossible to compute.

> [!warning] Starvation
> CPU-bound jobs with long CPU utilization could go into *starvation* (won't get scheduled), because new short jobs will get scheduled before them.

## Priority

Priority is a scheduling technique in which every job is assigned a *priority*, jobs with higher priorities get scheduled first. These priorities can be assigned either *internally* by the [OS](/Systems%20and%20Networking/Unit%201/Operating%20System/Operating%20System.md) or externally by the user.

Priorities are implemented using integers, but there is no convention for the ordering. Usually, low numbers mean higher priority (with 0 being the highest one).

> [!info] (Non-)preemptive
> Priority scheduling can be both preemptive and non-preemptive: either schedule jobs with the same priority preemptively using another scheduling algorithm such as round robin, or wait for the current job to block or terminate by itself.

> [!tip] Shortest Job First
> SJF can be seen as a priority scheduling algorithm: priorities correspond to the expected CPU time and lower priorities (shortest times) get scheduled first.

> [!warning] Starvation
> Jobs with low priority can go in starvation, i.e. jobs won't get scheduled because new jobs with higher priority get scheduled first. This problem can be solved with **aging**: priority of jobs is increased proportionally to the time they wait in queue, so that eventually they get scheduled.


## Multilevel Queue

Multilevel Queue is a scheduling algorithm that divides jobs into multiple queues, each queue is distinguished by a job category. Once a job is inserted into a queue in cannot change queue.

So, there are two levels of scheduling: a higher level scheduling to select the queue, and a lower level scheduling to select which process will be given the CPU. Each queue can implement whichever scheduling algorithm it's best suit for the jobs.

> [!abstract] Higher Level Scheduling
> Usually, the higher level scheduling is one of the following.
> - *[Strict Priority](#Priority):* each queue is assigned different priorities, higher priorities get scheduled first.
> - *[Round Robin](#Round%20Robin):* each queue gets a time slice, which can be of different sizes too.

![MLQ example](?TK)

## Multilevel Feedback Queue

Multilevel Feedback Queue is a scheduling algorithm similar to [MLQ](#Multilevel%20Queue), except the fact that jobs can change queue.

This is most appropriate when a process instructions may change from CPU-intensive to I/O-intensive, going from a higher to a lower priority. **Aging** can also be applied easier, by moving the job from a lower to a higher priority queue.

Higher priority (i.e. lower integers) queues have a larger time slice.

1. By default, jobs start in the highest priority queue;
2. If the job's time slice expires (not enough time), increase the priority;
3. If the job's time slice doesn't expire (too much time), decrease the priority.

MLFQ is the most flexible scheduling algorithm, but it's also the most complex to implement. There are many parameters that can influence it:
- Number of queues
- Scheduling algorithm for each queue
- Method used to move jobs across queues
- Method used to choose the initial queue for a job

> [!info] Fairness
> MLFQ tries to mimic the optimal behaviour of [SJF](#Shortest%20Job%20First) in terms of waiting time; it explicitly promotes short jobs, but it could be unfair to longer jobs.

## Lottery Scheduling

Every job is given a certain number of lottery tickets. On each time slice, a uniformly random winning ticket is selected, CPU time will be assigned to the owner of the ticket.

The best policy would be to give more tickets to short running jobs and less tickets to long running jobs (similar to SJF). To avoid starvations, each job gets at least one ticket, so it can be selected anytime. Adding and deleting jobs affects the other jobs *proportionally* and not with a fixed rate.

> [!info] Randomized Scheduler
> This is the only example of **randomized** scheduler, rather than deterministic.



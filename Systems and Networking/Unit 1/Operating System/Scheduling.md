# Scheduling

## Priority

Priority is a scheduling technique in which every [process](/Systems%20and%20Networking/Unit%201/Operating%20System/Process.md) has an assigned *priority*, and the dispatcher runs the processes with highest priority first. These priorities can be assigned either *internally* in the [OS](/Systems%20and%20Networking/Unit%201/Operating%20System/Operating%20System.md) or externally.

Priority is implemented by integers but there's no convention for it, which could lead to problems:
- No certain number for "high priority"
- Usually, low numbers mean higher priority (0 is the highest priority)

TK characteristics, criteria, issues

## Shortest Job First

## Multi-Level Queue

Multilevel queue is a scheduling technique in which there are multiple queues, one for each [job category](?TK). Once a job is inserted into a queue it cannot change queue.

Each queue, then, can implement whichever scheduling algorithm is best suit for the jobs. Usually, scheduling between queues can happen in two ways:
- **strict priority,** we assign a priority to each queue and schedule jobs of higher priority first;
- **round robin,** each queue gets a time slice, possibly of different sizes.

![MLQ Diagram](?TK)

## Multi-Level Feedback Queue

Multilevel Feedback Queue is a scheduling technique similar to [MLQ](#Multi-Level%20Queue), but jobs can change priority (schedule).

This is most appropriate when a process instructions may change from CPU-intensive to I/O-intensive, going from a higher to a lower priority. This is also useful to compensate **aging**, moving the job from a lower to a higher priority.

Lower priority queues have a larger time slice.

1. By default, jobs start in the highest priority queue;
2. If the job's time slice expires (not enough time), drop the priority by one level;
3. If the job's time slice doesn't expire (too much time), increase the priority by one level.
4. TK

MLFQ is the most flexible scheduling algorithm, but it's also the most complex to implement. There are many parameters that can influence it:
- Number of queues
- Scheduling algorithm for each queue
- Method used to move jobs across queues
- Method used to choose the initial queue for a job

MLFQ tries to mimic the optimal behaviour of [SJF](?TK) in terms of waiting time; it explicitly promotes short jobs (I/O ones), but it could be unfair to

## Lottery Scheduling

Every job is given a certain number of lottery tickets. On each time slice, a uniformly random winning ticket is selected, CPU time will be assigned to the owner of the ticket.

The best policy would be to give more tickets to short running jobs and less tickets to long running jobs (similar to SJF). To avoid starvations, each job gets at least one ticket, so it can be selected anytime. Adding and deleting jobs affects the other jobs *proportionally* and not with a fixed rate.

> [!tip] Note
> This is the only example of **randomized** scheduler, rather than deterministic.



# Timer

A timer is an hardware component which enables [CPU](/Systems and Networking/Unit 1/Architecture/CPU.md) [scheduling](?TK).

Physically it's just a clock with microseconds accuracy, but at every fixed interval of time (e.g. 100 microseconds) it generates an [interrupt](/Systems and Networking/Unit 1/Operating System/Trap.md#Interrupt) that notifies the scheduler to take over and decide which process to execute next.

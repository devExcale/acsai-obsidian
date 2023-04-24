# Timer

A timer is an hardware component which enables [CPU](/Systems%20and%20Networking/Unit%201/Architecture/CPU.md) [scheduling](?TK).

Physically it's just a clock with microseconds accuracy, but at every fixed interval of time (e.g. 100 microseconds) it generates an [interrupt](/Systems%20and%20Networking/Unit%201/Operating%20System/Trap.md#Interrupt) that notifies the scheduler to take over and decide which process to execute next.

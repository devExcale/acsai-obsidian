# Operating System

There isn't a universal definition for an **Operating System**, but one could say that it is an implementation of a *virtual machine* which should be easier to program than bare [hardware](High-Level%20Computer%20Architecture).

An **OS** stands between users (or application programs) and the underlying hardware, and it is the only mean to access the hardware.

## Parts

A system is distinguished into two parts.

### Kernel
It's the core of the OS, always running and managing the real resources;

### System Programs
It's anything else in the OS other than the Kernel.

## Features

The features of an OS are many:
- **Resource Manager:** manage physical resources (CPU, memory, I/o, etc.) with efficiency;
- **Virtual Machine:** virtualize any physical resource, to give the user and programs the illusion of infinite resources (and for efficiency reasons);
- **Separate HW/SW:** provides a set of API's, to control the access to physical hardware.

## Structure
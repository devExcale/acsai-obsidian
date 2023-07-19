# I/O Devices

*Input/Output Devices* are devices that let the user interact with the machine.

We can find multiple categories of I/O Devices:
- **Storage**, e.g. USB sticks
- **Communications**, e.g. headsets
- **User Interface**, e.g. monitors
- etc.

Each I/O Device is composed of two parts: the **physical device** and the **device controller**.

TODO: OS Software Abstraction diagram

## Physical Device

A *physical device* is the physical circuit/component of an I/O device, it directly interacts with the user.

A physical device does *not* necessarily need to communicate with a machine, because the device controller acts as a medium.

## Device Controller

A *device controller* is a circuit (chip or set of chips) that controls one or more physical devices.

The behaviour of the device controller is independent of the [OS](/Systems and Networking/Unit 1/Operating System/Operating System.md), instead it's the OS that [adapts to the controller](#Device Driver).

Like the CPU, every controller has some registers used to configure/interact with the device, which can be used by the CPU to communicate with it.

- **Status Registers:** provide information to the CPU about the status of the device (e.g. ready, busy, error);
- **Configuration/Control Registers:** can be used by the CPU to configure and control the device;
- **Data Registers:** can be used to share (read/write) data between the CPU and the device.

## Device Driver

I/O Devices and Operating Systems might speak different languages, so there has to be an intermedium that translates.

This medium is the *device driver*, a light middleware (software) that translates communications between devices and OS's.

## Communicating with Devices

TODO: port vs memory mapped IO

## I/O Tasks

// TODO

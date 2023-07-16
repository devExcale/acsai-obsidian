# Memory

Memory is a kind of storage, whether digital or analogic. There are different kinds of memory, each with its own properties.

![Image of Memory Hierarchy](?TK)

## Properties

### Volatile / Non-volatile

A volatile memory loses all of its contents when powered off, it isn't persistent between different machine boots.

A non-volatile memory, on the other hand, keeps its contents when powered off, so it persists data across different machine boots.

### Access time

Different storage types have different access times. These are dependent on the internal structure of the storage.

Usually, it is inversely proportional to the storage capacity.

### Storage type

Based on its use, we can define three types of storages.

1. **Primary:** used directly by the [CPU](/Systems and Networking/Unit 1/Architecture/CPU.md)
2. **Secondary:** used as mass storage
3. **Tertiary:** nowadays deprecated

## Hierarchy

A hierarchy of some types of memories, ranked by increasing access time and decreasing cost.

| **Memory**        | **Type**  | **Volatile** | **Access** time | **Capacity**    |
| ----------------- | --------- | ------------ | --------------- | --------------- |
| Register          | Primary   | yes          | 1 cc            | 32 or 64 bit    |
| Cache             | Primary   | yes          | 2 to 10 cc      | 100 KB to 10 MB |
| Main Memory       | Primary   | yes          | 50 to 100 cc    | 4 to 128 GB     |
| Solid-State Drive | Secondary | no           | ?               | 128 GB to 2 TB  |
| Hard-Disk Drive   | Secondary | no           | ~40M cc         | 256 GB to 10 TB |
| Optical Disk      | Tertiary  | no           | ?               | ?               |
| Magnetic Tapes    | Tertiary  | no           | ?               | ?               |

> [!info]
> *cc stands for [Clock Cycle](/Systems and Networking/Unit 1/Architecture/CPU.md#Instruction Cycle).*

> [!warning] Note
> Note: some cells are marked as unknown because the values between two different physical supports aren't equal. But the hierarchy still applies, so an average value should be found between the values of the previous and next rows.

## Representation

A memory can be seen a a sequence of *cells*, each cell stores a *[byte](?)*.

Every cell has an **address**, which CPUs and I/O devices can use to access (read/write) the memory.

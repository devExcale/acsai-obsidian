# Magnetic Disk

The magnetic disk is a mass storage device, used to store large amount of data; the drawback, though, is that it is much slower than the main memory.

With magnetic disks, two categories can be distinguished:
- **Hard Disk**, composed of metal disks (higher capacity);
- **Floppy Disk**, composed of flexible disks (lower capacity but portable).

## Structure

The magnetic disk drives are composed of multiple disks, attached to a *spindle* that rotates them. An *arm assembly* controls some arms (two per disk, as each disk has two working surfaces) with a *magnetic head* that does the reading and writing.

Each surface is composed of multiple *tracks* (concentric rings), the set of all tracks at the same radius from the spindle is called *cylinder*. The track, then, is further divided into *sectors*, which is the smallest addressable unit, with a memory size of 512 bytes.

![Image of a Magnetic Disk](/assets/Magnetic%20Disk%20Structure.jpg)

## Capacity

The overall capacity of the drive is given by

$$\large
	\text{Capacity} = B \cdot S \cdot T \cdot H
$$

where:

- $B$ is the byte capacity of every sector;
- $S$ is the number of sectors per track;
- $T$ is the number of tracks per surface;
- $H$ is the number of heads, i.e. number of surfaces.

> [!tip] Sectors Density
> Old magnetic disks had the same number of sectors in each track, meaning the inner track had a much higher density of sectors compared to the outer ring. 
> 
> Nowadays, magnetic disks have different numbers of sectors per track, so as to keep the density the same.

## Referencing

Each block of data in a magnetic disk can be referenced using a triple:

- **Head**
- **Cylinder / Track**
- **Sector**

> [!note] Cylinder Index
> Cylinders are indexed starting from the outer layer, i.e. the outermost track has index 0.

## Data Transfer

Data transfer of magnetic disks is composed of three steps:

- **Positioning Time**
- **Rotational Delay**
- **Transfer Time**

> [!note] Positioning Time
> Also called *Seek Time* or *Random Access Time*, it's the time that's needed for the heads to get to a specific track, including the time to stop. It's the step which takes the most amount of time.

> [!note] Rotational Delay
> It's the time that's needed for the disk to rotate to get a specific sector under the head. It ranges from 0 to a full revolution, which for a disk with average speed (7200 rpm or 120 rps) takes slightly more than 8 ms.

> [!note] Transfer Time
> It's the time taken by the head to actually read the contents of the entire sector.

The transfer rate of a magnetic disk is given by the capacity of a sector (512B) over the sum of all the steps needed to read data from one sector (i.e. seek time, rotational delay, transfer time).

# Disk Scheduling

When using [magnetic disks](/Systems and Networking/Unit 1/Storage Management/Magnetic Disk.md), the factor that most impacts I/O time isn't the time taken to read a single sector, but the delay to get the head from where it is to the correct sector (i.e. [seek time](/Systems and Networking/Unit 1/Storage Management/Magnetic Disk.md#Data Transfer)).

To help reduce the seek time, different algorithms to schedule incoming I/O requests can be applied:

- First Come First Served
- Shortest Seek Time First
- SCAN
- C-SCAN
- LOOK
- C-LOOK

> [!warning] Arm Speed
> Note that the arm speed isn't linear, but has acceleration and deceleration. The arm has to stop in a particular track if the sector isn't under the head. This means that the arm speed is a factor to consider when comparing disk scheduling algorithms.

## First Come First Served

The *First Come First Served* (FCFS) disk scheduling algorithm serves requests in the order they arrive.

It's easy to implement, but performance may degrade if requests are sparce between them.

## Shortest Seek Time First

The *Shortest Seek Time First* (SSTF) disk scheduling algorithm greedily serves a set of requests based on the distance of the requests from the head. The algorithm will serve first the request that's the closest to the current position of the head.

It can be implemented via a sorted list, and the overhead needed to keep the list sorted can be negligible because it'll take less time than the actual seek time.

In a global context, SSTF can increase the distance travelled by the head and could cause starvation (if one request is far from the head and closer requests keep coming).

> [!example] Global Inefficiency
> Take, as example, the set of requests {10, 20, 30, 40, 61} and the starting position of the head is 50. SSTF will first get all the requests other than 61, then in the end get to track 61, having travelled 91 tracks.
> 
> If it were to get to track 61 first and then get to the others, the head would have travelled only 62 tracks.

## SCAN

The *SCAN* disk scheduling algorithm continuously moves the head back and forth (0 to 100 and viceversa), visiting all the tracks in the meanwhile. Requests are served while the head is visiting the requested track.

Like SSTF, SCAN can implemented via a sorted list, where the head or the tail (depending on the current direction) contains the next request to serve, but unlike SSTF there's no risk of starvation, even though it's unfair to requests with close track but in the opposite direction (e.g. head at 50 going to 0, request for 51 comes in).

## LOOK

The *LOOK* disk scheduling algorithm works just like [SCAN](#SCAN), but instead of going from end to end, the head will turn back once the last request close to the end has been served.

> [!example]
> Head is at 20, going to track 0. The closes request to the end is 18: after having served the request on track 18, the head turns back in the opposite direction.

## C-SCAN

The *SCAN* disk scheduling algorithm works just like *SCAN*, but instead of going back and forth serving requests, the head gets reset back every time it reaches the end, without serving requests when going back.

## C-LOOK

The *C-LOOK* disk scheduling algorithm works just like *LOOK* TK

# Packet Delay

[Packets](/Systems and Networking/Unit 2/Internet/Packet.md) sent with [packet switching](/Systems and Networking/Unit 2/Network Core.md#Packet Switching) can be **lost** and suffer **delay**:

- Packets lost need to be sent again;
- **Every** packet suffers from delay that is given from different sources.

**Packet Delay** is given from the following sources.

| Order | Type             | Description                                                                      |
| ----- | ---------------- | -------------------------------------------------------------------------------- |
| 1.    | **Processing**   | Every router checks for errors in the packet and which way it should take.       |
| 2.    | **Queueing**     | The packet has to wait for other packets before itself to be sent.               |
| 3.    | **Transmission** | Depends on the length of the packet. Longer packets take more to be transmitted. |
| 4.    | **Propagation**  | Depends on the length and propagation speed of the physical mean.                |

The whole delay a packet can suffer is given from the following sum.

$$\large d_\text{tot} = d_\text{proc} + d_\text{queue} + d_\text{transm} + d_\text{prop} \ [s]$$

## Processing Delay

Processing delay is the time routers take to check for errors in the packet, plus the time it takes to decide where to send it. Usually, it's in the order of microseconds.

## Queueing Delay

Queueing delay is the time a packet spends in the router's waiting queue, before it is forwarded. It's highly variables, and depends on the level of congestion of the router.

## Transmission Delay

Transmission delay is the time it takes a *whole* packet to be sent from the router (*output speed*). It is dependent on the **packet length** $L\ [bits]$ and the **transmission rate** $R\ [bps=\frac{bits}{s}]$, and is given from the following ratio.

$$\large d_\text{transm} = \frac{L}{R}\ [s]$$

## Propagation Delay

Propagation delay is the time it takes the signal to travel through the whole [transport mean](/Systems and Networking/Unit 2/Transport Means.md). It is dependent on the **length of the mean** $d\ [m]$ and the **propagation speed** $s\ [\frac{m}{s}]$, and is given from the following ratio.

$$\large d_\text{prop} = \frac{d}{s}\ [s]$$

## Traffic Intensity

Take a queue with 10 packets: the first packet will be sent immediately, while the last packet will have to wait for 9 packets to be sent.

Now, imagine an **average packet arrival rate** $a \ [\frac{packets}{s}]$, meaning a rate of how many packets arrive in a second. We can use this variable to compute an average queueing rate, where $L,R$ are the same variables from the [Transmission Delay](#transmission delay).

$$\large
	\text{traffic intensity} = \frac{L \cdot a}{R}
	= \frac{\text{bits incoming}}{\text{bits outgoing}}
	= a \cdot d_\text{transm}
$$

Traffic intensity is the ratio of how many bits are arriving vs. how many bits are being transmitted. Different values of the ratio mean different things:

- $(0 \le r < 1)$ The queue is decreasing or packets are being forwarded immediately;
- $(r = 1)$ The average number of packets in the queue is fixed, neither increasing nor decreasing;
- $(r > 1)$ The packets in the queue are increasing and, if full, arriving packets are lost (infinite average queueing delay).

## Throughput

Throughput is the rate at which bits are actually delivered from the sender to the receiver, measured in $\frac{bits}{s}$. It can be either **instantaneous** (at a given point in time) or **average** (over a span of time).

Throughput is measured from sender to receiver, meaning we need to account for all routers/[links](?TK) in the path. In the path there's always a **bottleneck**, a link that caps the transfer rate to a certain limit: if in a path there's a link which supports at max 1K bits/s, even though other links could support higher speeds the minimum speed will always be 1K bits/s (meaning, no matter what other higher speeds there are, the [transmission delay](#Transmission Delay) will always be affected the most by the lower speed).

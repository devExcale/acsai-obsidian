## Network Core

A *network core* is a smaller network of connected [routers](?Systems%20and%20Networking/Unit%202/Devices.md#Router). Multiple network cores are interconnected to provide long-distance connections.

Routers in a network core are connected in a [partial mesh](?TK) to provide reliability. To send a packet from a source [host](?Systems%20and%20Networking/Unit%202/Devices.md#Host) to a destination host, routers [forward](#Forwarding) [packets](Systems%20and%20Networking/Unit%202/Packets/Packet.md) to the next router across an [optimal path](#Routing).

### Forwarding

Forwarding is an action that consists in moving arriving [packets](Systems%20and%20Networking/Unit%202/Packets/Packet.md) to other [Router](/Systems%20and%20Networking/Unit%202/Devices.md#Router). The goal of this action is to move the packet towards its destination.

### Routing

Routing is an action that consists in finding the *optimal* path along the connected network cores to send [packets](Systems%20and%20Networking/Unit%202/Packets/Packet.md) in the most efficient way from source to destination.

### Packet Switching

With packet switching, [packets](Systems%20and%20Networking/Unit%202/Packets/Packet.md) don't have a fixed path to go through. Instead, [routers](/Systems%20and%20Networking/Unit%202/Devices.md#Router) compute an optimal path of routers to transfer a packet from the sending host to the receiving host. In this way, go through one router to another, without having to propagate to all the network.

If a packet has length $L\ [bits]$ and walks through a channel with transmission rate $R\ [\frac{\text{bits}}{\text{bits/s}}]$, a packet will take $\frac{L}{R}$ seconds to be fully transmitted.

TK Before *forwarding* packets to the next link, a router must fully receive the packet (**store and forward**). Internally, routers have a queue for packets. If the arrival rate exceeds the transmission rate, packets are put in this queue. If more packets than the queue can contain arrive, these packets are dropped (lost).

### Circuit Switching

In circuit switching, routers themselves don't process [packets](Systems%20and%20Networking/Unit%202/Packets/Packet.md). Instead, they open a connection between the incoming [link](?TK) and the destination link, so that the hosts can communicate directly.

It is like a direct mean between the hosts, with no sharing of resources with third parties. Old telephone networks relied on this method.

![Diagram of Circuit Switching](?TK)

There are two methods to share the same channel: **FDM** and **TDM**.

#### Frequency Division Multiplexing

FDM divides the frequency into bands, each communication instance can happen between the bounds of an assigned band. The trade-off in respect to TDM is that communications can happen anytime.

#### Time Division Multiplexing

TDM divides time into slots, each communication instance is assigned slots when hosts can communicate. The trade-off in respect to FDM is that communications can allocate all the bandwidth.
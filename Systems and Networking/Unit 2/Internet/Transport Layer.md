# Transport Layer

The **Transport Layer** is the fourth layer of the [Internet Protocol Stack](/Systems and Networking/Unit 2/Internet/Layered Structure.md#Layered Structure), its reason is to provide a logical channel for communication between two applications across the network.

Transport-layer features are implemented in end hosts only, routers and switches work from the network layer down. To send a message from one host to another:

1. On the sending host, the transport layer breaks the **message** in smaller pieces to which is added a *transport header*. The final packets are called **segments**;
2. The segments are then passed to the network layer (segments are now called **datagrams**), which does its job and routes the datagrams to the destination host;
3. On the destination host, the network layer receives the datagrams, unpacks the segments and passes them to the transport layer;
4. The transport layer processes the received segments, builds the message and passes it to the application layer.

The internet works on two transport protocols: [**TCP**](/Systems and Networking/Unit 2/Protocols/TCP.md) and [**UDP**](/Systems and Networking/Unit 2/Protocols/UDP.md), each with its set of services. Some of the services that both *cannot* provide, though, are *delay guarantee* (i.e. maximum delay) and *bandwidth guarantee* (i.e. minimum throughput).

| **Protocol** | **Reliability** | **Packet Ordering** | **Connection** |
| ------------ | --------------- | ------------------- | -------------- |
| *TCP*        | Yes             | Yes                 | Yes            |
| *UDP*        | No              | No                  | No             |

## Multiplexing and Demultiplexing

As already said, the transport layer provides a virtual channel between applications that want to communicate. The base of this channel is sockets: the source application writes into the socket and the destination application reads from the socket.

An host, though, can hold many connections, each of which can be accessed through socket; when a packet arrives, the transport layer has to redirect the packet through the right socket.

Sockets are handled with the following criteria:
- **UDP sockets** (connectionless) are identified through the two-tuple **destination address and port**, any packet (regardless of source) sent to the receiving host will be forwarded through the socket identified by the specified port;
- **TCP sockets** (connection) are identified through the four-tuple **source address and port, destination address an port**, any packet sent to the receiving host will be forwarded to the socket identified by the specified tuple. If no socket is identified by that tuple, a new socket is created.

> [!warning] UDP sockets
> 
> UDP sockets don't recognize the source (i.e. who sent the packet), so it is possible that applications from multiple hosts could talk to one receiver.




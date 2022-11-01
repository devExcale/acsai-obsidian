# Application Layer

Developing an application nowadays is significantly easier, considering that [layers](/Systems%20and%20Networking/Unit%202/Packets/Layered%20Structure.md) other than the [application layer](/Systems%20and%20Networking/Unit%202/Packets/Layered%20Structure.md#Application) are already implemented. The only thing a developer should think of are:
- Application logic;
- Application architecture;
- Which transport protocol to use.

The application architecture dictates the role of each host and the relation between them.

## Client-Server Architecture

The Client-Server is an architecture paradigm where some hosts, namely the **servers**, provide services to the end users, called **clients**.

Servers and clients each have their characteristics.

**Server:**
- Always on
- (Usually) owned by a service provider
- Provides services to clients
- Could collaborate with other servers
- Has a well-known [address](?TK) (either [IP](?TK) or [DNS](?TK))

**Client:**
- It's the end user
- Requests services from servers
- Does not communicate directly with other clients

Often, just one server cannot satisfy the request of all clients. To fix this problem, more than one servers are installed in specialized [data centres](?TK), so that the servers can share requests and load of work.

## Peer-to-Peer Architecture

A.K.A. **P2P**, its an architecture paradigm with no distinction between clients and servers. Each **peer** (host) provides functionalities as both client and server, and peers can communicate freely and directly between each other. Peers are not machines owned by service providers, but are instead machines owned by end users.

Like a client connects to a known server, a peer must know other peers to communicate with them. There are some ways to discover peers:
- Use a centralized system (server) which can list connected peers;
- Register known peers by hand;
- Scan the network for other peers.

P2P is more "efficient" than Client-Server in bandwidth usage and workload sharing: peers don't connect to one server only (huge bandwidth usage) that needs to handle all the requests (high computational power needed), but peers themselves handle requests. This means that there is a lower bandwidth usage (peers are sparse) and workload is shared (between peers), at the cost of the initial setup for peers discovery and other drawbacks (mainly security and reliability).

## Communication

An application/program that runs on a machine is just a [process](/Systems%20and%20Networking/Unit%201/Operating%20System/Process.md), so applications that need to communicate can do so like processes: by [exchanging messages](?TK).

These [messages](/Systems%20and%20Networking/Unit%202/Packets/Layered%20Structure.md#Application) can be exchanged over the network too, thanks to the [layered structure](/Systems%20and%20Networking/Unit%202/Packets/Layered%20Structure.md) of packets.

Processes over the network can communicate through **sockets**: a software interface, a virtual channel used by the machine to transfer and receive packets. In a communication there are two sockets involved, one for each host.

A socket is distinguished by two things:
- An [IP address](?TK), which identifies an host;
- A port, which identifies a service (or more generally, a "channel") on the host.
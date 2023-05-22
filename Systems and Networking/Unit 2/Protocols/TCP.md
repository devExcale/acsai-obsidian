# Transfer Control Protocol

The Transfer Control Protocol is a [transport layer](Systems%20and%20Networking/Unit%202/Internet/Transport%20Layer.md) protocol based on the [Reliable Data Transfer](/Systems%20and%20Networking/Unit%202/Protocols/RDT.md) 3.0 protocol. It extends RDT by adding other features such as congestion control, flow control and connections.

Unlike RDT, in TCP both hosts of a conversation are both the sender and the receiver of a connection. A TCP connection is opened via a **three-way handshake**:
- $A$ sends a SYN packet with a *random* sequence number $x$;
- $B$ sends an ACK/SYN packet for $x+1$, while setting the packet sequence number to a random $y$;
- $A$ sends an ACK packet for $y+1$ with sequence number $x+1$

> [!note] Sequence Numbers and ACK
> 
> Because both hosts are both senders and receivers in the connection, when a receiver is replying to a packet with sequence number $x$, it must send a new packet with its own sequence number $y$ acknowledging packet $x+1$; then, the other party has to send packet $x+1$ acknowledging packet $y+1$.
> 
> Unlike RDT, hosts in a TCP connection acknowledge the sequence number of the next expected packet instead of the received packet.

![Timeline of a TCP handshake](assets/tcp_handshake.png)


## TCP Segment Structure

![Packet structure of a TCP segment](assets/tcp_segment.png)

1.  **Source Port:** The source port is a 16-bit field that identifies the port number of the sender's application or process.
2.  **Destination Port:** The destination port is also a 16-bit field that specifies the port number of the receiver's application or process.
3.  **Sequence Number:** This 32-bit field indicates the sequence number of the first data octet (byte) in the TCP segment. It helps in ordering and reassembling received data.
4.  **Acknowledgment Number:** In an ACK (acknowledgment) packet, the 32-bit acknowledgment number field indicates the next sequence number the sender expects to receive. It acknowledges the receipt of data up to that sequence number.
5.  **Data Offset:** The 4-bit data offset field specifies the size of the TCP header in 32-bit words. It determines the starting point of the TCP data payload.
6.  **Flags:** The TCP flags consist of several 1-bit fields that control various aspects of the TCP connection. These flags include:
	-   **URG** (Urgent Pointer): Indicates that urgent data is present in the TCP segment.
	-   **ACK** (Acknowledgment): Indicates that the acknowledgment number field is valid.
	-   **PSH** (Push Function): Requests the receiving application to process the data immediately.
	-   **RST** (Reset Connection): Resets the TCP connection.
	-   **SYN** (Synchronize Sequence Numbers): Initiates a TCP connection setup.
	-   **FIN** (Finish): Closes the TCP connection.
7.  **Window Size:** This 16-bit field specifies the number of bytes the sender is willing to receive, also known as the receive window. It helps in flow control by indicating the amount of available buffer space on the receiver's side.
8.  **Checksum:** The 16-bit checksum field is used for error detection. It ensures the integrity of the TCP segment by verifying the integrity of the header and payload.
9.  **Urgent Pointer:** If the URG flag is set, this 16-bit field points to the last byte of urgent data in the TCP segment.
10.  **Options:** The options field is optional and used to include additional parameters or functionality. Some commonly used options include Maximum Segment Size (MSS), Selective Acknowledgment (SACK), and Timestamps.
11.  **TCP Payload:** The TCP payload consists of the actual data being transmitted. It can range from zero bytes (in ACK or control packets) to a maximum determined by the maximum segment size (MSS) negotiated during connection setup.

## TCP Retransmission Timeout

Declaring a correct timeout is a crucial step to ensure the full potential of TCP. The timeout should be set to a value longer than the RTT, but the RTT isn't fixed:
- if it is too short then there will be a lot of retransmissions of delayed packets,
- if it is too long then retransmission of lost packets will take too much, slowing the whole transmission.

A formula for a *weighted estimated* RTT is called **Exponentially Weighted Moving Average** (*a.k.a. EWMA*), which computes a *more stable* RTT, that fluctuates less w.r.t. the measured one. 

$$\large
	\text{RTT}_i = (1-\alpha) \cdot \text{RTT}_{i-1} + \alpha \cdot \text{rtt}_i
$$

> [!abstract] Estimated RTT (EWMA) Variables
> 
> - $\text{rtt}_i$ is the $i$-th measured RTT;
> - $\text{RTT}_i$ is the $i$-th estimated RTT, assuming $\text{RTT}_0 = 0$;
> - $\alpha$ is a parameter that adjusts the average, a standard value is $\alpha = .125$.

The estimated RTT can be used to compute an adjustable timeout (*a.k.a. RTO*). Originally double the estimated RTT (i.e. $\text{RTO}_i = 2 \cdot \text{RTT}_{i-1}$) was a recommended value, but now another formula that uses the *mean deviation* called **Jacobson's Algorithm** is recommended.

$$\large
	\text{RTO}_i = \text{RTT}_{i-1} + 4 \cdot \bar\sigma_{i-1}
$$

> [!abstract] Jacobson's Algorithm Variables
> 
> - $\text{RTO}_i$ is the $i$-th recommended timeout;
> - $\bar\sigma_i$ is the $i$-th *mean deviation*.

The mean deviation gets extremely expensive to compute as more time goes on, so a cheaper-to-compute version of the mean deviation can be computed using EWMA.

$$\large
	\bar\sigma_i =
		(1-\rho) \, \bar\sigma_{i-1}
		+ \rho \, |\text{rtt}_i - \text{RTT}_{i-1}|
$$

> [!abstract] Mean Deviance (EWMA) Variables
> 
> - $\rho$ is a parameter that adjusts the average, a standard value is $\rho = .25$.

> [!note] Exponential Back-off
> 
> It could still happen that the retransmission timeout is too short, thus the sender may retransmit duplicates many times. A solution to this problem is **exponential back-off**: the RTO for a packet is double upon each timeout of the packet, to give more time to delayed packets; the first RTO is still computed using Jacobson's algorithm.
> 
> This is an initial notion of *congestion control*.

## TCP Flow-Congestion Control

The flow and congestion control mechanisms in TCP address different aspects of data transmission to ensure reliable and efficient communication. These mechanisms work together to prevent issues such as buffer overflow, packet loss, and network congestion.

> [!abstract] Flow and Congestion Control
> 
> - **Flow control** prevents receiver buffer overflow, ensuring that data is delivered and processed at a pace that the receiver can handle.
> - **Congestion control** helps maintain network stability by regulating the sending rate to avoid overwhelming the network and causing congestion-induced performance degradation.


Flow control operates on an end-to-end level, it resolves the issue of the sender transferring data faster than the receiver can buffer and process. The receiver, on each response, sends a *feedback* to the sender on how much free space it has left to buffer packets, specified in the `rwnd` header of the segment. This way, the sender knows how much can be sent and the receiver's buffer won't get overflowed.

Congestion control, on the other hand, operates at a network level and focuses on preventing congestion within the network. It monitors the state of the network and dynamically adjusts the sending rate of TCP packets (through the congestion window `cwnd`) to avoid network congestion.

The sender monitors the network status by looking for *duplicate ACKs* and *timeouts*, which are indicators of network congestion. If ACKs arrive steadily, then the congestion window `cwnd` can be increased in size; otherwise if duplicate ACKs or timeouts are detected, `cwnd` must be decreased in size.

> [!note] Sender's Window
> 
> The sender's window size is set to be the minimum between the receiver's window and the congestion window. This limits the reliable transmission rate to at most the ratio the window size over the RTT; at most because packet loss or corruption could still happen.

The first version of TCP congestion control was named **Tahoe TCP**. It considered three duplicate ACKs the same as a timeout, the only states it had were *slow start* and *congestion avoidance*.

![Tahoe TCP - Diagram](assets/tcp_tahoe.png)

Then, a better version of TCP congestion control called **Reno TCP** was developed. It considered three duplicate ACKs as a lighter indication of congestion than a timeout, it also added *fast recovery* as an additional state to the ones already in Tahoe TCP. 

![Reno TCP - Diagram](assets/tcp_reno.png)

### Slow Start

When a TCP connection begins, show start is the first state of the connection. The congestion window `cwnd` is set to 1 MSS and it's "doubled" on every RTT. The window isn't actually doubled on every RTT, but in reality it is incremented by 1 MSS for every ACK received (which, without loss or corruption, is equivalent to doubling the window every RTT).

TCP continues in a state of slow start until `cwnd` becomes greater than a set threshold called `sstresh`. If doubling `cwnd` would result in `cwnd` being greater than `ssthresh`, then `cwnd` will be set to the value of `ssthresh`. After reaching `ssthresh`, TCP will step out of slow start and get into *congestion avoidance* (i.e. linear increase).

The initial state of `ssthresh` can be set to a constant, and then it is updated every time a timeout happens. Upon a timeout (or 3dupACKs in Tahoe TCP), TCP will step out of whichever state it is on and get into slow start: `ssthresh` is set to half the size `cwnd` was on the timeout, `cwnd` is set to 1 MSS and `cwnd` will be increased exponentially (i.e. double every RTT).

### Congestion Avoidance

*TK*

### Fast Recovery

*TK*
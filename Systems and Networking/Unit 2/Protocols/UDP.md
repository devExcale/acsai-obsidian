# Uniform Datagram Protocol

UDP is the simplest form of transport protocol one could think of. It is almost barebone IP, it adds almost no functionality. It may seem that it is useless comparing it to TCP, but it has its own quirks:
- **Finer application-level control,** when an application tasks the transport layer to send a message, UDP will do it right away. TCP, on the other hand, has a congestion control system, that may slow down the message;
- **No connection,** so UDP can (again) send packets right away. TCP, on the other hand (again), has a three-way handshake with the goal to form a connection, which in turns slows down the message;
- **Smaller header,** UDP has 8 bytes of headers, versus 20 bytes of TCP headers.
# HyperText Transfer Protocol

The **HyperText Transfer Protocol** is the main [application-layer](Systems%20and%20Networking/Unit%202/Packets/Layered%20Structure.md#Application) protocol used in the **Web**. HTTP has been developed to permit the exchange of documents between hosts through the web.

Clients ask, through a structured message in the application layer, to servers a **web page** (document), which is composed of objects; these objects could be any file (e.g. image, html file, video file).

A document is uniquely identified by an **Uniform Resource Locator** (URL):

$$\large
	\underbrace{\text{http://}}_{(1)\ protocol}
	\underbrace{\text{github.com}}_{(2)\ hostname}
	\underbrace{\text{/favicon.png}}_{(3)\ resource}
$$

1. Application protocol to be used. In this case, HTTP;
2. Hostname (either [IP](?TK) or [DNS](?TK) address) of the server;
3. Path of the resource to get.

The default port of HTTP is `80`, which is usually implicit. If a server exposes a website on another port, though, it can be specified in the URL:

$$\large
	\text{http://github.com}
	\underbrace{\text{:8080}}_{(4)\ port}
	\text{/favicon.png}
$$

4. Explicit port where the website is exposed.

HTTP uses the [TCP](?TK) transport-layer protocol, so thanks to lower layers HTTP does not have to think about reliability and insuring the message got across. Instead, it can think of just sending the documents to clients.

HTTP is called a **stateless protocol**, because servers do not store information about the client. If a client asks for the same file two times in a row, the server will send that same file two times.

## Persistency

The HTTP could either be **non-persistent** or **persistent**, meaning whether the server can transfer more than one file in one open TCP connection.

Take for example a document composed of one HTML page `index.html` and 5 PNG images, all residing on the same server with address `site.edu`.

- ***Non-persistent***

1. The client initiates a TCP connection with the server on port 80 (`site.edu:80`);
2. The client sends an HTTP request message through the URL `http://site.edu/index.html`;
3. The server processes the request, retrieves the document and sends it via an HTTP response message;
4. The server tries to close the TCP connection (only closes once the server knows the client got everything right);
5. The client receives the response and extracts the document from the response message, while the connection is terminated. While extracting the document it finds references to the 5 images;
6. The first 4 steps are executed for each image.

To the time it takes to transfer all the files, we'd have to add 2 RTT for each [TCP handshake](?TK) needed to open a new connection. Moreover, looking at both client and server, there's the need to allocate new resources (i.e. socket) every time a new connection is opened. This is crucial especially from the server side, which is processing many requests simultaneously.

- ***Persistent***

1. The client initiates a TCP connection with the server on port 80 (`site.edu:80`);
2. The client sends an HTTP request message through the URL `http://site.edu/index.html`;
3. The server processes the request, retrieves the document and sends it via an HTTP response message;
4. The server waits an amount of time before closing the connection, so that the client can follow instantly with new requests;
5. The client receives the response and extracts the document from the response message, with the connection still open. While extracting the document it finds references to the 5 images, so it opens requests for each new file;
6. The server receives the requests and tries to send the files concurrently;
7. The connection is closed either by the client, after receiving the files, or by the server, after a timeout.

A persistent connection takes just 1 RTT for each file requested (plus the one initiating the TCP connection), so it is faster than a non-persistent one $(n+1 \le 2n)$, and there's no need to allocate new socket resources for each file.
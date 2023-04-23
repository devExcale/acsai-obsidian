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

## Connection

The HTTP connection can be either **non-persistent** or **persistent**, meaning whether the server can transfer more than one file in one open TCP connection.

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

## Format

The HTTP defines two types of messages: **request** (used to request an object) and **response** (used to return an object).

*HTTP Request*
```http
GET /somedir/page.html HTTP/1.1
Host: excale.ovh
Connection: close
User-agent: Mozilla/5.0
Accept-language: it, en

```

*HTTP Response*
```http
HTTP/1.1 200 OK
Connection: close
Date: Thu, 03 Nov 2022 16:40:43 GMT
Server: Apache/2.2.3 (CentOS)
Last-Modified: Thu, 03 Nov 2022 16:40:43 GMT
Content-Length: 6821
Content-Type: text/html

(entity body...)
```

An HTTP message is a simple human-readable [ASCII](?TK) message, containing some lines.

The first line is the **request line** or **status line**, respectively for requests and responses. Then are the **headers**, key-value pairs that are like *variables* included in requests and responses.

| **Name**       | **Contains**                              |
| -------------- | ----------------------------------------- |
| *Request Line* | Method, URL, HTTP version                 |
| *Status Line*  | HTTP version, Status code, Status message |

Each line is terminated by a combination of carriage return `cr` and line feed `lf`. Moreover, there's a blank line after the header lines (this too terminated by `cr` and `lf`).

After the header lines is the space for the **entity body**: the object that needs to be exchanged between client and server. The server isn't the only one that can send objects; in fact, with some [methods](#Methods), the client can send objects too.

![General format of an HTTP message](?TK)

### Methods

The method of an HTTP request tells the server how to interpret the request and what to send as a response.

| **Method** | **Description**               |
| ---------- | ----------------------------- |
| GET        | The client requests an object |
| POST       | TK                            |
| PUT        | TK                            |
| DELETE     | TK                            |
| HEAD       | TK                            |

### Status

TK

| **Code** | **Message**                  | **Description** |
| -------- | ---------------------------- | --------------- |
| `2XX`    |                              |                 |
| `200`    | *OK*                         |                 |
| `3XX`    |                              |                 |
| `301`    | *Moved Permanently*          |                 |
| `4XX`    | General Client Error         |                 |
| `400`    | *Bad Request*                |                 |
| `404`    | *Not Found*                  |                 |
| `5XX`    | General Server Error         |                 |
| `505`    | *HTTP Version Not Supported* |                 |

### Headers

Headers are a key-value pair and are one of the key information in HTTP messages. Most headers are optional, except some required ones.

Except required ones, headers are a way the HTTP offers to customize responses based on the requesting client.

| **Header**          | **Host** | **Possible Values**        | **Description**                                                            |
| ------------------- | -------- | -------------------------- | -------------------------------------------------------------------------- |
| `Host`              | Client   | Address (either IP or DNS) | Destination of the request.                                                |
| `Connection`        | Both     | TK                         | Whether to keep the TCP connection open.                                   |
| `User-agent`        | Client   | Any String                 | Code of the requesting web browser.                                        |
| `Accept-language`   | Client   | Any Locale                 | Tells the server to send the object in a preferred language, if possible.  |
| `Date`              | Server   | Any Date                   | Indicate the date at which the response has been created/object retrieved. |
| `Server`            | Server   |                            |                                                                            |
| `Last-Modified`     | Server   |                            |                                                                            |
| `Content-Length`    | Server   |                            |                                                                            |
| `Content-Type`      | Server   |                            |                                                                            |
| `If-modified-since` | Client   | Any Date                   |                                                                            |
| `Cookie`            | Client   |                            |                                                                            |
| `Set-Cookie`        | Server   |                            |                                                                            |

### Cookies

The HTTP is stateless, so no information (either of client and server) is saved across requests. This simplifies the structure of HTTP and permits *high-performance* web servers, but takes aways customizability and some functionality.

These characteristics can be reintroduced with **cookies**: special key-value pairs that go outside the scope of headers.

The cookie technology has three main components:
- One or more `Cookie` [header lines](#Headers) in the HTTP request message;
- One or more `Set-Cookie` header line in the HTTP response message;
- A cookies file kept on the user's end system, which is managed by the browser.

Cookies have a security policy: every website can store and read only its own cookies, while other cookies aren't accessible to it (e.g. `google.com`'s cookies aren't accessible to `facebook.com`)

The browser stores the cookies in a file; whenever the client makes a request these cookies are sent under a `Cookie` header in a semicolon-separated list of `key=value` pairs (e.g. `Cookie: id=269; theme=dark`).

The server can read these cookies to customize the response (or to track a session with the client); it can tell the client to store other cookies with the `Set-Cookie` header. The same logic of the `Cookie` header is applied: cookies are sent in a semicolon-separated list of `key=value` pairs, but there's more. The `Set-Cookie` header can also specify some attributes of the cookie, namely:
- *Domain and Path* (a more granular security feature)
- *Expires or Max-Age* (respectively date or seconds after which the cookie is deleted)
- *Secure and HttpOnly* (whether the cookie can be read using https only and from scripting languages)

### Proxy Server

A **proxy server** is a web server that satisfies HTTP requests on behalf of another web server. It stands in the middle of a client and one or more servers, and can have various functions:
- Security checks
- Web cache
- Load balancing

Here we analyse especially the **web cache** functionality.

The client won't make direct HTTP requests to the original server, but it will instead send the request to the proxy. The proxy has its own storage where it keeps frequently-asked files:
- if the proxy can find the requested file in its storage, then it will respond directly to the client;
- otherwise, the proxy will forward the request to the original server, which will (hopefully) provide the requested object. The proxy will save the object on its storage and forward the original server's response.

> [!info] Note
> *Note that the proxy is both a server and a client: it is a server for the browser, and a client for the original server.*

Caches are important for two main reasons:

1. They can reduce long-distances response time.

Imagine a client in America that sends a request to a server in Europe. The RTT will take some time, because packets have to travel from America to Europe and then back to America.

If the server providers were to install a web cache in America, the client would be able to ask to the proxy. If the proxy can provide the requested file, then there's no need for the client to ask the cross-continental server.

And this, implicitly, is the other reason caches are important:

2. They can reduce internet traffic.

Reducing incoming traffic from America, more bandwidth will be available in Europe, especially to the server providers, which will have to answer less requests.

Web caching introduces a problem: what if the server updates an object? The cache then will have an outdated version of the file.

To solve this problem, before replying to the clients, a proxy performs a **Conditional GET**: the proxy sends a GET request to retrieve the object requested by the client, and appends a `If-modified-since` header containing a date. The origin server will:
- send the whole object in the response, if the object has been modified after the specified date;
- send a `304 Not Modified` [response](#Status) with an empty body, if the file stored in the cache is up-to-date.

*Conditional GET*
```http
GET /fruit/kiwi.gif HTTP/1.1
Host: excale.ovh
If-modified-since: Fri, 4 Nov 2022  12:23:56

```

*Conditional response*
```http
HTTP/1.1 304 Not Modified
Date: Fri, 4 Nov 2022 12:25:06
Server: Apache/1.3.0 (Unix)

(empty entity body)
```

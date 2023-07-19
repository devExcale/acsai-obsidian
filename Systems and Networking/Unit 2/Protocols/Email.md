# Email

Email was and is one of the most important tools the internet hosts. TK

The email technology has three components:

| **Component**    | **Description**                                       |
| ---------------- | ----------------------------------------------------- |
| *User agents*    | Clients that lets users communicate with mail servers |
| *Mail servers*   | Servers that store and send email to other servers    |
| *SMTP*           | Protocol used to send and exchange email                       |
| *POP3* or *IMAP* | Protocols used to download email                      |

![Diagram of email system](?TK)

Each user registered within a mail server has a **mailbox**, which manages and maintains the messages sent to them, with relative attachments.

## Simple Mail Transfer Protocol

SMTP is the core protocol of email, it's the protocol that lets mail servers exchange email messages. It needs reliability, so SMTP uses [TCP](?TK) as transport protocol.

SMTP works like this:
1. A sender uses its user agent to compose a message, set the receiver's email address and send the message;
2. The sender's user agent sends the message to the configured mail server, which places it in a **message queue**;
3. The sender's mail server (which now acts as a client) opens a TCP connection to the receiver's mail server;
4. After an initial SMTP handshake, the client sends the sender's message to the receiver's mail server;
5. The receiver's mail server places the message in the receiver's mailbox;
6. The receiver can then use his user agent to retrieve the message whenever he wants.

TK SMTP port

If the receiver's server isn't able to open a connection, the message stays in the sender's server's message queue. The sender's server will try to send it again after some time passed.

### SMTP Commands

The core of SMTP works by exchanging human-readable messages. In these messages, the sender server *executes* some commands, to which the receiver server replies with codes and optional messages.

| **Command** | **Parameter**            | **Description**                                                                                                        |
| ----------- | ------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| `HELO`      | Sender server's hostname | Short for *HELLO*, introduces the sender's server.                                                                     |
| `MAIL FROM` | Sender's address         | Specifies the sender's address.                                                                                        |
| `RCPT TO`   | Receiver's address       | Specifies the receiver's address.                                                                                      |
| `DATA`      | Message                  | The actual message to be transmitted. This can be multi-line, and ends with a line with just a dot. (i.e. `CRLF.CRLF`) |
| `QUIT`      | N/A                      | Tells the receiver's server to close the TCP connection.                                                               |

If the sender has multiple messages to send to the same receiver, a new connection isn't required every time. Once the sender has introduced itself with the `HELO` command, it can send a new message by opening with the `MAIL FROM` command and closing it by ending the `DATA` command (i.e. `CRLF.CRLF`). After sending all the messages, the connection can be closed with the `QUIT` command.

### Message Format

#### Headers

Much like [HTTP](/Systems and Networking/Unit 2/Protocols/HTTP.md), SMTP messages can include headers. The main difference, though, is that while HTTP headers are useful only to browsers and web servers, SMTP headers are useful only to end users (i.e. receivers).

Headers in SMTP messages provide a way for senders to add more information to receivers, like an address to reply to.

SMTP headers, like HTTP headers, are key-value pairs that each compose one line at the start of the message, and are separated by an empty line from the actual message. Some are required (`From`, `To`, `Subject`), while others are optional

> [!warning] Note
> Headers differ from SMTP commands. While the headers `From` and `To` repeat information already provided during the SMTP handshake, this information is actually not used by the servers, but only to the end users. These headers could be different from the information used during the handshake, but the receiving user will still be the one provided with commands.

A typical SMTP message (just the message) looks like this:

```properties
From: alice@crepes.fr
To: bob@hamburger.edu
Subject: Studying SMTP.

(message)
```

#### Encoding

The SMTP standard works by sending messages encoded with 7-bit ASCII. Any character encoded in any other way will be sent as a 7-bit ASCII character(s) anyway.
This includes any binary part and attachments.

#### Attachments

Attachments are included at the end of the message, encoded as 7-bit ASCII characters.

### Example of SMTP Exchange

`S:` marks the messages sent by the receiver's server, while `C:` the ones sent by the sender's server.

```properties
S: 220 hamburger.edu  
C: HELO crepes.fr  
S: 250 Hello crepes.fr, pleased to meet you
C: MAIL FROM: <alice@crepes.fr>  
S: 250 alice@crepes.fr ... Sender ok  
C: RCPT TO: <bob@hamburger.edu>  
S: 250 bob@hamburger.edu ... Recipient ok  
C: DATA  
S: 354 Enter mail, end with "." on a line by itself  
C: Do you like ketchup?  
C: How about pickles?  
C: .  
S: 250 Message accepted for delivery  
C: QUIT  
S: 221 hamburger.edu closing connection
```

## Reading Emails

While a sender can use SMTP to send email messages, these messages will reach the receiver's email server, where they will be stored in the respective mailbox. To read the messages, the receiver has to use other designated protocols:
- [POP3](#POP3)
- [IMAP](#IMAP)

## POP3

POP3 is the first mail access protocol created, and is quite simple. This simplicity, though, limits its features.

POP3 works like this:
1. **Authorization,** the user agent uses username and password (sent in cleartext) to log in the mail server;
2. **Transaction,** the user agent retrieves all the emails and can do actions such as mark messages for deletion, remove marks for deletion and obtain mail statistics;
3. **Update,** it occurs after the clients issues the `quit` message, which ends the POP3 session. The mail server deletes all the messages previously marked for deletion.

The problem with POP3 is this basic featuring: messages can be stored in folders and categories just once they've been downloaded in the end device. If a user downloads emails on another user agent, such changes won't be seen in this other client.

### POP3 Commands

Much like SMTP, POP3 works by exchanging messages. The client can send commands, to which the server can respond in two ways: `+OK` and `-ERR`, both can be followed by an additional message.

| **Command** | **Parameters** | **Description**                                           |
| ----------- | -------------- | --------------------------------------------------------- |
| `user`      | Username       | Necessary to authenticate, must be the first command.     |
| `pass`      | Password       | Necessary to authenticate, must come after `user`.        |
| `list`      | N/A            | Lists the messages stored in the mailbox.                 |
| `retr`      | Message ID     | Retrieves the content of a message stored in the mailbox. |
| `dele`      | Message ID     | Marks a message for deletion.                             |
| `quit`      | N/A            | Tells the server to close the connection.                 |

### Example of POP3 Exchange

```properties
S: +OK POP3 server ready  
C: user bob  
S: +OK  
C: pass hungry  
S: +OK user successfully logged on
C: list  
S: 1 498  
S: 2 912
S: .  
C: retr 1  
S: (blah blah ...  
S: .................  
S: ..........blah)  
S: .  
C: dele 1  
C: retr 2  
S: (blah blah ...  
S: .................  
S: ..........blah)  
S: .  
C: dele 2  
C: quit  
S: +OK POP3 server signing off
```

## IMAP

To fix POP3's limitations, IMAP has been created. IMAP is more complex that POP3, but offers more functionalities.

TK

# Domain Name System

Hosts in a network can be identified by their [IP address](?TK), which are easy to understand for machines. For humans, though, they're harder to remember, especially when there's many to remember.

To fix this problem, the **Domain Name System** has been created. The DNS associates one or more *alphanumeric addresses* to one IP address, so that humans may use this canonical mnemonic address instead of numeric ones.

The DNS is both:
1. a distributed database implemented in a hierarchy of DNS servers;
2. an application-layer protocol that allows hosts to query said database.

> [!info] The protocol
> The DNS is an application-layer protocol that can be used parallelly to other application-layer protocols such as [HTTP](Systems%20and%20Networking/Unit%202/Protocols/HTTP.md) and [SMTP](Systems%20and%20Networking/Unit%202/Protocols/Email.md#Simple%20Mail%20Transfer%20Protocol). It uses [UDP](?TK) over port 53.

## Services

- **Host Aliasing**

TK

- **Mail Server Aliasing**

TK

- **Load Distribution**

TK

## Structure

The DNS database is a distributed database, the hierarchy is so organized:
1. Root DNS servers
2. Top-Level Domain (TLD) servers
3. Authoritative servers
4. (Local DNS server)

[Hierarchy of DNS servers](?TK)

### Root DNS Server

The Root DNS servers are the main *entry point* for DNS queries, they contain the addresses to the TLD servers.

Root servers are managed by 13 different organizations, and there are more than 400 servers scattered all over the world. This is done to reduce traffic volume, response time and to prevent a single point of failure. Moreover, maintenance would be easier too.

### Top-Level Domain Server

Each TLD (e.g. `org`, `com`, `it`) has an associated server (or cluster of servers), which point to the correlated authoritative servers. Every TLD server is managed by a large company.

### Authoritative Server

Authoritative servers are the final leaf of the distributed hierarchy, they contain actual records that bind mnemonic DNS addresses to IP addresses.

This type of server is managed by companies, every company/private could have its own authoritative server to route DNS addresses of their public services to IP addresses. If someone decides that they do not want to host a DNS server, they could always pay another company to add DNS records in their stead.

### Local DNS Server

A local DNS server doesn't strictly belong to the DNS hierarchy, but it's still central for hosts connecting through ISPs. Each ISP has a local DNS server (also called *default name server*), which acts as an entry-point to the hierarchy.

When an host makes a request using DNS, the default name server acts as a proxy which forwards the request to servers in the hierarchy, without needing to follow the proper order (perhaps because of a cache).

## Queries

The DNS works through queries: the host asks the DNS to resolve a hostname, queries can either be **iterated** or **recursive**.

### Iterated Queries

Iterated queries work like this:
1. The host asks to the local server to resolve an hostname;
2. The local server asks the root server, which sends a list of TLD servers;
3. The local server asks the TLD servers, which returns an authoritative server;
4. The local server asks the authoritative server, which could act as an additional layer to multiple nested authoritative servers. In this case, the authoritative resolves the hostname either directly or through **recursive queries** (in the case of nested authoritative servers);
5. The local server then returns the resolved hostname to the requesting host.

![Diagram of an iterated query](?TK)

### Recursive Queries

Recursive queries work like this:
1. The host asks to the local server to resolve an hostname;
2. The local server asks the root server to resolve the hostname;
3. The root server asks the right TLD server to resolve the hostname;
4. The TLD server asks the right authoritative server to resolve the hostname;
5. The authoritative server resolves the hostname either directly or through an additional query to the right authoritative server;
6. The resolved hostname then travels back to the requesting host in the reversed order of querying: authoritative, TLD, root, local, host.

![Diagram of a recursive query](?TK)

### Caching

Similarly to HTTP, going every time from the root server to the authoritative one increases traffic load on the network. To reduce this strain, DNS server can (and must) **cache resolved hostnames**.

This way, if an host was to ask to the local server about an hostname:
- if the local host contains the resolved hostname, it'll return that directly;
- otherwise, if the local host contains the resolved address a right TLD server, it'll ask the TLD server;
- if even no TLD server address is stored, the local server will ask the root server and the query will be just like the initial examples.

> [!info] Root DNS
> This caching system makes it so the root servers are actually a *last resource*, to contact if not even the right TLD server is known from the local server.

DNS mappings, though, could change any moment (e.g. maintenance); this leads to two things:
- defining a caching time limit;
- defining a way to tell if a resolved hostname is absolute or not.

> [!abstract] Caching Time
> Caching time is **finite**, usually two days, but it can be configured using [TTL](?TK). The reason is to update regularly DNS mappings.

> [!abstract] Authoritative Mapping
> A DNS query response can be marked as `Authoritative` or `Non-Authoritative`.
> 
> - `Authoritative` says that the mapping is coming from an authoritative server, so the mapping is *absolute*;
> - `Non-Authoritative` says that the mapping is coming from a cache, so the mapping could have changed in the meantime.

## DNS Records

Every mapping is stored in the distributed database in a four-tuple called **Resource Record** (RR), constructed like this: `(Name, Value, Type, TTL)`.

### TTL

The **Time-To-Live** is the amount of time after which a cached mapping should expire, removed from the cache.

### Type

DNS records have more than a type, based on the application of the mapping.

| **Type** | **Name**                | **Value**                         | **Description**                                                                                                                                                           |
| -------- | ----------------------- | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `A`      | A hostname              | Associated IP address             | The classic hostname-IP address mapping.                                                                                                                                  |
| `NS`     | A domain (e.g. foo.com) | Authoritative server's IP address | The mapping of a domain to the relative authoritative server.                                                                                                             |
| `CNAME`  | A hostname              | A canonical hostname              | An alias for a hostname to a more mnemonic hostname (e.g. `foo.com` to `www.foo.com`)                                                                                     |
| `MX`     | A hostname              | Associated hostname/IP address    | Canonical name of the mail server. This way, the mail server can have the same hostname as the web server, but with different IPs (e.g. `foo.com` to `mail.bar.foo.com`). |

## DNS Messages

DNS messages identify both queries and responses, as they have the same structure. A DNS message is composed of a **header** part, of size 12 bytes, and 4 other sections.

![Format of a DNS message](?TK)

The header is divided into 6 categories of 2 bytes each:
1. **Identification,** a number that identifies the query, so the response can then be matched using this;
2. **Flags,** some 1-bit flags;
3. **Number of questions,** how many hostnames in the query should be resolved;
4. **Number of answer RRs,** how many resolved Resource Records are in the answer;
5. **Number of authority RRs,** how many authority Resource Records are in the answer;
6. **Number of additional RRs,** how many Resource Records with additional information are in the answer.

Not all the bits in the flags section are used, some are reserved for future use. Some of the flags are:
- **Query/Flag,** indicates whether the message is a query or a reply;
- **Authoritative,** indicates whether the server is authoritative;
- **Recursion desired,** indicates whether the clients prefers to perform the query using recursion instead of iterating;
- **Recursion available,** indicates whether the server can execute recursive queries.

The other sections are:
1. **Question,** contains the actual hostnames to resolve. To resolve an hostname, the client must send the name and the type of mapping (e.g. `A`, `NS`, `MX`);
2. **Answer,** contains the the resolved hostnames in form of Resource Records (i.e. `Name, Value, Type, TTL`);
3. **Authority,** contains records of other authoritative servers (e.g. recursive queries);
4. **Additional Information,** contains other useful records. For example, when querying an `MX` record that maps to a canonical name, this section could contain the `A` record of the canonical name.

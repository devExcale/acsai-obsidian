# Security

Nowadays, people could use anything for their personal gains, [Internet](/Systems%20and%20Networking/Unit%202/Networks.md#Internet) included. So, it is imperative to learn what malicious people could do and how to counteract.

## Attacks

### Packet Sniffing

People could access the [transport mean](/Systems%20and%20Networking/Unit%202/Transport%20Means.md) of [packets](Systems%20and%20Networking/Unit%202/Internet/Packet.md) and read packets that are going through that transport mean (e.g. shared ethernet, wireless)!

Malicious users could read the content of these packets and find sensitive information about sender and receiver (including passwords).

### Packet Spoofing

Malicious users could send packets with a false source address, to imitate actions needed to further scopes.

### Denial of Service

(Distributed) Denial of Service consists in [cracking](?TK) other network devices to then uniformly attack a selected target. The goal of this attack is to allocate as many resources to make the target unavailable, unreachable to other hosts, by sending as many useless packets as the cracked devices can.

All the cracked network devices are called *botnet*.

## Defense

### Authentication

Authentication is a security measure which consists in providing a way to prove that you are who you say you are, so that other users/hardware cannot impersonate you.

Phones provide authentication through SIM cards, but in the internet there's no other hardware support, software implementations are needed.

### Confidentiality

Even if other users could catch packets, these packets must not be readable (or at least the message must not be understandable).

Confidentiality is implemented via [encryption](?TK). 

### Integrity Checks

A [digital signature](?TK) is inserted in the packet, so to check nobody tampered with it.

### Access Restrictions

Devices could connect to password-protected VPNs, so that their devices are not "talking" over a public network.

### Firewalls

Firewalls are either hardwares or softwares inserted in network cores, specialized in network analysis. The main functionalities are:
- Filter incoming packets to restrict senders, receivers and applications;
- Detecting and reacting to [DOS](#Denial%20of%20Service).

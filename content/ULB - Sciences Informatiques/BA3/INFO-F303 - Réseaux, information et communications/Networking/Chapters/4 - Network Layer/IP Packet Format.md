---
title: IP Packet Format
authors: Alessandro Dorigo
tags:
  - Network
---


> [!info]+ Définition
>
> The IP packet format is a standardized structure for transmitting data over the Internet Protocol. Each packet consists of a header (containing control information) and a payload (containing the actual data). The packet format is 32 bits wide.
> ![[62dbadfe5340104db00cde865550e157.png]]

> [!abstract]- Header Fields
>
> **IP protocol version number (ver):** Specifies the version of IP being used
>
> **Header length (len):** Measured in 32-bit words
>
> **Type of service:** Indicates the type of service requested
>
> - diffserv
> - ECN (Explicit Congestion Notification)
>
> **Length:** Total packet length in bytes
>
> **16-bit identifier, flags, fragment offset:** Used for fragmentation/reassembly
>
> **Time to live (TTL):** Remaining max hops, decremented at each router
>
> **Upper layer protocol:** Identifies the upper layer protocol (e.g., TCP or UDP)
>
> **Header checksum:** Used for error detection in the header
>
> **Source IP address:** 32-bit source IP address
>
> **Destination IP address:** 32-bit destination IP address
>
> - Maximum length: 64K bytes
> - Typically: 1500 bytes or less
>
> **Options (if any):** Optional fields such as timestamp, record route taken

> [!abstract]- Payload
>
> **Payload data:** Variable length, typically a TCP or UDP segment

> [!abstract]- Overhead
>
> Total overhead for TCP+IP:
>
> - 20 bytes of TCP
> - 20 bytes of IP
> - = 40 bytes + application layer overhead for TCP+IP

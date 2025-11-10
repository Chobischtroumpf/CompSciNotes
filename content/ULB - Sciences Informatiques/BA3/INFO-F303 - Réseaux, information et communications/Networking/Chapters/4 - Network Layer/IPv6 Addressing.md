---
title: IPv6 Addressing
authors: Alessandro Dorigo
tags:
  - Network
---

> [!info]
> The initial motivation for IPv6 was that the 32-bit IPv4 address space would get completely allocated
>
> Additional motivation was:
> - Speed processing/forwarding: 40-byte fixed length header, no fragmentation allowed in routers
> - Enable different network-layer treatment of “flows”
> And its only requirement was:
> - There wowuld be no changes in higher and lower protocol layers

> [!info]+ Definition
>
> IPv6 is the next generation Internet Protocol that uses 128-bit addresses (compared to IPv4's 32-bit addresses). The packet format has been simplified compared to IPv4 to enable faster processing at routers.
> They are written as $x:x:x:x:x:x:x:x$ where $x$ is a 16-bit hexadecimal field.

> [!example]+ Example
>
> Full IPv6 address: 2001:0000:130F:0000:0000:09C0:876A:130B

> [!abstract]- Header Fields
> ![[81451e381bb2a88b667acc8a7b80ae41.png]]
> **ver:** Version number (32 bits wide format)
>
> **pri:** Priority - identifies priority among packets in flow
>
> **flow label:** Identifies packets in same "flow" (concept of flow looking into higher level headers, e.g., port, but concept of "flow" not well defined)
>
> **payload len:** Length of the payload
>
> **next hdr:** Identifies the next header (allows to chain several extension headers and finally identify upper layer protocol - no protocol field like in IPv4)
>
> **hop limit:** Similar to TTL in IPv4
>
> **source address (128 bits):** 128-bit IPv6 source address
>
> **destination address (128 bits):** 128-bit IPv6 destination address
>
> **payload (data):** The actual data being transmitted

> [!tip]+ What's Missing Compared to IPv4
>
> Compared to IPv4, IPv6 removes several fields:
>
> - No header checksum (to speed processing at routers)
> - No fragmentation/reassembly (only possible at source)
> - No options (available as upper-level, next-header protocol at router)# IPv6 Addresses

> [!abstract]- Address Notation Rules
>
> **Leading zeros in a field are optional:**
>
> $$ \text{2001:0:130F:0:0:9C0:876A:130B} $$
>
> is equivalent to 2001:0000:130F:0000:0000:09C0:876A:130B
>
> **Successive fields of 0 are represented as :: but can be used at most once in an ip:**
>
> - 2001:0:130F::9C0:876A:130B is allowed
> - 2001::130F::9C0:876A:130B is **not** allowed (:: used twice)

> [!example]+ Example
>
> Special addresses:
>
> - FF01:0:0:0:0:0:0:1 can be written as FF01::1
> - 0:0:0:0:0:0:0:1 can be written as ::1 (loopback address)
> - 0:0:0:0:0:0:0:0 can be written as :: (this host)

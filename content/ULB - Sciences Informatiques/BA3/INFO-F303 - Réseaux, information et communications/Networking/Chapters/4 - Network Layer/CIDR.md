---
title: CIDR
authors: Alessandro Dorigo, Mihai Bors
tags:
  - Network
---
> [!info]+ Definition
> **CIDR (Classless InterDomain Routing)** is an addressing scheme where the [[Subnet]] portion of an IP address can be of arbitrary length, replacing the older class-based system. Addresses are written as `a.b.c.d/x`, where `x` is the number of bits in the subnet portion.

## CIDR Notation

> [!abstract]+ Address Format
> **Format:** `a.b.c.d/x`
>
> - `a.b.c.d`: The IP address in dotted-decimal notation
> - `/x`: The prefix length (number of network bits)
>
> **Example:** `200.23.16.0/23`
> - First 23 bits: subnet identifier
> - Remaining 9 bits: host identifier

## Detailed Example

> [!example]+ Understanding `/23`
> ![[208aba30eb5e10049401846373ad02df.png]]
>
> **Address:** `200.23.16.0/23`
>
> | Octet | Decimal | Binary |
> |:---:|:---:|:---:|
> | 1st | 200 | `11001000` |
> | 2nd | 23 | `00010111` |
> | 3rd | 16 | `00010000` |
> | 4th | 0 | `00000000` |
>
> **Prefix boundary falls mid-octet:**
> ```
> ←───────── 23 bits ─────────→ ←─ 9 bits ─→
> 11001000   00010111   0001000|0   00000000
> ────────   ────────   ───────|─   ────────
>  octet 1    octet 2    octet 3     octet 4
>                              ↑
>                    split happens here
> ```
>
> **Subnet mask:** `255.255.254.0`
>
> **Usable hosts calculation:**
> - Host bits: $32 - 23 = 9$
> - Total addresses: $2^9 = 512$
> - Usable hosts: $512 - 2 = 510$
> - Address range: `200.23.16.0` → `200.23.17.255`

> [!tip]+ Interesting Note
> A `/23` gives two consecutive `/24` networks combined (`200.23.16.x` and `200.23.17.x`), resulting in 510 usable hosts instead of 254.

## Quick Reference

> [!abstract]+ Common CIDR Blocks
>
> | CIDR | Host Bits | Usable Hosts | Typical Use |
> |:---:|:---:|:---:|:---:|
> | /8 | 24 | 16,777,214 | Large ISP |
> | /16 | 16 | 65,534 | Large organization |
> | /24 | 8 | 254 | Small network |
> | /28 | 4 | 14 | Small subnet |
> | /30 | 2 | 2 | Point-to-point link |
> | /32 | 0 | 1 | Single host |

## Special IP Addresses

> [!info]+ Reserved Addresses
> ![[02068b758560ea32d81c44c0b3b98864.png]]
>
> These reserved addresses have specific meanings and **cannot be assigned to regular hosts**.

### This Host: `0.0.0.0`

> [!note]+ Definition
> | Binary | All 32 bits = 0 |
> |--------|-----------------|
> | Decimal | `0.0.0.0` |
>
> **Meaning:** "Me, right now, before I know my own IP address."
>
> **Used when:** A device is booting up and needs to request an IP address (e.g., during [[DHCP]] discovery).

### Local Broadcast: `255.255.255.255`

> [!note]+ Definition
> | Binary | All 32 bits = 1 |
> |--------|-----------------|
> | Decimal | `255.255.255.255` |
>
> **Meaning:** "Send this to everyone on my local network."
>
> **Used for:** [[DHCP]] requests, ARP. Routers **do not forward** this address.

### Directed Broadcast: `<Network>.255`

> [!note]+ Definition
> | Network part | Host part |
> |--------------|-----------|
> | Specific network ID | All ones |
>
> **Example:** `192.168.1.255` (for network `192.168.1.0/24`)
>
> **Meaning:** "Send this to everyone on that specific remote network."
>
> **Note:** Routers *can* forward this (though often disabled for security).

### Loopback: `127.x.x.x`

> [!note]+ Definition
> | First octet | Remaining |
> |-------------|-----------|
> | 127 | Anything (typically `0.0.1`) |
>
> **Most common:** `127.0.0.1` ("localhost")
>
> **Meaning:** "Send this back to myself."
>
> **Used for:**
> - Testing network software without a physical network
> - Inter-process communication on the same machine
> - Verifying TCP/IP stack functionality
>
> Traffic to `127.x.x.x` **never leaves the machine**.

## Related Concepts

> [!note]+ See Also
> - **[[IPv4]]**: IP addressing fundamentals
> - **[[Subnet]]**: Network subdivision
> - **[[DHCP]]**: Dynamic address assignment
> - **[[Hierarchical Addressing]]**: Route aggregation
> - **[[NAT]]**: Private address translation
> - **[[Network Layer]]**: Layer where CIDR operates

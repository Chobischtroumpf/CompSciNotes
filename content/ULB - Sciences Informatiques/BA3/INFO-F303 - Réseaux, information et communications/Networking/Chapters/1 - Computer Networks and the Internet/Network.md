---
title: Network
authors: Alessandro Dorigo
tags:
  - Network
---


> [!info]+ Definition
> A **network** is a collection of devices, routers, and links managed by an organization.
>
> ![[363ed2e0cd4c1296da8cd620cf94f97c.png]]

^89dac9

## [[ULB - Sciences Informatiques/BA3/INFO-F303 - Réseaux, information et communications/Networking/Chapters/1 - Computer Networks and the Internet/Internet#^c8a6b5|Internet]] [[Protocol#^4bfd4c|Protocol]] Stack
> [!abstract]- Five-Layer Architecture
> **Application Layer**:
> - **Function**: Support network applications
> - **Protocols**: HTTP, FTP, SMTP
> - **Data unit**: Message
>
> **Transport Layer:**
> - **Function**: Process-to-process data transfer
> - **Protocols**: TCP (reliable), UDP (unreliable)
> - **Data unit**: Segment
>
> **Network Layer:**
> - **Function**: Routing of packets from source to destination
> - **Protocols**: IP, routing protocols
> - **Data unit**: Datagram
>
> **Link Layer:**
> - **Function**: Data transfer between neighboring network elements
> - **Protocols**: Ethernet, WiFi
> - **Data unit**: Frame
>
> **Physical Layer:**
> - **Function**: Bit encoding/decoding
> - **Data unit**: Bits

| ![[f7be45923211de0f28f623248ef59792.png]] | ![[7b0ec748f10e6923e0dd9c9325afbd46.png]] |
| :----------------------------------: | :----------------------------------: |

> [!note]+ Additional OSI Layers
> The OSI reference model includes two extra layers not typically implemented separately in [[ULB - Sciences Informatiques/BA3/INFO-F303 - Réseaux, information et communications/Networking/Chapters/1 - Computer Networks and the Internet/Internet#^c8a6b5|Internet]] [[Protocol#^4bfd4c|protocols]]:
> - **Presentation Layer**: Encryption, compression, machine-specific conventions
> - **Session Layer**: Synchronization, checkpointing, recovery of data exchanges

![[a67d1e6ab52cbaef4eff7a97481f5942.png]]

As data moves down the [[Protocol#^4bfd4c|protocol]] stack:
1. **Application**: Creates message ($M$)
2. **Transport**: Adds transport header ($H_t$ $M$) → segment
3. **Network**: Adds network header ($H_n$ $H_t$ $M$) → datagram
4. **Link**: Adds link header ($H_l$ $H_n$ $H_t$ $M$) → frame
5. **Physical**: Transmits as bits

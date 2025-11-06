---
title: Network
authors: Alessandro Dorigo
tags:
  - Network
---


> [!info]+ Definition
> A **network** is a collection of devices, routers, and links managed by an organization.
>
> ![[Pasted image 20250918143524.png]]

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

| ![[Pasted image 20250918154322.png]] | ![[Pasted image 20250918154454.png]] |
| :----------------------------------: | :----------------------------------: |

> [!note]+ Additional OSI Layers
> The OSI reference model includes two extra layers not typically implemented separately in [[ULB - Sciences Informatiques/BA3/INFO-F303 - Réseaux, information et communications/Networking/Chapters/1 - Computer Networks and the Internet/Internet#^c8a6b5|Internet]] [[Protocol#^4bfd4c|protocols]]:
> - **Presentation Layer**: Encryption, compression, machine-specific conventions
> - **Session Layer**: Synchronization, checkpointing, recovery of data exchanges

![[Pasted image 20250918154713.png]]

As data moves down the [[Protocol#^4bfd4c|protocol]] stack:
1. **Application**: Creates message ($M$)
2. **Transport**: Adds transport header ($H_t$ $M$) → segment
3. **Network**: Adds network header ($H_n$ $H_t$ $M$) → datagram
4. **Link**: Adds link header ($H_l$ $H_n$ $H_t$ $M$) → frame
5. **Physical**: Transmits as bits

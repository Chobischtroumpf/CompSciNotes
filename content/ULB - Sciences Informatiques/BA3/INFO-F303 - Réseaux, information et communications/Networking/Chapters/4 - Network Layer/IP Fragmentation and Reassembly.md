---
title: IP Fragmentation and Reassembly
authors: Alessandro Dorigo, Mihai Bors
tags:
  - Network
---
> [!info]+ Definition
> **IP Fragmentation** is the process of dividing a large IP packet into smaller fragments when it exceeds the Maximum Transmission Unit (MTU) of a network link. **Reassembly** is the process of combining these fragments back into the original packet at the destination host.

## Why Fragmentation?

> [!abstract]+ MTU Constraints
> **Network links have MTU (Maximum Transfer Unit):**
> - Specifies the largest possible link-level frame
> - Different link types have different MTUs
>
> **Common MTU values:**
>
> | Link Type | MTU (bytes) |
> |-----------|-------------|
> | Ethernet | 1500 |
> | PPPoE (DSL) | 1492 |
> | IPv6 minimum | 1280 |
> | Dial-up | 576 |
>
> When a large IP packet exceeds the MTU, it must be **fragmented** into smaller packets.

## Fragmentation Process

> [!note]+ Key Characteristics
> **Where fragmentation occurs:**
> - Performed by routers when packet exceeds outgoing link's MTU
> - Fragments can be further fragmented at subsequent routers
>
> **Where reassembly occurs:**
> - Only at the **final destination** host
> - Not at intermediate routers (not transparent)
> - Destination uses IP header fields to identify and order fragments

## IP Header Fields for Fragmentation

> [!info]+ Fragmentation Control Fields
> Three fields in the [[IPv4 Structure|IP header]] control fragmentation:
>
> **Identification (16 bits):**
> - Unique identifier assigned by sender
> - All fragments of the same original packet share this ID
>
> **Flags (3 bits):**
> - Bit 0: Reserved (must be 0)
> - Bit 1: **DF** (Don't Fragment) - 0 = may fragment, 1 = don't fragment
> - Bit 2: **MF** (More Fragments) - 0 = last fragment, 1 = more fragments follow
>
> **Fragment Offset (13 bits):**
> - Position of this fragment in the original packet
> - Measured in units of 8 bytes (64 bits)
> - Allows receiver to reassemble in correct order

## Fragmentation Example

> [!example]+ Fragmenting a 4000-byte Packet
> ![[aa425c15ac42736dd7c0b101cbce5027.png]]
>
> **Given:**
> - Original packet: 4000 bytes total
> - MTU: 1500 bytes
> - IP header: 20 bytes
> - Maximum data per fragment: 1480 bytes
>
> **Original packet:**
>
> | Length | ID | Flag | Offset |
> |--------|-----|------|--------|
> | 4000 | x | 0 | 0 |
>
> **After fragmentation (3 fragments):**
>
> | Fragment | Length | ID | MF Flag | Offset | Data Bytes |
> |----------|--------|-----|---------|--------|------------|
> | 1 | 1500 | x | 1 | 0 | 0-1479 |
> | 2 | 1500 | x | 1 | 185 | 1480-2959 |
> | 3 | 1040 | x | 0 | 370 | 2960-3979 |

> [!tip]+ Understanding the Offset Calculation
> **Offset is measured in 8-byte units:**
>
> $$\text{Offset} = \frac{\text{Byte position}}{8}$$
>
> **Example calculations:**
> - Fragment 1: starts at byte 0 → offset = $0 \div 8 = 0$
> - Fragment 2: starts at byte 1480 → offset = $1480 \div 8 = 185$
> - Fragment 3: starts at byte 2960 → offset = $2960 \div 8 = 370$

## Interpreting Fragment Fields

> [!abstract]+ Reading Fragment Information
> **How to identify fragments:**
>
> | Field Value | Meaning |
> |-------------|---------|
> | Offset = 0 | First fragment |
> | MF = 1 | More fragments follow |
> | MF = 0 | Last fragment |
> | MF = 0, Offset = 0 | Unfragmented packet |
>
> **Note:** The MF flag of the last fragment is a copy of the MF flag from before fragmentation (typically 0).

## Reassembly Process

> [!note]+ At the Destination Host
> **Reassembly steps:**
> 1. Collect all fragments with the same Identification value
> 2. Order fragments using Fragment Offset
> 3. Verify all fragments received (MF flags and offsets must be consistent)
> 4. Combine data portions in order
> 5. Deliver complete packet to upper layer
>
> **Timeout:**
> - If not all fragments arrive within a timeout period
> - Destination discards all received fragments
> - No partial delivery to upper layer

## IPv6 Difference

> [!warning]+ No Router Fragmentation in IPv6
> **[[IPv6]] handles fragmentation differently:**
> - Routers do **not** fragment packets
> - Fragmentation only possible at the **source host**
> - Uses Path MTU Discovery to find smallest MTU along path
> - Simplifies router processing

## Related Concepts

> [!note]+ See Also
> - **[[IPv4 Structure]]**: IP header fields used for fragmentation
> - **[[IPv6]]**: Different fragmentation approach
> - **[[Network Layer]]**: Layer where fragmentation occurs
> - **[[Data Plane]]**: Per-router forwarding function

---
title: IPv4 Structure
authors: Alessandro Dorigo, Mihai Bors
tags:
  - Network
---
> [!info]+ Definition
> The **IP packet structure** (also called IP datagram) defines the format for transmitting data over the Internet Protocol. Each packet consists of a header (containing control information) and a payload (containing the actual data, typically a [[TCP]] or [[UDP]] segment).

## IPv4 Packet Format

```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|Version|  IHL  |Type of Service|          Total Length         |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|         Identification        |Flags|      Fragment Offset    |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|  Time to Live |    Protocol   |         Header Checksum       |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                       Source Address                          |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Destination Address                        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Options                    |    Padding    |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                             data                              |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

> [!abstract]+ Overhead
> **Total overhead for TCP+IP:**
> - 20 bytes of TCP header
> - 20 bytes of IP header
> - = 40 bytes + application layer overhead

## Header Fields

### Version and Header Length

> [!note]+ Version (4 bits)
> **IP protocol version number**
> - Value 4 for IPv4
> - Value 6 for [[IPv6]]

> [!note]+ IHL - Internet Header Length (4 bits)
> **Length of the IP header in 32-bit words**
>
> **Purpose:**
> - Points to the beginning of the data
> - Required because Options field is variable length
>
> **Values:**
> - Minimum: 5 (20 bytes, no options)
> - Maximum: 15 (60 bytes with options)
>
> **Calculation:**
> - Multiply value by 4 to get header size in bytes
> - Example: IHL = 5 → 20 byte header

### Type of Service

> [!note]+ Type of Service (8 bits)
> **Quality of service parameters**
>
> ```
>    0     1     2     3     4     5     6     7
> +-----+-----+-----+-----+-----+-----+-----+-----+
> |                 |     |     |     |     |     |
> |   PRECEDENCE    |  D  |  T  |  R  |  0  |  0  |
> |                 |     |     |     |     |     |
> +-----+-----+-----+-----+-----+-----+-----+-----+
> ```
>
> **Modern usage:**
> - **Diffserv:** Differentiated services for QoS
> - **ECN:** Explicit Congestion Notification (last 2 bits)
>
> **Legacy fields:**
> - D: 0 = Normal Delay, 1 = Low Delay
> - T: 0 = Normal Throughput, 1 = High Throughput
> - R: 0 = Normal Reliability, 1 = High Reliability

### Length and Identification

> [!note]+ Total Length (16 bits)
> **Total packet length in bytes (header + data)**
>
> **Range:**
> - Maximum: 65,535 bytes (64K)
> - Typical: 1500 bytes or less (limited by MTU)
>
> **Minimum requirement:**
> - All hosts must accept datagrams up to 576 bytes
> - Recommended to send larger only if destination can handle it

> [!note]+ Identification (16 bits)
> **Identifies fragments of the same original packet**
>
> **Purpose:**
> - Assigned by sender
> - Used by receiver to reassemble fragments
> - All fragments of same packet share this ID
>
> See [[IP Fragmentation and Reassembly]] for details.

### Fragmentation Control

> [!note]+ Flags (3 bits)
> **Control flags for fragmentation**
>
> ```
>     0   1   2
>   +---+---+---+
>   |   | D | M |
>   | 0 | F | F |
>   +---+---+---+
> ```
>
> | Bit | Name | Meaning |
> |-----|------|---------|
> | 0 | Reserved | Must be zero |
> | 1 | DF | 0 = May Fragment, 1 = Don't Fragment |
> | 2 | MF | 0 = Last Fragment, 1 = More Fragments |

> [!note]+ Fragment Offset (13 bits)
> **Position of this fragment within the original packet**
>
> **Characteristics:**
> - Measured in units of 8 bytes (64 bits)
> - First fragment has offset 0
> - Allows receiver to reassemble in correct order
>
> **Example:**
> - Offset = 185 means fragment starts at byte 1480 (185 × 8)

### TTL and Protocol

> [!note]+ Time to Live - TTL (8 bits)
> **Remaining maximum hops before packet is discarded**
>
> **Purpose:**
> - Prevents packets from looping forever
> - Bounds maximum datagram lifetime
>
> **Behavior:**
> - Decremented by 1 at each router
> - Packet discarded when TTL reaches 0
> - Originally meant to be seconds, but practically counts hops

> [!note]+ Protocol (8 bits)
> **Identifies the upper layer protocol in the data portion**
>
> **Common values:**
>
> | Value | Protocol |
> |-------|----------|
> | 1 | ICMP |
> | 6 | [[TCP]] |
> | 17 | [[UDP]] |
> | 89 | OSPF |

### Error Detection

> [!note]+ Header Checksum (16 bits)
> **Error detection for the header only**
>
> **Characteristics:**
> - Covers header fields only, not data
> - Recomputed at each router (because TTL changes)
> - Uses one's complement arithmetic (same as [[Checksum|TCP/UDP]])
>
> **Note:** [[IPv6]] removes this field to speed up processing

### Address Fields

> [!note]+ Source Address (32 bits)
> **IP address of the sending host**
>
> See [[IPv4]] for address format details.

> [!note]+ Destination Address (32 bits)
> **IP address of the receiving host**
>
> Used by routers for [[Forwarding]] decisions via [[Longest Prefix Matching]].

## IP Options

> [!info]+ Options Field (Variable)
> **Optional parameters at end of IP header**
>
> **Characteristics:**
> - May or may not appear in datagrams
> - Must be implemented by all IP modules
> - Variable length, padded to 32-bit boundary
>
> **Format:**
> - Single octet options (End of List, No-Op)
> - Multi-octet options (type, length, data)

> [!example]+ Common Options
>
> | Option | Purpose |
> |--------|---------|
> | End of Option List | Marks end of options |
> | No Operation | Padding for alignment |
> | Record Route | Records route taken by packet |
> | Timestamp | Records time at each hop |
> | Loose Source Routing | Specifies intermediate routers (can use others) |
> | Strict Source Routing | Specifies exact route (must follow) |

### Padding

> [!note]+ Padding (Variable)
> **Ensures header ends on 32-bit boundary**
>
> - Composed of zeros
> - Makes header length multiple of 4 bytes
> - Ensures data begins on 32-bit boundary

## Header Size Summary

> [!abstract]+ IP Header Sizes
> **Minimum header:** 20 bytes
> - No options
> - IHL = 5
>
> **Maximum header:** 60 bytes
> - 40 bytes of options
> - IHL = 15
>
> **Typical header:** 20 bytes
> - Options rarely used in practice

## Related Concepts

> [!note]+ See Also
> - **[[IPv4]]**: IP addressing fundamentals
> - **[[IPv6]]**: Next generation with simplified header
> - **[[IP Fragmentation and Reassembly]]**: When packets exceed MTU
> - **[[TCP Structure]]**: Transport layer segment format
> - **[[Checksum]]**: Error detection mechanism
> - **[[Network Layer]]**: Layer where IP operates

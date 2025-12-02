---
title: IPv6 Structure
authors: Mihai Bors
tags:
  - Network
---
> [!info]+ Definition
> The **IPv6 packet structure** defines the format for transmitting data over Internet Protocol version 6. The header is a fixed 40 bytes with a simplified design compared to [[IPv4 Structure|IPv4]], enabling faster router processing and supporting extension headers for optional features.

## IPv6 Packet Format

```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|Version| Traffic Class |           Flow Label                  |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|         Payload Length        |  Next Header  |   Hop Limit   |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                                                               |
+                                                               +
|                                                               |
+                         Source Address                        +
|                                                               |
+                          (128 bits)                           +
|                                                               |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                                                               |
+                                                               +
|                                                               |
+                      Destination Address                      +
|                                                               |
+                          (128 bits)                           +
|                                                               |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                             data                              |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

## Header Fields

### Version and Traffic Class

> [!note]+ Version (4 bits)
> **IP protocol version number**
> - Value: 6 (for IPv6)
> - Same position as in [[IPv4 Structure|IPv4]] for compatibility

> [!note]+ Traffic Class (8 bits)
> **Quality of service and priority information**
>
> **Purpose:**
> - Similar to IPv4's Type of Service field
> - Enables differentiated services (DiffServ)
> - Last 2 bits used for ECN (Explicit Congestion Notification)
>
> **Usage:**
> - Identifies priority among packets in a flow
> - Allows routers to provide different treatment levels

### Flow Label

> [!note]+ Flow Label (20 bits)
> **Identifies packets belonging to the same flow**
>
> **Purpose:**
> - Enables special handling for a sequence of packets
> - Routers can identify flows without examining higher-layer headers
> - Facilitates Quality of Service (QoS) mechanisms
>
> **Characteristics:**
> - Non-zero value indicates a flow
> - Zero means no flow label assigned
> - Concept of "flow" not strictly defined in the standard
>
> **Benefit:** Routers can make forwarding decisions without looking into [[TCP]] or [[UDP]] headers (e.g., port numbers)

### Length and Protocol

> [!note]+ Payload Length (16 bits)
> **Length of the IPv6 payload in bytes**
>
> **Includes:**
> - Any extension headers present
> - The upper-layer data ([[TCP]]/[[UDP]] segment)
>
> **Does NOT include:**
> - The 40-byte IPv6 header itself
>
> **Maximum value:** 65,535 bytes
>
> **Note:** For jumbo payloads exceeding 65,535 bytes, the Hop-by-Hop Options extension header is used with payload length set to 0.

> [!note]+ Next Header (8 bits)
> **Identifies the type of header immediately following the IPv6 header**
>
> **Key feature:** Allows chaining of multiple extension headers
>
> **Common values:**
>
> | Value | Header Type |
> |-------|-------------|
> | 0 | Hop-by-Hop Options |
> | 6 | [[TCP]] |
> | 17 | [[UDP]] |
> | 43 | Routing Header |
> | 44 | Fragment Header |
> | 58 | ICMPv6 |
> | 59 | No Next Header |
>
> **Note:** Uses the same values as IPv4's Protocol field for upper-layer protocols

### Hop Limit

> [!note]+ Hop Limit (8 bits)
> **Maximum number of hops before packet is discarded**
>
> **Behavior:**
> - Decremented by 1 at each forwarding node
> - Packet discarded if Hop Limit reaches 0 during forwarding
> - Destination host processes packets with Hop Limit = 0 normally
>
> **Replaces:** IPv4's Time to Live (TTL) field
>
> **Range:** 0-255 hops

### Address Fields

> [!note]+ Source Address (128 bits)
> **IPv6 address of the packet's originator**
>
> See [[IPv6]] for address format and notation.

> [!note]+ Destination Address (128 bits)
> **IPv6 address of the intended recipient**
>
> **Note:** May not be the ultimate recipient if a Routing extension header is present.

## What's Missing from IPv4

> [!abstract]+ Simplified Header Design
> IPv6 removes several IPv4 fields to speed processing:
>
> | Removed Field | Reason |
> |---------------|--------|
> | **Header Checksum** | Speeds router processing; upper layers have checksums |
> | **Header Length (IHL)** | Fixed 40-byte header; no variable options |
> | **Identification, Flags, Fragment Offset** | No router fragmentation; only source can fragment |
> | **Options + Padding** | Moved to extension headers (optional) |
>
> **Result:** Routers process IPv6 headers faster than IPv4

## Extension Headers

> [!info]+ Optional Header Chaining
> **Extension headers replace IPv4 options:**
> - Placed between IPv6 header and upper-layer header
> - Chained using Next Header field
> - Processed only by destination (except Hop-by-Hop)
>
> **Common extension headers:**
>
> | Header | Purpose |
> |--------|---------|
> | Hop-by-Hop Options | Options examined by every node |
> | Routing | Specifies intermediate destinations |
> | Fragment | Fragmentation info (source-only) |
> | Destination Options | Options for destination only |
> | Authentication | IPsec authentication |
> | ESP | IPsec encryption |

> [!example]+ Header Chain Example
> ```
> IPv6 Header → Routing Header → TCP Header → Data
> (Next: 43)    (Next: 6)
> ```
>
> The Next Header field creates a chain leading to the final payload.

## Header Size Comparison

> [!abstract]+ IPv4 vs IPv6 Headers
>
> | Aspect | IPv4 | IPv6 |
> |--------|------|------|
> | **Base header size** | 20-60 bytes (variable) | 40 bytes (fixed) |
> | **Address size** | 32 bits | 128 bits |
> | **Options** | In header | Extension headers |
> | **Fragmentation** | Router or source | Source only |
> | **Checksum** | Yes | No |

## Related Concepts

> [!note]+ See Also
> - **[[IPv6]]**: Protocol overview and addressing
> - **[[IPv4 Structure]]**: IPv4 header for comparison
> - **[[IP Fragmentation and Reassembly]]**: Fragmentation differences
> - **[[TCP Structure]]**: Transport layer segment format
> - **[[UDP]]**: Transport protocol identified by Next Header
> - **[[Network Layer]]**: Layer where IPv6 operates

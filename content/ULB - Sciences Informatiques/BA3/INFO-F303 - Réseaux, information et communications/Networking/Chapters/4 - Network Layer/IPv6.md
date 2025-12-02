---
title: IPv6
authors: Alessandro Dorigo, Mihai Bors
tags:
  - Network
---
> [!info]+ Definition
> **IPv6 (Internet Protocol version 6)** is the next generation Internet Protocol that uses 128-bit addresses to replace [[IPv4]]'s 32-bit addresses. The protocol features a simplified header format designed for faster router processing and native support for flow-based traffic handling.

## Why IPv6?

> [!abstract]+ Motivation for IPv6
> **Address exhaustion:**
> - 32-bit IPv4 address space becoming fully allocated
> - IPv6 provides $2^{128}$ addresses (vs IPv4's $2^{32}$)
>
> **Speed improvements:**
> - 40-byte fixed-length header (no variable options in base header)
> - No fragmentation at routers
> - No header checksum (removed to speed processing)
>
> **New capabilities:**
> - Native support for different treatment of "flows"
> - Built-in extension header mechanism
>
> **Design requirement:**
> - No changes needed in higher layers ([[TCP]], [[UDP]]) or lower layers

## IPv6 Address Format

> [!note]+ Address Notation
> **Format:** `x:x:x:x:x:x:x:x` where each `x` is a 16-bit hexadecimal field
>
> **Full address example:**
> ```
> 2001:0000:130F:0000:0000:09C0:876A:130B
> ```
>
> **Simplification rules:**
>
> | Rule | Example |
> |------|---------|
> | Leading zeros optional | `2001:0:130F:0:0:9C0:876A:130B` |
> | Consecutive zeros as `::` | `2001:0:130F::9C0:876A:130B` |
>
> **Important:** `::` can only be used **once** per address

> [!example]+ Special Addresses
>
> | Address | Shorthand | Purpose |
> |---------|-----------|---------|
> | `0:0:0:0:0:0:0:0` | `::` | This host (unspecified) |
> | `0:0:0:0:0:0:0:1` | `::1` | Loopback address |
> | `FF01:0:0:0:0:0:0:1` | `FF01::1` | All nodes multicast |

## Address Structure

> [!abstract]+ Hierarchical Addressing
> IPv6 uses [[Hierarchical Addressing]] for efficient routing aggregation:
>
> ```
> |←────── 64 bits ──────→|←────── 64 bits ──────→|
> |        Prefix         |        Suffix         |
> |   (Site identifier)   | (Interface identifier)|
> ```
>
> **Prefix (64 bits):**
> - Identifies a site
> - Initial part (typically 48 bits) assigned by ISP
>
> **Suffix (64 bits):**
> - Identifies an interface within the site
> - Can be assigned via: DHCPv6, derived from MAC address, or pseudo-random

- See [[IPv6 Structure]] for complete header format.

## Link-Local Addresses

> [!info]+ Special Scope Addresses
> **Link-local addresses** are used for communication within a single network link.
>
> **Characteristics:**
> - Not routable beyond the local link
> - Scope limited to a single link segment
> - Suffix derived from 48-bit interface MAC address
> - Prefix is always `FE80:0:0:0`
>
> **Format:**
> ```
> Link-local = FE80:0:0:0:<interface-derived-suffix>
> ```
>
> **Example:** `FE80::1` for a simple interface

## Transition: IPv4 to IPv6

> [!warning]+ The Challenge
> **Not all routers can be upgraded simultaneously:**
> - No "flag days" possible on the Internet
> - Mixed IPv4 and IPv6 routers must coexist
> - Gradual transition over many years

## Tunneling

> [!abstract]+ IPv6 over IPv4 Networks
> **Tunneling:** IPv6 packet carried as *payload* inside an IPv4 packet among IPv4 routers.
>
> ![[66ed8eb5f9ac3176670d29d29e39223b.png]]
>
> **Encapsulation structure:**
>
> | Layer | Contents |
> |-------|----------|
> | IPv4 Header | src: IPv4 addr, dest: IPv4 addr |
> | IPv6 Packet (payload) | IPv6 header + original data |
>

## Tunneling Scenarios

> [!example]+ Scenario 1: Direct IPv6 Connection
> ![[4bfff9d7650e05aa4943b4681e2f8cab.png]]
>
> **Network:** A (IPv6) — B (IPv6) — *Ethernet* — E (IPv6) — F (IPv6)
>
> Standard IPv6 packet in link-layer frame. No tunneling needed.

> [!example]+ Scenario 2: IPv4 Network Between IPv6 Routers
> ![[eb0fe4d7393bb1312923956833b7789c.png]]
>
> **Network:** A (IPv6) — B (IPv6/v4) — *IPv4 network* — E (IPv6/v4) — F (IPv6)
>
> IPv6 packets are **tunneled** through the IPv4 network.

> [!example]+ Scenario 3: Detailed Tunnel View
> ![[031c95f3150fa652edbc7fefda2ba549.png]]
>
> **Logical view:**
> ![[a0d4ffd3fe79012a1000e1d533433807.png]]
>
> **Physical view:**
> ![[e1344040e7829a73100c0e2beca59282.png]]
>
> **Packet flow:**
>
> | Segment | Packet Format |
> |---------|---------------|
> | A → B | IPv6 (flow: X, src: A, dest: F, data) |
> | B → C → D → E | IPv4 (src: B, dest: E) containing IPv6 packet |
> | E → F | IPv6 (flow: X, src: A, dest: F, data) |

## IPv6 Adoption

> [!info]+ Current Status
> As of 2025, Google statistics indicate that roughly **45%** of connections to Google services use IPv6.
>
> **Adoption varies by:**
> - Country/region
> - ISP support
> - Enterprise vs consumer networks

## Related Concepts

> [!note]+ See Also
> - **[[IPv6 Structure]]**: Detailed header format
> - **[[IPv4]]**: Previous IP version
> - **[[IPv4 Structure]]**: IPv4 header for comparison
> - **[[IP Fragmentation and Reassembly]]**: Different approach in IPv6
> - **[[Hierarchical Addressing]]**: Route aggregation
> - **[[Network Layer]]**: Layer where IPv6 operates

---
title: ICMP
authors: Mihai Bors
tags:
  - Network
---
> [!info]+ Definition
> **ICMP (Internet Control Message Protocol)** is a network-layer protocol used by hosts and routers to communicate network-level information, primarily for error reporting and diagnostic functions. ICMP messages are carried inside IP packets, making it technically "above" IP in the protocol stack.

## Purpose

> [!abstract]+ ICMP Functions
> **Error reporting:**
> - Unreachable host, network, port, or protocol
> - TTL expired (packet discarded)
> - Bad IP header
>
> **Diagnostic tools:**
> - Echo request/reply (used by `ping`)
> - Router discovery and advertisement

## ICMP Message Format

> [!note]+ Message Structure
> **Each ICMP message contains:**
> - **Type:** Category of message
> - **Code:** Specific condition within type
> - **First 8 bytes of IP packet:** From the packet that caused the error
>
> This allows the sender to identify which packet triggered the error.

## Common ICMP Message Types

> [!info]+ Type and Code Reference
>
> | Type | Code | Description |
> |:----:|:----:|:------------|
> | 0 | 0 | Echo reply (ping response) |
> | 3 | 0 | Destination network unreachable |
> | 3 | 1 | Destination host unreachable |
> | 3 | 2 | Destination protocol unreachable |
> | 3 | 3 | Destination port unreachable |
> | 3 | 6 | Destination network unknown |
> | 3 | 7 | Destination host unknown |
> | 4 | 0 | Source quench (congestion control - deprecated) |
> | 8 | 0 | Echo request (ping) |
> | 9 | 0 | Router advertisement |
> | 10 | 0 | Router discovery |
> | 11 | 0 | TTL expired |
> | 12 | 0 | Bad IP header |

## Traceroute and ICMP

> [!example]+ How Traceroute Works
> ![[96d79a53fd316e8175cff57c9e28da99.png]]
>
> **Process:**
> 1. Source sends sets of UDP segments to destination
> 2. First set has TTL=1, second set has TTL=2, and so on
> 3. Packet in $n^{th}$ set arrives at $n^{th}$ router
> 4. Router discards packet (TTL expired) and sends ICMP message back
> 5. ICMP message (type 11, code 0) includes router name and IP address
> 6. Source records RTT for each hop

> [!success]+ Stopping Criteria
> **When tracing is complete:**
> - UDP segment eventually arrives at destination host
> - Destination returns ICMP "port unreachable" message (type 3, code 3)
> - Source stops sending probes
>
> **Note:** Traceroute typically sends 3 probes at each TTL level to measure RTT variability.

## Related Concepts

> [!note]+ See Also
> - **[[IPv4 Structure]]**: IP header fields including TTL
> - **[[Network Layer]]**: Layer where ICMP operates
> - **[[UDP]]**: Transport protocol used by traceroute probes
> - **[[Router Architecture]]**: Routers generate ICMP messages

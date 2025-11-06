---
title: 3-way-handshake
authors: Alessandro Dorigo
tags:
  - Network
---


> [!info]+ Definition
> **3-way-handshake** is the standard [[TCP]] connection establishment protocol that uses three message exchanges to ensure both client and server are ready to communicate and agree on initial sequence numbers. It solves the problems inherent in [[2-way-handshake]].

## Protocol Operation

> [!success]+ Three-Step Process
> ![[Pasted image 20251102141937.png]]
>
> **Step 1: `SYN` (Client -> Server)**
> - Client chooses initial sequence number `x`
> - Sends TCP `SYN` message without data
> - Starts timer for `SYN` retransmission
> - Client: `CLOSED -> SYN SENT`
>
> **Step 2: `SYNACK` (Server -> Client)**
> - Server chooses initial sequence number `y`
> - Sends TCP `SYNACK` message, ACKing `SYN`
> - `SYNACK(y, x+1)`: "I got your `x`, here's my `y`"
> - Server: `LISTEN -> SYN RCVD`
>
> **Step 3: `ACK` (Client → Server)**
> - Client receives `SYNACK(x+1)` from server (indicates server is live)
> - Sends `ACK` for `SYNACK` with `ACK(y+1)`
> - Segment may contain client->server data with `seq=x+1`
> - Client: `SYN SENT -> ESTAB`
>
> **Connection Established**:
> - Server receives `ACK(y+1)` (indicates client is live)
> - Allocates buffer
> - Server: `SYN RCVD -> ESTAB`

## Robustness: Lost `SYNACK` Scenario

> [!example]+ Handling Lost SYNACK
> ![[Pasted image 20251102145427.png]]
>
> **What happens**:
> 1. **Normal start**: Client sends `SYN(x)`
> 2. **Server responds**: `SYNACK(y, x+1)` sent but lost (X)
> 3. **Client retransmits**: Timeout triggers `SYN(x)` retransmission
> 4. **Server handles duplicate**:
>    - Already in `ESTAB` state with sequence number `y`
>    - Retransmits `ACK(y+1)`
>    - Can include `data(x+1)` immediately
> 5. **Recovery complete**: Connection established successfully

## Security: Sequence Number Validation

> [!warning]+ Preventing Replay Attacks
> **Security check requirement**:
> - Server receives `SYNACK(y', x+1)` from somewhere
> - Server must reject if `y != y'`
> - Sequence number `y'` must not have been used recently with this client
> - "Recent" = within maximum packet lifetime (MSL, typically 2 minutes)

## Connection Refused

> [!note]+ Port Not Open
> **When server port not open**:
> - TCP server sends back `RST` segment
> - Resets connection attempt
> - Client receives error

## Choosing Initial Sequence Numbers

> [!abstract]+ Sequence Number Selection
> ![[Pasted image 20251102145555.png]]
>
> **Constraints for choosing x and y**:
> - `x` and `y` must not have been used recently in former connection between:
>   - Same client (IP and port)
>   - Same server (IP and port)
> - "Recently" = less than TCP Maximum Segment Lifetime (MSL)
> - Otherwise, duplicate segments from former connection could be confused with new connection
>
> **Practical implementation**:
> - Same client port cannot be reused sooner than 2 MSL for new connection
> - x can be chosen randomly (client port reuse restriction handles safety)
> - y picked at random and checked not recently used between same endpoints

## Client/Server State Machines

> [!note]+ Connection State Transitions
> ![[Pasted image 20251102145746.png]]
>
> **Five connection states**:
> - `CLOSED`: No connection
> - `LISTEN`: Server waiting for connection request
> - `SYN RCVD`: Server received SYN, sent SYNACK
> - `SYN SENT`: Client sent SYN, waiting for SYNACK
> - `ESTAB`: Connection established, data transfer ready
>
> **Client state progression**:
> ```
> CLOSED -> SYN SENT → ESTAB
> ```
>
> **Server state progression**:
> ```
> CLOSED -> LISTEN → SYN RCVD → ESTAB
> ```

## Related Concepts

> [!note]+ See Also
> - **[[TCP Connection Management]]**: Connection lifecycle overview
> - **[[2-way-handshake]]**: Flawed alternative this improves
> - **[[TCP]]**: Protocol using this handshake
> - **[[TCP Structure]]**: SYN/ACK flags in segment header
> - **[[Reliable Data Transfer]]**: Connection enables reliable transfer
> - **[[Transport Layer]]**: Layer where handshake occurs
> - **[[RTT]]**: Affects handshake timing

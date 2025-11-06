---
title: 2-way-handshake
authors: Alessandro Dorigo
tags:
  - Network
---


> [!info]+ Definition
> **2-way-handshake** is a flawed connection establishment protocol where the client sends a connection request and the server responds with acceptance. This simple approach has critical vulnerabilities that make it unsuitable for [[TCP]].

## Protocol Operation

> [!note]+ Handshake Steps
> **Simple 2-way exchange**:
> ```
> Client -> Server: req_conn(x)
> Server -> Client: acc_conn(x)
> Both enter ESTAB state
> ```
>
> ![[Pasted image 20251102141607.png]]
>
> **Process**:
> - Client sends connection request with initial sequence number x
> - Server accepts and acknowledges
> - Connection established

## Problems with 2-Way Handshake

> [!fail]+ Half-Open Connection
> ![[Pasted image 20251102141658.png]]
>
> **Scenario**:
> 1. Client sends `req_conn(x)`
> 2. Server sends `acc_conn(x)` (enters `ESTAB`)
> 3. Timeout before `acc_conn(x)` is received
> 4. Client retransmits `req_conn(x)`
> 5. `acc_conn(x)` received, `ESTAB`
> 6. Client terminates connection
> 7. Server forgets about `x`
> 8. **Problem**: Retransmitted `req_conn(x)` opens new connection
>
> **Issue**: Half-open connection where server thinks connection exists but client has moved on

> [!fail]+ Duplicate Data Accepted
> ![[Pasted image 20251102141732.png]]
>
> **Scenario**:
> - Same problem as above but with data transmission
> - Duplicate connection causes data to be accepted twice
> - Old duplicate segments from previous connection confuse new connection

## The Solution

> [!success]+ Fix: 3-Way Handshake
> The [[3-way-handshake]] solves these problems by:
> - Adding a third acknowledgment step
> - Ensuring both sides confirm connection establishment
> - Verifying sequence numbers before accepting data

## Related Concepts

> [!note]+ See Also
> - **[[TCP Connection Management]]**: Connection setup overview
> - **[[3-way-handshake]]**: Correct solution to these problems
> - **[[TCP]]**: Protocol that uses 3-way handshake
> - **[[TCP Structure]]**: `SYN`/`ACK` flags used in handshake
> - **[[Transport Layer]]**: Layer where handshake occurs

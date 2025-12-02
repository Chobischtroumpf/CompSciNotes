---
title: Demultiplexing
authors: Mihai Bors
tags:
  - Network
---
> [!info]+ Definition
> **Demultiplexing** is the process used by the receiver to deliver received segments to the correct socket using header information. It's the complementary operation to [[Multiplexing]].

## How Demultiplexing Works

> [!abstract]- Receiver-Side Process
> **At the transport layer, the receiver**:
> 1. Receives IP datagrams from network layer
> 2. Each datagram has source and destination IP addresses
> 3. Each datagram carries one transport-layer segment ([[UDP]] or [[TCP]])
> 4. Each segment has source and destination port numbers
> 5. Host uses IP addresses and port numbers to direct segment to appropriate socket

## Header Information Used

> [!note]+ Demultiplexing Keys
> **Information extracted from headers**:
>
> **From IP header (Network layer)**:
> - Source IP address
> - Destination IP address
>
> **From Transport header**:
> - Source port number
> - Destination port number
>
> **How used**:
> - Receiving host combines these fields
> - Determines which socket should receive the data
> - Different protocols use different combinations
>
> ![[4855448d50173b699eb08c2e7f9e8e44.png]]

## UDP Demultiplexing

> [!info]+ UDP's Simple Approach
> **UDP uses only 2 values for demultiplexing**:
> - Destination IP address
> - Destination port number
>
> **Process**:
> 1. When creating UDP socket, app may specify host-local port number
> 2. When creating datagram to send, app must specify:
>    - Destination IP address
>    - Destination port number (remote process ID)
> 3. When receiving UDP segment:
>    - Checks destination port number in segment
>    - Directs segment to socket with that port number
>
> **Key characteristic**:
> - **IP packets with same destination port number** (regardless of source) **are directed to same UDP socket**
> - Source information not used for socket selection
> - One socket can receive from multiple senders
>
> ![[fe50d0edc21cb6d23e26c01a06d20155.png]]

> [!example]+ UDP Demultiplexing Example
> **Scenario**:
> - Server has UDP socket on port `9157`
> - Three different clients send datagrams to `9157`
>
> **What happens**:
> - All three datagrams directed to same socket
> - Server sees different source IP/port for each
> - But all delivered through single socket
> - Application must track sources if needed

## TCP Demultiplexing

> [!info]+ TCP's 4-Tuple Approach
> **TCP uses 4 values for demultiplexing**:
> 1. Source IP address
> 2. Source port number
> 3. Destination IP address
> 4. Destination port number
>
> **Why more complex?**
> - Web servers have different TCP sockets for each connecting client
> - Non-persistent HTTP: different socket for each request
> - All sockets associated with same server port number
> - Destination port number alone insufficient
>
> **Process**:
> 1. Each TCP connection socket associated with single TCP connection
> 2. Connection identified by 4-tuple (connection ID)
> 3. When receiving TCP segment from network layer:
>    - Uses all four values to identify connection
>    - Directs segment to appropriate TCP connection socket
>
> **Key characteristic**:
> - **Each client connection gets its own socket**
> - Multiple clients to same server port use different sockets
> - Server distinguishes by full 4-tuple
>
> ![[d24d65d325b33e3108197467a06fe1e6.png]]

> [!example]+ TCP Demultiplexing Example
> **Scenario**:
> - Web server listening on port 80
> - Three clients connect to the server
>
> **What happens**:
> ```
> Client A: 145.37.20.11:5555 -> Server: 200.10.5.1:80 (Socket SA)
> Client B: 145.37.20.11:5556 -> Server: 200.10.5.1:80 (Socket SB)
> Client C: 145.37.30.22:5555 -> Server: 200.10.5.1:80 (Socket SC)
> ```
>
> - Three different sockets created
> - Each identified by unique 4-tuple
> - Even though destination is same (port `80`)
> - Even Client A and C have same source port (`5555`)

## UDP vs TCP Demultiplexing

> [!abstract]- Key Differences
>
> | Aspect | UDP | TCP |
> |--------|-----|-----|
> | **Identifier** | Dest IP + Dest Port | 4-tuple (src IP, src port, dest IP, dest port) |
> | **Sockets per server port** | One socket for all clients | One socket per client connection |
> | **Connection tracking** | None | Full connection state |
> | **Socket creation** | Single socket handles all | New socket for each connection |
> | **Use case** | Simple, stateless services | Complex, stateful connections |

## Related Concepts

> [!note]+ See Also
> - **[[Multiplexing]]**: Complementary operation at sender
> - **[[Socket]]**: Destination of demultiplexed data
> - **[[Transport Layer]]**: Layer that performs demultiplexing
> - **[[UDP]]**: Simple connectionless demultiplexing
> - **[[TCP]]**: Complex connection-oriented demultiplexing
> - **[[Process]]**: Final destination of demultiplexed data

---
title: UDP
authors: Alessandro Dorigo
tags:
  - Network
---


> [!info]+ Definition
> **UDP (User Datagram Protocol)** is a connectionless, unreliable transport protocol that provides a "no-frills" extension of best-effort IP service. It offers minimal overhead for applications that don't need reliability guarantees.

## Characteristics

> [!abstract]- UDP Features
> **Unreliable, unordered delivery**:
> - No delivery guarantees
> - Segments may be lost
> - Segments may arrive out-of-order to application
>
> **Connectionless**:
> - No handshaking between sender and receiver
> - Each UDP segment handled independently
> - No connection state maintained

| ![[2d71d43a6a513a01de38412c4d56d66b.png]] | ![[405646a4ab4eee480b6bfe0a1abc265c.png]] |
| :----------------------------------: | :----------------------------------: |
## Why Use UDP?

> [!success]+ Advantages of UDP
> **No connection establishment**:
> - No [[RTT]] delay for handshaking
> - Faster startup than [[TCP]]
>
> **No connection state**:
> - No state maintained at sender or receiver
> - Server can support more active clients
>
> **Small header size**:
> - Only 8 bytes of overhead
> - More efficient for small messages
>
> **No congestion control**:
> - Can send data at any rate
> - Useful for real-time applications
> - No throttling from network conditions

> [!example]+ Common UDP Applications
> - **Streaming media**: Video/audio streaming (Netflix, YouTube live)
> - **DNS**: Domain name resolution
> - **SNMP**: Network management
> - **Real-time gaming**: Multiplayer games
> - **VoIP**: Voice over IP (Skype, Discord)
> - **IoT devices**: Sensor data transmission

## UDP Segment Structure

> [!note]+ Header Fields
> **Source Port** (16 bits):
> - Port number of sending process
>
> **Destination Port** (16 bits):
> - Port number of receiving process
>
> **Length** (16 bits):
> - Length of UDP segment (header + data) in bytes
> - Minimum value: 8 bytes (header only)
>
> **[[Checksum]]** (16 bits):
> - Error detection for segment
> - Optional in IPv4, mandatory in IPv6

![[7048762c13cdaf01843ebf27ab8ab989.png]]

## Related Concepts

> [!note]+ See Also
> - **[[TCP]]**: Reliable alternative to UDP
> - **[[Checksum]]**: UDP's error detection mechanism
> - **[[Demultiplexing]]**: How UDP delivers to correct socket
> - **[[Socket]]**: Interface for UDP communication
> - **[[Transport Layer]]**: Layer where UDP operates
> - **[[Socket programming]]**: Implementation details

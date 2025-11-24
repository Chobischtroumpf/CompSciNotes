---
title: Socket programming
authors: Alessandro Dorigo
tags:
  - Network
---


> [!info]+ Definition
> **Socket programming** is the practice of building client/server applications that communicate using [[Socket#^d7aa97|sockets]]. Applications can use either UDP or TCP protocols for communication.
## Socket Programming with UDP
> [!abstract]- UDP Socket Characteristics
> **Connectionless Communication**:
> - No connection established between client and server
> - No handshaking before sending data
> - Sender explicitly attaches destination IP address and port number to each packet
> - Receiver extracts sender IP address and port number from received datagram
>
> **Reliability**:
> - Transmitted datagrams may be lost
> - Datagrams may be received out-of-order
> - Application must handle reliability if needed

> [!note]+ UDP Socket Implementation
> **Key Points**:
> - Both client and server processes use the same `DatagramSocket`
> - Destination IP address and port number are explicitly attached to each datagram
> - Source IP address and port number are automatically included
> - Client and server discover each other's addresses when receiving datagrams
>
> ![[2aa62fa9742b333c1fe249262dcfd6dc.png]]
## Socket Programming with TCP
> [!abstract]- TCP Socket Characteristics
> **Connection-Oriented Communication**:
> - Client must contact server before communication
> - Server process must be running and have created a socket
> - Client creates TCP socket specifying server's IP address and port number
> - Server creates new socket for each client connection
>
> **Connection Management**:
> - Allows server to communicate with multiple clients simultaneously
> - Source IP address and port number used to distinguish different clients
> - Each client gets a dedicated socket on the server side

> [!note]+ TCP Socket Implementation
> **Setup Process**:
> 1. Server listens on a well-known port (e.g., port 80 for HTTP)
> 2. Client initiates connection to server's IP and port
> 3. Server accepts connection and creates new socket for that client
> 4. HTTP messages (or other protocol data) are exchanged
> 5. TCP connection is closed when communication is complete
>
> ![[5a956529543326b314ee2a0e63b79f9d.png]]

> [!tip]+ Protocol Comparison
> **When to use UDP**:
> - Real-time applications (video streaming, VoIP)
> - Applications that can tolerate packet loss
> - Minimal overhead needed
>
> **When to use TCP**:
> - Reliable data transfer required
> - File transfers, web browsing, email
> - Order of packets matters

> [!example]+ Common Socket Programming Patterns
> **UDP Pattern**:
> ```
> 1. Create DatagramSocket
> 2. Send/receive datagrams with explicit addressing
> 3. Close socket when done
> ```
>
> **TCP Pattern**:
> ```
> Server:
> 1. Create ServerSocket on port
> 2. Accept incoming connections
> 3. Create new socket for each client
> 4. Exchange data
> 5. Close connection
> ```
>
> ```
> Client:
> 1. Create Socket to server IP:port
> 2. Exchange data
> 3. Close connection
> ```

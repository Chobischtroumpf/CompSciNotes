---
title: Network Layer
authors: Alessandro Dorigo, Mihai Bors
tags:
  - Network
---
> [!info]+ Definition
> The **Network Layer** transports segments from sending to receiving hosts, while the [[Transport Layer]] provides logical communication between processes.

## Sender and Receiver Responsibilities

> [!note]+ Sender Operations
> The network layer at the sender:
> 1. Receives segments from [[TCP]]/[[UDP]] (transport layer)
> 2. Encapsulates segments into packets
> 3. Passes packets to the link layer for transmission

> [!note]+ Receiver Operations
> The network layer at the receiver:
> 1. Receives packets from the link layer
> 2. Extracts the segment from the packet
> 3. Delivers TCP/UDP segments to the transport layer protocol

> [!note]+ Router Operations
> Routers in the network:
> - Examine header fields in all IP packets
> - Move packets from input to output ports
> - Transfer packets along end-to-end path

![[977921fb2d431f5451c1210887311019.png]]

## Network Layer Architecture

> [!abstract]+ Two Planes
> The network layer is divided into two distinct functional planes:
>
> **[[Data Plane]]:**
> - Local, per-router function
> - Determines how packets are forwarded from input to output port
> - Hardware-based, operates in nanosecond time frame
>
> **[[Control Plane]]:**
> - Network-wide logic
> - Determines how packets are routed among routers
> - Software-based, operates in millisecond time frame

> [!tip]+ Protocol Stack Position
> The network layer sits between the transport layer (TCP, UDP) above and the link layer below, with the physical layer at the bottom of the protocol stack.
>
> ![[6afca847778e02e6c93d1b8e79bb0d7a.png]]

## Service Model

> [!abstract]+ Best-Effort Service
>
> | Network Architecture | Service Model | Bandwidth | Loss | Order | Timing |
> |:---:|:---:|:---:|:---:|:---:|:---:|
> | Internet | best effort | none | no | no | no |
>
> **No guarantees on:**
> 1. Successful packet delivery to destination
> 2. Timing or order of delivery
> 3. Bandwidth available to end-to-end flow

## Network Layer Components

> [!info]+ Core Components
> **IP Protocol:**
> - Defines packet format and addressing
> - Specifies packet handling conventions
>
> **ICMP Protocol:**
> - Handles error reporting
> - Provides router signaling
>
> **Routing Protocols:**
> - Path-selection algorithms (OSPF, BGP)
> - [[Forwarding]] done via tables
> - SDN controllers for software-defined networking

## Related Concepts

> [!note]+ See Also
> - **[[Data Plane]]**: Per-router forwarding function
> - **[[Control Plane]]**: Network-wide routing logic
> - **[[IPv4]]**: Current Internet Protocol version
> - **[[IPv6]]**: Next generation Internet Protocol
> - **[[Router Architecture]]**: Internal router structure
> - **[[Forwarding]]**: Moving packets through routers
> - **[[Transport Layer]]**: Layer above network layer

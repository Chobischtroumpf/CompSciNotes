---
title: Control Plane
authors: Alessandro Dorigo, Mihai Bors
tags:
  - Network
---
> [!info]+ Definition
> The **Control Plane** implements *network-wide* logic that determines how packets are routed among routers along the end-to-end path from source to destination hosts. It operates in software at millisecond timescales.

## Control Plane Approaches

> [!abstract]+ Two Main Approaches
> **1. Traditional Routing Algorithms:**
> - Implemented directly in routers
> - Each router runs routing protocols
> - Routers compute forwarding tables independently
> - Distributed decision-making
>
> **2. Software-Defined Networking (SDN):**
> - Implemented in remote servers
> - Centralized controller computes forwarding tables
> - Controller distributes tables to routers
> - Centralized decision-making

### Traditional Routing

> [!note]+ Per-Router Control Plane
> ![[5af56eaef19bf6a2a83d822ac9bba98e.png]]
>
> **Characteristics:**
> - Routing algorithm runs in every router
> - Routers exchange routing messages
> - Each router computes its own forwarding table
> - Examples: OSPF, BGP protocols

### Software-Defined Networking

> [!note]+ Logically Centralized Control Plane
> ![[ce7a796f4ebfc4129e75e55a8fe1db9b.png]]
>
> **Characteristics:**
> - Remote controller interacts with local control agents (CAs)
> - Controller has global network view
> - Computes and installs forwarding tables in routers
> - Separates control logic from forwarding hardware

## Related Concepts

> [!note]+ See Also
> - **[[Data Plane]]**: Per-router forwarding function
> - **[[Network Layer]]**: Layer containing control plane
> - **[[Router Architecture]]**: Complete router structure

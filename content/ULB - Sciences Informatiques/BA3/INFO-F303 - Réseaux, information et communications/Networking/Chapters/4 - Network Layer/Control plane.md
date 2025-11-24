---
title: Control plane
authors: Alessandro Dorigo
tags:
  - Network
---

> [!info]+ Définition
> The **control plane** implements _network-wide_ logic that determines how packets are routed among routers along the end-to-end path from source host to destination host.

### Control-Plane Approaches

> [!abstract]+ Main control-plane approaches:
>
> **Traditional routing algorithms:**
>
> - Implemented directly in routers
> - Each router runs routing protocols to compute forwarding tables
>
> **[[SDN]]:**
>
> - Implemented in remote servers
> - Centralized controller computes and distributes forwarding tables to routers

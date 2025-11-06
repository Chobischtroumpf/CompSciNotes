---
title: Router Architecture
authors: Alessandro Dorigo
tags:
  - Network
---

> [!info]+ What's a Router
>
> A router is a network device that forwards data packets between computer networks. The router architecture consists of two main planes: the control plane and the data plane.

> [!abstract]+ High-Level View of Generic Router Architecture
>
> **Routing processor (control plane):**
>
> - Software-based component
> - Handles routing, management
> - Operates in millisecond time frame
>
> **[[Switching Fabric|High-speed switching fabric]] (data plane):**
>
> - Hardware-based component
> - Handles forwarding
> - Operates in nanosecond time frame
>
> **[[Router input ports]]:**
>
> - Receive incoming packets
> - Connected to switching fabric
>
> **[[Router output ports]]:**
>
> - Send outgoing packets
> - Connected to switching fabric

> [!tip]+ Architecture division
>
> The architecture is divided into two distinct planes:
>
> - **Routing, management control plane** (software): operates in millisecond time frame
> - **Forwarding data plane** (hardware): operates in nanosecond time frame
>
> The routing processor communicates with the high-speed switching fabric, which connects multiple input ports to multiple output ports.

---
title: Switching Fabric
authors: Alessandro Dorigo, Mihai Bors
tags:
  - Network
---
> [!info]+ Definition
> The **switching fabric** is the hardware component of a router that transfers packets from input ports to appropriate output ports. It forms the core of the [[Data Plane]], operating at nanosecond timescales.

## Switching Rate

> [!abstract]+ Performance Metric
> **Switching rate:** Rate at which packets transfer from inputs to outputs
>
> **Ideal performance:**
> $$\text{Switching rate} = N \times \text{line rate}$$
>
> Where $N$ is the number of input ports. This ensures no bottleneck at the fabric.

## Types of Switching Fabrics

> [!note]+ Three Architectures
> ![[ba57d1b103f800b280ab710f3d27c3c0.png]]
>
> | Type | Mechanism | Limitation |
> |------|-----------|------------|
> | Memory | CPU-controlled memory copy | Memory bandwidth |
> | Bus | Shared bus transfer | Bus bandwidth |
> | Crossbar | Direct input-output paths | Scalability |

### Memory-Based Switching

> [!note]+ First Generation Routers
> ![[47ea001e77a7769c7f347213e949ff16.png]]
>
> **Characteristics:**
> - Packet switching under direct CPU control
> - Packet copied to system memory, then to output port
> - Two bus crossings per packet
>
> **Performance limit:**
> $$\text{Switching speed} \leq \frac{\text{Memory bandwidth}}{2}$$

### Bus-Based Switching

> [!note]+ Shared Bus Architecture
> ![[cf5ac4787de7beec68afe4955dd7e87b.png]]
>
> **Characteristics:**
> - Packets transfer directly from input to output memory via shared bus
> - No CPU memory copy required
> - Packet tagged with destination output port address
>
> **Performance limit:**
> $$\text{Switching speed} \leq \text{Bus bandwidth}$$
>
> **Example:** Cisco 5600 with 32 Gbps bus (sufficient for access routers)

### Crossbar Switching

> [!success]+ High-Performance Architecture
> **Crossbar switch:**
> - Provides direct paths between any input-output pair
> - Multiple transfers can occur simultaneously
> - Most scalable architecture
>
> **Multistage switches:**
> - Build $n \times n$ switch from multiple stages of smaller switches
> - Reduces complexity while maintaining parallelism

> [!example]+ Multistage Switch Structure
> ![[c4970ac0a3c617527587a0e011feda24.png]]
>
> An $8 \times 8$ switch can be built from multiple smaller crossbar stages, where the packet tag defines the path through the network.

## Exploiting Parallelism

> [!tip]+ Cell-Based Switching
> **Process:**
> 1. Fragment IP packet into fixed-length cells at entry
> 2. Switch cells through fabric in parallel
> 3. Reassemble IP packet at exit
>
> **Benefits:**
> - Avoids head-of-line blocking for large packets
> - Enables parallel processing through fabric
>
> **Note:** This internal fragmentation is different from [[IP Fragmentation and Reassembly]] — it occurs only within the router.

> [!example]+ Scaling with Multiple Planes
> ![[2f0833eb1e761ea6db04d79568219278.png]]
>
> **Cisco CRS Router:**
> - Basic unit: 8 switching planes operating in parallel
> - Each plane: 3-stage interconnection network
> - Total capacity: up to 100s of Tbps
>
> $$\text{Total capacity} = \text{Number of planes} \times \text{Capacity per plane}$$

## Related Concepts

> [!note]+ See Also
> - **[[Router Architecture]]**: Complete router structure
> - **[[Data Plane]]**: Per-router forwarding function
> - **[[Port Queueing]]**: Buffering at input and output ports
> - **[[Network Layer]]**: Layer where switching occurs

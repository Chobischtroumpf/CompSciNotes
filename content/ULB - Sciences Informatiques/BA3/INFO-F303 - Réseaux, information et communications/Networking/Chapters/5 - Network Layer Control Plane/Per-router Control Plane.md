---
title: Per-router Control Plane
authors: Mihai Bors
tags:
  - Network
---
Individual routing algorithm components in each and every router interact in the control plane

![[Pasted image 20251106151914.png]]

## Routing Algorithm Classification

Global:
- all routers discover the complete topology and all link cost information, then routers compute their own routing tree
- "link state" algorithms

Decentralized:
- iterative process of computation, routers exchange information with neighbors
- routers initially only know link costs to attached neighbors,
- finally, routers know their distances to all other routers (but without knowing the topology per se)
- "distance vector" algorithms

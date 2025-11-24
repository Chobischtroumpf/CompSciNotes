---
title: Network Layer Functions
authors: Alessandro Dorigo
tags:
  - Network
---

# Two key network-layer functions

## Network-Layer Functions

> [!info]+ Definition
> The network layer provides two fundamental functions:
>
> **Forwarding:** The process of moving packets from a router's input link to the appropriate router's output link.
>
> **Routing:** The process of determining the route taken by packets from source to destination. This is accomplished through _routing algorithms_.

## Analogy: Taking a Trip

> [!example]+ Example
> The distinction between forwarding and routing can be understood through a travel analogy:
>
> **Forwarding:** The process of getting through a single interchange (local decision at each intersection)
>
> **Routing:** The process of planning the entire trip from source to destination (global planning of the complete path)
>
> The analogy illustrates that:
>
> - Forwarding is like navigating through individual intersections or highway interchanges
> - Routing is like planning the complete route on a map from your starting point to your final destination

> [!tip]+ Remarque
> While forwarding is a local action performed at each router, routing is a global function that determines the end-to-end path through the network.

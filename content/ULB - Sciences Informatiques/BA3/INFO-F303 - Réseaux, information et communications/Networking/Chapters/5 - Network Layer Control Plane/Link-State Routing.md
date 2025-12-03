---
title: Link-State Routing
authors: Mihai Bors
tags:
  - Network
---
> [!info]+ Definition
> **Link-State Routing** is a routing algorithm where each router builds a complete map of the network topology through flooding of link-state information, then independently computes shortest paths to all destinations using Dijkstra's algorithm.

## Three Phases

> [!abstract]+ Algorithm Overview
> Link-state routing operates in three distinct phases:
>
> | Phase | Description |
> |-------|-------------|
> | 1. Topology Discovery | "Link state broadcast" - all nodes obtain complete topology |
> | 2. Path Computation | Each node computes least-cost paths using Dijkstra's algorithm |
> | 3. Forwarding Table | Each node derives its forwarding table from the spanning tree |

## Phase 1: Graph Topology Discovery

### Building Link State Packets (LSPs)

> [!note]+ LSP Structure
> **Link State Packets contain:**
> - Source node identifier
> - Sequence number
> - Age (time-to-live)
> - Distance vector limited to neighbors only
>
> ![[d5e035370fa54240b2dcfdada1d7ae92.png]]

> [!example]+ LSP Contents Example
>
> | Router | Advertises Neighbors |
> |--------|---------------------|
> | **A** | B (cost 4), E (cost 5), F (cost 1) |
> | **B** | A (cost 4), C (cost 2), E (cost 8) |
> | **C** | B (cost 2), D (cost 3) |
> | **D** | C (cost 3), E (cost 7), F (cost 6) |
> | **E** | A (cost 5), C (cost 1), F (cost 8) |
> | **F** | B (cost 6), D (cost 7), E (cost 8) |
>
> **Field meanings:**
> - **Seq.** (Sequence number): Identifies the version of this LSP (newer = higher number)
> - **Age**: Time-to-live; prevents old LSPs from circulating forever

### Distributing LSPs

> [!success]+ Selective Flooding
> **Flooding rules:**
> - Packets are NOT forwarded on the links they arrived on
> - Duplicate (or older) packets are detected by the sequence number
> - Packets are acknowledged
>
> ![[64bf991d51cd684f308e35825b4d6275.png]]

> [!example]+ LSP Buffer at Router B
> Router B has neighbors **A, C, and F**. The buffer tracks every LSP received:
>
> | Field | Meaning |
> |-------|---------|
> | **Source** | Router that originated the LSP |
> | **Seq** | Sequence number (higher = newer) |
> | **Age** | Time-to-live counter |
> | **Send flags** | "Do I still need to forward this to neighbor X?" (1=yes) |
> | **ACK flags** | "Has neighbor X acknowledged receiving this?" (1=yes) |
> | **Data** | The actual link-state information |
>
> **Example row for LSP from D:**
>
> | Source | Seq | Age | Send A | Send C | Send F | ACK A | ACK C | ACK F |
> |--------|-----|-----|--------|--------|--------|-------|-------|-------|
> | D | 21 | 59 | 1 | 0 | 0 | 0 | 1 | 1 |
>
> - **Send flags**: B needs to forward to **A** (=1), but NOT to C or F (=0) because that's where it came from
> - **ACK flags**: C and F already acknowledged (=1), A hasn't yet (=0)

### Potential Problems

> [!warning]+ Sequence Number Wrap-Around
> **Problem:** What if the sequence number wraps around?
>
> **Solution:** Use 32-bit sequence number
> - Needs 137 years to wrap around at one LSP per second
> - In practice, LSPs sent every ~10 seconds

> [!warning]+ Router Crash Recovery
> **Problem:** Router restarts with sequence number 0, packets ignored until reaching previous value
>
> **Solution:** Age field
> - Decremented by 1 every second
> - Entry removed when age hits 0
> - Also handles corrupted sequence numbers

### Message Complexity

> [!note]+ Complexity Analysis
> For $n$ nodes and $l$ links (with $l \geq n - 1$):
>
> | Operation | Complexity |
> |-----------|------------|
> | Broadcast from one source | $\mathcal{O}(l)$ link crossings |
> | Each router's message | $\mathcal{O}(l)$ links |
> | **Overall message complexity** | $\mathcal{O}(nl)$ |

## Phase 2: Shortest Path Calculation

> [!abstract]+ Dijkstra's Algorithm
> Each router computes least-cost paths from itself ("source") to all other routers:
> - Uses Dijkstra's algorithm
> - Produces one spanning tree per "source" router
>
> **Time complexity:**
>
> | Implementation | Per Router | Whole Network |
> |----------------|------------|---------------|
> | Efficient | $\mathcal{O}(l \log n)$ | $\mathcal{O}(nl \log n)$ |
>
> ![[b43ef5f7ba387f4722f806aac5432232.png]]
>
> *Top: Network topology. Bottom: Least-cost-path tree from node $u$*

## Phase 3: Forwarding Table Derivation

> [!success]+ Building the Forwarding Table
> Using the least-cost-path tree from $u$:
>
> | Destination | Next Hop | Outgoing Link |
> |-------------|----------|---------------|
> | v | v | 1 |
> | x | x | 2 |
> | y | x | 2 |
> | w | x | 2 |
> | z | x | 2 |
>
> **Interpretation:**
> - First row: direct route from $u$ to $v$
> - Other rows: routes from $u$ via $x$ to all other destinations

> [!tip]+ Practical Considerations
> - Router IDs (v, x, y, ...) are IP addresses (e.g., router loopback address)
> - Nodes also have attached [[Subnet|subnets]], whose IP prefixes:
>   - Must be carried in link state packets
>   - Must be added in forwarding tables as additional destinations

## Related Concepts

> [!note]+ See Also
> - **[[Link Cost]]**: Metrics used in path computation
> - **[[Optimality Principle]]**: Foundation for shortest-path algorithms
> - **[[Per-router Control Plane]]**: Distributed routing architecture
> - **[[Control Plane]]**: Network-wide routing logic
> - **[[Forwarding]]**: Using the computed tables
> - **[[Network Layer]]**: Layer where link-state routing operates

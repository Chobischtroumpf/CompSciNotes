---
title: Peer-to-peer paradigm
authors: Alessandro Dorigo
tags:
  - Network
---


> [!info]+ Definition
> The **peer-to-peer (P2P) paradigm** is a distributed application architecture where peers (end systems) communicate directly with each other without relying on a centralized always-on server.

^08944a

> [!abstract]- Core Characteristics
> **No Always-On Server**:
> - No centralized server required to be running continuously
> - Reduces infrastructure costs and single points of failure
>
> **Direct Peer Communication**:
> - Arbitrary end systems communicate directly with each other
> - Each peer can act as both client and server
>
> **Service Exchange**:
> - Peers request services from other peers
> - Peers provide services to other peers in return
> - New peers bring new service capacity but also new demands
>
> **Dynamic Nature**:
> - Peers are intermittently connected
> - Peers frequently change IP addresses
> - Network topology changes constantly

> [!note]+ Advantages of P2P
> **Scalability**:
> - Self-scaling: each new peer adds capacity
> - No bottleneck at centralized server
>
> **Cost Efficiency**:
> - No expensive server infrastructure needed
> - Distributes bandwidth and storage costs
>
> **Resilience**:
> - No single point of failure
> - System continues functioning even if peers leave

> [!warning]+ Challenges of P2P
> - **Complexity**: More difficult to manage and coordinate
> - **Security**: Harder to implement security measures
> - **Inconsistent availability**: Peers may not always be online
> - **Variable performance**: Depends on peer capabilities
## P2P Architecture
![[0c2143df5fcc0816231ecdcbbb924ef3.png]]
## Hybrid P2P Paradigms
- Many applications use hybrid approaches that combine P2P communication with centralized coordination.

> [!example]+ Skype (Voice-over-IP)
> **Architecture**:
> - **Centralized server**: Finds addresses and establishes connection between two peers
> - **P2P connection**: Direct voice communication between clients (not through server)
>
> **Benefits**:
> - Server handles complex NAT traversal and peer discovery
> - Direct P2P connection reduces latency for voice data

> [!example]+ Instant Messaging
> **Architecture**:
> - **Centralized service**: Client presence detection and location
> - **P2P communication**: Actual chatting done directly between peers
>
> **Benefits**:
> - Server maintains user availability and contact lists
> - Messages flow directly between users for privacy and speed

> [!example]+ BitTorrent (File Sharing)
> **Architecture**:
> - **Tracker (centralized)**: Maintains list of peers participating in the torrent
> - **P2P file exchange**: File chunks exchanged directly between peers
>
> **Benefits**:
> - Tracker coordinates which peers have which pieces
> - Actual data transfer distributed across all peers
> - Incredibly efficient for large file distribution
## Related Concepts
> [!note]+ See Also
> - Compare with [[Client-server paradigm]]
> - Uses [[Process#^6a45eb|processes]] and [[Socket#^d7aa97|sockets]] for communication
> - Requires [[Application layer protocol|protocols]] for coordination

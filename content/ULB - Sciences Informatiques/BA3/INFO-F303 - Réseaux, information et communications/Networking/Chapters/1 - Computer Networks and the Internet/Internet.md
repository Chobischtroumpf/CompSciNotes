---
title: Internet
authors: Alessandro Dorigo
tags:
  - Network
---


> [!info]+ Definition
> The **Internet** is a [[Network#^89dac9|network]] of networks - interconnected ISPs (Internet Service Providers) that must be interconnected so that any two [[Host#^019621|hosts]] can send [[Packet#^150f99|packets]] to one another.

^c8a6b5

> [!note]+ Two Views of the Internet
> **"Nuts and bolts" view:**
> - Billions of connected computing devices ([[Host#^019621|hosts]] = end systems)
> - [[Switch#^97dbe2|Packet switches]] that forward packets (routers, switches)
> - [[Communication link#^b83bd9|Communication links]] (fiber, copper, radio, satellite)
> - [[Network#^89dac9|Networks]]: collection of devices, routers, links managed by organizations
>
> ![[Pasted image 20250918144145.png]]
>
> **"Service" view:**
> - Infrastructure that provides services to applications (Web, streaming, multimedia, teleconferencing, email, games, e-commerce, social media, interconnected appliances)
> - Provides programming interface to distributed applications: "hooks" allowing sending/receiving apps to connect to, use Internet transport services
>
> ![[Pasted image 20250918144412.png]]

> [!abstract]- Internet Standards
> - **RFC (Request for Comments)**: Documents defining Internet standards
> - **IETF (Internet Engineering Task Force)**: Organization developing Internet standards
> - **[[Protocol#^4bfd4c|Protocols]]**: Rules governing communication (HTTP, TCP, IP, WiFi, 4G, Ethernet)

Provides programming interfaces to distributed applications:
- Hooks allowing sending/receiving apps to connect to, use Internet transport services

## The Big Question: ISP Interconnection
Given millions of access ISPs, how to connect them together?

|               ![[Pasted image 20250918151601.png]]               |              ![[Pasted image 20250918151748.png]]               |                                  ![[Pasted image 20250918151758.png]]                                   |
| :--------------------------------------------------------------: | :-------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------: |
|     **Direct connection**: O(N²) connections - doesn't scale     | **Single global ISP**: Customer-provider economic relationships |                      **Competing ISPs**: Multiple global ISPs need interconnection                      |
|               ![[Pasted image 20250918151805.png]]               |              ![[Pasted image 20250918151812.png]]               |                                  ![[Pasted image 20250918151821.png]]                                   |
| **Internet Exchange Points (IXPs)**: Peering points between ISPs |    **Regional ISPs**: Connect access networks to global ISPs    | **Content provider networks**: Private networks (Google, Microsoft) bypassing traditional ISP hierarchy |
## Current Internet Structure
> [!abstract]- Hierarchical Structure
>
> ![[Pasted image 20250918151855.png]]
>
> **At center**: Small number of well-connected large [[Network#^89dac9|networks]]
> - **Tier-1 ISPs**: Commercial ISPs (Sprint, AT&T, Orange, Deutsche Telekom) with national/international coverage
> - **Content provider networks**: Private networks (Google) connecting data centers to Internet, often bypassing tier-1/regional ISPs, but without accepting transit traffic

![[Pasted image 20250918152615.png]]

---
title: Internet
authors: Alessandro Dorigo, Mihai Bors
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
> ![[7e6e165dc5c7c3f00a0fc82051aebebe.png]]
>
> **"Service" view:**
> - Infrastructure that provides services to applications (Web, streaming, multimedia, teleconferencing, email, games, e-commerce, social media, interconnected appliances)
> - Provides programming interface to distributed applications: "hooks" allowing sending/receiving apps to connect to, use Internet transport services
>
> ![[c7db63712e6476b6d405e8b97e8c238e.png]]

> [!abstract]- Internet Standards
> - **RFC (Request for Comments)**: Documents defining Internet standards
> - **IETF (Internet Engineering Task Force)**: Organization developing Internet standards
> - **[[Protocol#^4bfd4c|Protocols]]**: Rules governing communication (HTTP, TCP, IP, WiFi, 4G, Ethernet)

Provides programming interfaces to distributed applications:
- Hooks allowing sending/receiving apps to connect to, use Internet transport services

## The Big Question: ISP Interconnection
Given millions of access ISPs, how to connect them together?

|               ![[ae239a1cc0958a2e966a37dd1e0e2862.png]]               |              ![[01b2bc626e1ca4c1076bc675bc7db7a3.png]]               |                                  ![[0ba11e1f2ab47525ed3d97a8b2059929.png]]                                   |
| :--------------------------------------------------------------: | :-------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------: |
|     **Direct connection**: O(N²) connections - doesn't scale     | **Single global ISP**: Customer-provider economic relationships |                      **Competing ISPs**: Multiple global ISPs need interconnection                      |
|               ![[92be16105b6c64e920b17ae9e3251c1f.png]]               |              ![[8e766c16ba2d0f215b15eea115e14b59.png]]               |                                  ![[161dcc81fdc6e7871239f593161bbac9.png]]                                   |
| **Internet Exchange Points (IXPs)**: Peering points between ISPs |    **Regional ISPs**: Connect access networks to global ISPs    | **Content provider networks**: Private networks (Google, Microsoft) bypassing traditional ISP hierarchy |
## Current Internet Structure

> [!abstract]- Hierarchical Structure
>
> ![[7f0e834b6955054e508d96d94fde16e3.png]]
>
> **At center**: Small number of well-connected large [[Network#^89dac9|networks]]
> - **Tier-1 ISPs**: Commercial ISPs (Sprint, AT&T, Orange, Deutsche Telekom) with national/international coverage
> - **Content provider networks**: Private networks (Google) connecting data centers to Internet, often bypassing tier-1/regional ISPs, but without accepting transit traffic

![[49d8b4506c1c6a2cab080947e86f5090.png]]

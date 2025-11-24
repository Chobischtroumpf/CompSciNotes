---
title: Link Cost
authors: Mihai Bors
tags:
  - Network
---
![[393610f72a8ea9dcd5632149095b8d33.png]]
Graph Abstraction

- we keep infinite to say that there is no link

## Settings

- Hop counts (all link costs equal to 1)
- InvCap: link cost is inversely proportional to the link capacity (in bps)
	- Thus high capacity links attract more traffic (smaller cost)
	- This minimizes average link utilization (= fraction of link capacity used by traffic)
- Delay (e.g. static propagation delay)
- Administrative link cost
	- Any link cost computed so as to optimise a given network score
	- For example to better balance the network load given a traffic matrix
- Basically link costs can be any summable quantity
	- Summable means “it makes sense to express the cost of a path as the sum of all the link costs along this path”
	- Examples of non summable costs: packet error rate on link, link capacity

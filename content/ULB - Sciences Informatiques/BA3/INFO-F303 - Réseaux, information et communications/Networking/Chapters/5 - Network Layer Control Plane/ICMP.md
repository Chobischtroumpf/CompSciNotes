---
title: ICMP
authors: Mihai Bors
tags:
  - Network
---
Internet Control Message Protocol

used by hosts and routers to communicate network-level information
- error reporting: unreachable host, network, port, protocol
- echo request/reply (used by ping )

network-layer “above” IP:
- ICMP messages carried in IP packets

ICMP message: type, code plus first 8 bytes of IP packet causing error

![[Pasted image 20251106150543.png]]
Different ICMP message types/codes and descriptions

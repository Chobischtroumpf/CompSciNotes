---
title: NAT
authors: Alessandro Dorigo, Mihai Bors
tags:
  - Network
---
> [!info]+ Definition
> **NAT (Network Address Translation)** is a technique that allows all devices in a local network to share a single public IP address. All outgoing packets have the same source NAT IP address (but different source port numbers), while incoming packets are translated back to private `10.0.0.0/24` addresses.

## Why Use NAT?

> [!success]+ Advantages
> **Address conservation:**
> - Only one IP address needed from ISP for all devices
> - Addresses private network exhaustion problem
>
> **Flexibility:**
> - Can change addresses of hosts in local network without notifying outside world
> - Can change ISP without changing addresses of devices in local network
>
> **Security:**
> - Devices inside local network not directly addressable
> - Not visible by outside world

## How NAT Works

> [!abstract]+ Translation Process
> ![[49dd31fc6943592c75dcee49141e0537.png]]
>
> **Outgoing packets:**
> - Replace source IP address and port # with NAT IP address and new port #
> - Remote clients/servers respond using NAT IP address as destination
>
> **NAT translation table:**
> - Remembers every (source IP, port #) → (NAT IP, new port #) mapping
>
> **Incoming packets:**
> - Replace NAT IP address and new port # in destination fields
> - Use corresponding source IP and port # from NAT table

> [!example]+ NAT Translation Example
> ![[c2fdd32a619581ef58ff163644cb7e4d.png]]
>
> **Step-by-step process:**
> 1. Host `10.0.0.1` sends packet to `128.119.40.186:80`
> 2. NAT router changes source from `10.0.0.1:3345` to `138.76.29.7:5001`, updates table
> 3. Reply arrives with destination `138.76.29.7:5001`
> 4. NAT router changes destination from `138.76.29.7:5001` to `10.0.0.1:3345`

## NAT Traversal Problem

> [!warning]+ The Problem
> **Scenario:** A client wants to connect to a server with address `10.0.0.1`
>
> **Issues:**
> - Server address `10.0.0.1` is local to LAN
> - Client can't use it as destination address
> - Only one externally visible NATed address exists: `138.76.29.7`

### Solutions

> [!info]+ Solution 1: Static Configuration
> Statically configure NAT to forward incoming connection requests at given port to server.
>
> **Example:** `138.76.29.7:2500` always forwarded to `10.0.0.1:25000`

> [!info]+ Solution 2: Universal Plug and Play (UPnP)
> ![[5b4ef4f4464009b4ae63610520c0e9f4.png]]
>
> **Allows NATed host to:**
> - Learn public IP address (`138.76.29.7`)
> - Add/remove port mappings (with lease times)
>
> Automates static NAT port map configuration.

> [!info]+ Solution 3: Relaying
> ![[bfe4fd0b845ee26e4ba603113884b16e.png]]
>
> **Process:**
> 1. NATed server establishes connection to relay
> 2. External client connects to relay
> 3. Relay bridges packets between two connections

## Related Concepts

> [!note]+ See Also
> - **[[IPv4]]**: IP addressing fundamentals
> - **[[Subnet]]**: Private network addressing
> - **[[DHCP]]**: Often used with NAT for private networks
> - **[[Network Layer]]**: Layer where NAT operates

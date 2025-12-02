---
title: IPv4
authors: Alessandro Dorigo, Mihai Bors
tags:
  - Network
---
> [!info]+ Definition
> **IPv4 (Internet Protocol version 4)** uses 32-bit addresses to identify hosts and routers on the Internet. Each IP address is associated with a host or router interface, where an interface represents the connection between a device and a physical link.

## IP Address Format

> [!abstract]+ Address Notation
> **32-bit identifier written in dotted-decimal notation:**
>
> ```
> 223.1.1.1 = 11011111.00000001.00000001.00000001
> ```
>
> **Each octet:**
> - Represents 8 bits (1 byte)
> - Range: 0-255 in decimal
> - Separated by dots

## Address Structure

> [!note]+ Hierarchical Structure
> IP addresses have a hierarchical structure composed of two parts:
>
> **Subnet part (address prefix):**
> - High-order bits of the IP address
> - Devices in the same [[Subnet]] share common high-order bits
> - Identifies the network portion
>
> **Host part:**
> - Remaining low-order bits
> - Uniquely identifies individual devices within the subnet
> - Distinguishes different hosts on the same network
>
> ```
> |←── Subnet part ──→|←── Host part ──→|
> |   (high-order)    |   (low-order)   |
> ```

- Most details found at [[IPv4 Structure]]

## Interfaces

> [!info]+ What is an Interface?
> **Interface:** Connection between host/router and physical link
>
> **Characteristics:**
> - Routers typically have multiple interfaces
> - Hosts typically have one or two interfaces (Ethernet, WiFi)
> - Each interface has its own IP address
>
> ![[9a6fa82268cb12ca1fe30bc060c4c9a3.png]]
>
> *Small network of 7 hosts (3 subnets) connected via a single router*

## Address Assignment

> [!abstract]+ How Devices Get IP Addresses
> **Two methods:**
>
> **1. Static Configuration:**
> - Hard-coded by system administrator
> - Configured in system files (e.g., `/etc/rc.config`)
> - Permanent address assignment
>
> **2. Dynamic Configuration ([[DHCP]]):**
> - Automatically assigned when joining network
> - Addresses can be reused
> - Supports mobile users

## Related Concepts

> [!note]+ See Also
> - **[[Subnet]]**: Network subdivision using IP prefixes
> - **[[CIDR]]**: Classless addressing scheme
> - **[[DHCP]]**: Dynamic address assignment protocol
> - **[[IPv6]]**: Next generation IP with 128-bit addresses
> - **[[NAT]]**: Address translation for private networks
> - **[[IPv4 Structure]]**: Structure of IP packets
> - **[[Network Layer]]**: Layer where IPv4 operates

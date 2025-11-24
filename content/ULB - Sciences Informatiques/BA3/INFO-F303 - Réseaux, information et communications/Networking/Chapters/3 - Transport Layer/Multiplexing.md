---
title: Multiplexing
authors: Alessandro Dorigo
tags:
  - Network
---


> [!info]+ Definition
> **Multiplexing** is the process used by the sender to handle data from multiple sockets, adding transport headers (including information used for [[Demultiplexing]]) before passing segments to the network layer.

## How Multiplexing Works

> [!abstract]- Sender-Side Process
> **At the transport layer, the sender**:
> 1. Receives messages from multiple application processes
> 2. Each process sends through its own socket
> 3. Transport layer adds header to each message
> 4. Header contains source and destination information
> 5. Segments passed down to network layer
>
> ![[d4bdab9b68ea6210fc14dc69e3bfe31e.png]]

## Multiplexing in Action

> [!example]+ Example Scenario
> **Multiple applications on same host**:
> - Web browser connecting to multiple sites
> - Email client checking mail
> - Streaming video application
> - File transfer in progress
>
> **Multiplexing process**:
> 1. Each application writes to its socket
> 2. Transport layer creates segment for each
> 3. Adds unique source port for each application
> 4. Adds destination IP and port from application
> 5. All segments pass through same network interface
>
> **Result**:
> - Multiple data streams share one network connection
> - Each identified by unique port combination
> - Receiving host can demultiplex back to correct processes

## Related Concepts

> [!note]+ See Also
> - **[[Demultiplexing]]**: Complementary operation at receiver
> - **[[Socket]]**: Interface where multiplexing occurs
> - **[[Transport Layer]]**: Layer that performs multiplexing
> - **[[UDP]]**: Simple multiplexing/demultiplexing
> - **[[TCP]]**: More complex multiplexing with connections
> - **[[Process]]**: Source of data being multiplexed

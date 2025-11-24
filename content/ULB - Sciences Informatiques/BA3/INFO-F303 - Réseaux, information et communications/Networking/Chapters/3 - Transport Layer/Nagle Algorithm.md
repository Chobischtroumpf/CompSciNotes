---
title: Nagle Algorithm
authors: Alessandro Dorigo
tags:
  - Network
---


> [!info]+ Definition
> The **Nagle Algorithm** is a [[TCP]] optimization that prevents sending many small segments when the application provides data in small units (e.g., one byte at a time). It reduces network overhead by buffering small amounts of data until conditions are met for efficient transmission.

## The Problem

> [!warning]+ Small Packet Overhead
> **When TCP receives data one byte at a time**:
> - Without optimization: 41-byte segments (1 byte data + 40 bytes TCP/IP header)
> - Massive overhead: 40 bytes header for 1 byte payload
> - Network congestion from excessive small packets
> - Inefficient bandwidth usage

## How Nagle Algorithm Works

> [!success]+ Buffering Strategy
> **Rules**:
> 1. Send first small packet immediately
> 2. Buffer all subsequent data until outstanding bytes are ACKed
> 3. Send buffered data when:
>    - All previous bytes are ACKed, OR
>    - MSS (Maximum Segment Size) bytes have been buffered, OR
>    - Previous segment was full size
>
> ![[0933c564e65c5fd81fb895592e222a40.png]]

## Use Cases

> [!example]+ Common Applications
> **Telnet**:
> - User types characters one at a time
> - Nagle prevents sending each keystroke immediately
> - Groups characters into reasonable-sized segments
>
> **Interactive applications**:
> - Terminal sessions
> - Command-line interfaces
> - Text-based protocols

## Disabling Nagle

> [!note]+ TCP_NoDelay Option
> **When to disable**:
> - Real-time applications requiring immediate transmission
> - Low-latency requirements more important than efficiency
>
> **How to disable**:
> - Socket option: `TCP_NoDelay`
> - Sets TCP to send data immediately regardless of size

## Related Concepts

> [!note]+ See Also
> - **[[TCP]]**: Transport protocol using Nagle
> - **[[TCP Structure]]**: Segment format and overhead
> - **[[Silly Window Syndrome]]**: Related efficiency problem
> - **[[Socket]]**: Interface for TCP_NoDelay option

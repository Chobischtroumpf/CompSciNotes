---
title: TCP Flow Control
authors: Alessandro Dorigo
tags:
  - Network
---


> [!info]+ Definition
> **TCP Flow Control** is a mechanism where the receiver controls the sender's transmission rate to prevent the sender from overwhelming the receiver's buffer by transmitting too much data too quickly.

## The Problem

> [!warning]+ Buffer Overflow Risk
> **Without flow control**:
> - Sender might transmit data faster than receiver can process
> - Receiver's buffer could overflow
> - Data would be lost
> - Connection reliability compromised
>
> **Solution**: Receiver tells sender how much free buffer space is available

## How TCP Flow Control Works

> [!success]+ Receiver-Controlled Flow
> **Receiver advertises free buffer space**:
> - Uses `rwnd` (receive window) field in [[TCP Structure|TCP header]]
> - Indicates number of bytes receiver can accept
> - Dynamically updated in each ACK
>
> **Sender limits transmission**:
> - Keeps track of unACKed ("in-flight") data
> - Ensures `unACKed_data ≤ rwnd`
> - Prevents receiver buffer overflow

## Receive Buffer

> [!note]+ Receiver-Side Buffering
> ![[Pasted image 20251102115312.png]]
>
> **Buffer components**:
> - **Occupied space**: Data received but not yet read by application
> - **Free space**: Available for new incoming data
> - Total size: `RcvBuffer`
>
> **Buffer management**:
> ```
> rwnd = RcvBuffer - [bytes in buffer not yet read by application]
> ```

> [!abstract]+ Receiver Protocol Stack
> ![[Pasted image 20251102115139.png]]

## Related Concepts

> [!note]+ See Also
> - **[[TCP]]**: Main protocol overview
> - **[[TCP Structure]]**: Header fields including window
> - **[[Reliable Data Transfer]]**: Overall reliability mechanisms
> - **[[Transport Layer]]**: Layer where flow control operates
> - **[[RTT]]**: Affects buffer size requirements
> - **[[Socket]]**: Buffer configuration interface

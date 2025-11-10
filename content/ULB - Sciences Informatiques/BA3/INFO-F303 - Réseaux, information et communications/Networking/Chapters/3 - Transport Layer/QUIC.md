---
title: QUIC
authors: Alessandro Dorigo
tags:
  - Network
---


> [!info]+ Definition
> **QUIC (Quick UDP Internet Connections)** is an application-layer protocol built on top of [[UDP]] designed to increase performance of [[HTTP]]. QUIC combines connection establishment, reliability, congestion control, authentication, and encryption in a single handshake.

## Core Characteristics

> [!success]+ Key Features
> **Built on UDP**:
> - Application-layer protocol
> - Avoids TCP head-of-line blocking
> - Deployed on many Google servers and apps (Chrome, mobile YouTube)
>
> **Fast connection establishment**:
> - Reliability, congestion control, authentication, encryption established in one [[RTT]]
> - Combines TCP + TLS handshake into single step
>
> **Stream multiplexing**:
> - Multiple application-level "streams" over single QUIC connection
> - Per-stream reliable data transfer and security
> - Shared congestion control across streams

> [!warning]+ Implementation Challenges
> User-space nature introduces unique challenges:
> - Coarse-grained timers
> - System call overhead
> - OS scheduling delays

## Protocol Comparison

> [!abstract]+ HTTP/2 over TCP vs QUIC
> ![[86cc76f5cf87b46daf8ce0a6c6dccbd9.png]]
>
> **HTTP/2 over TCP (with TLS)**:
> - Application layer comprised of HTTP/2 + TLS
> - Transport layer is TCP
>
> **HTTP/2 over QUIC over UDP**:
> - Application layer is HTTP/2 + QUIC (HTTP/3)
> - Transport layer is UDP

## Connection Establishment

> [!success]+ One RTT Handshake
> ![[6104363b1dc74565edde1db94a49b10d.png]]
>
> **TCP + TLS approach**:
> - TCP 3-way handshake (1 RTT)
> - TLS handshake (1-2 RTT)
> - Total: 2-3 RTT before data transfer
>
> **QUIC approach**:
> - Single handshake (1 RTT)
> - Establishes connection, security, and congestion control
> - Immediate data transfer possible

## Protocol Stack

> [!abstract]+ HTTP/3 Architecture
> ![[9d8192cb27b6082ee1e21c2273d7de61.png]]
>
> **Traditional stack (HTTP/1.1, HTTP/2)**:
> - HTTP over TCP with TLS
> - TCP provides reliability and congestion control
>
> **Modern stack (HTTP/3)**:
> - HTTP/2 semantics over QUIC over UDP
> - QUIC provides reliability and congestion control
> - Better stream multiplexing

## Error and Congestion Control

> [!note]+ TCP-Inspired Algorithms
> **From QUIC specification**:
> "Readers familiar with TCP's loss detection and congestion control will find algorithms here that parallel well-known TCP ones"
>
> **Features**:
> - Loss detection similar to TCP
> - Congestion control algorithms adapted from TCP
> - Per-stream reliability
> - Aggregate congestion control

## Related Concepts

> [!note]+ See Also
> - **[[UDP]]**: Transport protocol QUIC is built on
> - **[[TCP]]**: Protocol QUIC improves upon
> - **[[HTTP 2]]**: HTTP version used with QUIC
> - **[[HTTP 1.1]]**: Previous HTTP version
> - **[[RTT]]**: Connection establishment time metric
> - **[[Transport Layer]]**: Layer where QUIC operates
> - **[[3-way-handshake]]**: TCP approach QUIC improves on

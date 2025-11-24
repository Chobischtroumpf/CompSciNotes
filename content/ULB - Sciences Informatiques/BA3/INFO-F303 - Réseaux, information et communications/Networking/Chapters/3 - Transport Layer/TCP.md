---
title: TCP
authors: Alessandro Dorigo
tags:
  - Network
---


> [!info]+ Definition
> **TCP (Transmission Control Protocol)** is a connection-oriented, reliable transport protocol that provides ordered, error-checked delivery of data between applications running on hosts. TCP guarantees all data arrives correctly and in the order it was sent.

## Core Characteristics

> [!success]+ TCP Features
> **Reliable, in-order delivery**:
> - Guarantees all data arrives correctly
> - Data delivered in the order it was sent
> - Retransmits lost or corrupted segments
>
> **Connection-oriented**:
> - Requires connection setup before data transfer
> - Maintains connection state at sender and receiver
> - Three-way handshake to establish connection
>
> **Flow control**:
> - Prevents sender from overwhelming receiver
> - Receiver advertises available buffer space (see [[TCP Flow Control]])
>
> **Congestion control**:
> - Prevents sender from overwhelming network
> - Adjusts sending rate based on network conditions

> [!example]+ Common TCP Applications
> - **HTTP/HTTPS**: Web browsing
> - **FTP**: File transfer
> - **SMTP**: Email transmission
> - **SSH**: Secure remote access
> - **Telnet**: Remote terminal access

## TCP Segment Structure

> [!note]+ Header Overview
> TCP segment consists of:
> - **Header**: 20 bytes minimum (up to 60 bytes with options)
> - **Data**: Variable length payload
>
> ![[8484e72e2a76e93eafa1e184dc5f6850.png]]
>
> See [[TCP Structure]] for complete header field details.

## Sequence and Acknowledgment Numbers

> [!info]+ Sequence Numbers
> **Byte stream "number" of first byte in segment's data**
>
> **Key points**:
> - TCP views data as stream of bytes
> - Each byte has a sequence number
> - Segment's sequence number = number of first data byte
> - Initial sequence number (ISN) chosen randomly during handshake
>
> ![[15c0a489bb54e4507db760f1a367daf6.png]]

> [!info]+ Acknowledgment Numbers
> **Sequence number of next byte expected from other side**
>
> **Cumulative acknowledgments**:
> - ACK($n$) means "I've received all bytes up to $n - 1$"
> - Requesting byte $n$ next

> [!example]+ Simple Telnet Scenario
> ![[8c0e4e1460009693037a0133f1abab7a.png]]
>
> **Sequence**:
> 1. Client sends "C" (seq=42, 1 byte)
> 2. Server ACKs with ACK=43 (expecting byte 43)
> 3. Server echoes "C" back (seq=79, 1 byte)
> 4. Client ACKs with ACK=80 (expecting byte 80)

## TCP Sender

> [!note]+ Sender Events and Actions
> **Data received from application**:
> - Create segment with sequence number
> - Sequence number = byte-stream number of first data byte
> - Start timer if not already running
> - Timer is for oldest unACKed segment
> - Expiration interval: `TimeOutInterval`
>
> **Timeout**:
> - Retransmit segment that caused timeout
> - Restart timer
>
> **ACK received**:
> - If ACK acknowledges previously unACKed segments:
>   - Update what is known to be ACKed
>   - Start timer if there are still unACKed segments

> [!abstract]+ Sender FSM
> ![[2b2203fef59c6ba01497a795d41dbadc.png]]
>
> **States**:
> - Single state with three events
> - Handles data from above, timeout, and ACK receipt

## Retransmission Scenarios

> [!example]+ Lost ACK Scenario
> ![[714c7e603978cf7e80359942074d9de6.png]]
>
> **What happens**:
> 1. Segment sent with seq=92, 8 bytes
> 2. ACK=100 sent back but lost
> 3. Timeout occurs at sender
> 4. Sender retransmits seq=92
> 5. Receiver discards duplicate, resends ACK=100

> [!example]+ Premature Timeout
> ![[60f93ad211b551de5aab082833c49948.png]]
>
> **What happens**:
> 1. Sender transmits seq=92, 8 bytes
> 2. Sender transmits seq=100, 20 bytes
> 3. Receiver sends ACK=100
> 4. Receiver sends ACK=120
> 5. **Timeout occurs** before ACK=100 arrives at sender
> 6. Sender retransmits seq=92
> 7. ACK=100 finally arrives at sender
> 8. ACK=120 arrives at sender (sender now knows all bytes received)
> 9. Duplicate seq=92 arrives at receiver
> 10. Receiver sends cumulative ACK=120 (already has all data)

> [!example]+ Cumulative ACK
> ![[c49ea22235b40ab25e8f4a6d8440db4f.png]]
>
> **What happens**:
> 1. Sender transmits seq=92, 8 bytes
> 2. Sender transmits seq=100, 20 bytes
> 3. Receiver sends ACK=100
> 4. **ACK=100 is lost**
> 5. Receiver sends ACK=120 (cumulative ACK for all received data)
> 6. Sender receives ACK=120 (knows bytes 92-119 all received)
> 7. Sender transmits seq=120 (next segment)
> 8. **No retransmission needed** - cumulative ACK covered both segments

## TCP Receiver

> [!note]+ Receiver ACK Generation
>
> | Event | TCP Receiver Action |
> |-------|-------------------|
> | Arrival of in-order segment with expected seq #. All data up to expected seq # already ACKed | **Delayed ACK**. Wait up to 500ms for next segment. If no next segment, send ACK |
> | Arrival of in-order segment with expected seq #. One other segment has ACK pending | **Immediate ACK**. Send single cumulative ACK, ACKing both segments |
> | Arrival of out-of-order segment with higher-than-expected seq # (gap detected) | **Immediate duplicate ACK**. Indicate seq # of next expected byte |
> | Arrival of segment that partially or completely fills gap | **Immediate ACK**. Provided segment starts at lower end of gap |

> [!tip]+ Delayed ACK Strategy
> **Purpose**: Reduce ACK overhead
> - Wait briefly (typically 200ms, max 500ms) for next segment
> - If another segment arrives, send one ACK for both
> - If timer expires, send ACK anyway
> - Reduces ACK traffic by ~50%

## TCP Fast Retransmit

> [!info]+ Fast Retransmit Mechanism
> **If sender receives 3 additional ACKs for same data ("triple duplicate ACKs"), resend unACKed segment with smallest sequence number**
>
> **Rationale**:
> - Receipt of three duplicate ACKs indicates 3 segments received after a missing segment
> - Lost segment is likely
> - Don't wait for timeout - retransmit immediately
>
> ![[665c2a8e4db23c3fbc55415404016ea4.png]]
>
> **Advantages**:
> - Faster recovery than waiting for timeout
> - Reduces retransmission delay
> - Improves throughput

> [!tip]+ Why Three Duplicate ACKs?
> - One or two duplicates might be due to reordering
> - Three duplicates strongly indicate loss
> - Balances between premature retransmission and delay

## Error Recovery Comparison

> [!abstract]+ TCP vs GBN vs SR
> **Like [[Go-Back-N]]**:
> - TCP has cumulative ACKs
> - TCP has single retransmission timer
>
> **Like [[Selective Repeat]]**:
> - TCP has receiver buffer (buffers out-of-order segments)
> - TCP only retransmits oldest unACKed packet on timeout
> - TCP has SACK (Selective ACK) option
>
> **TCP's unique features**:
> - Fast retransmit mechanism (3 duplicate ACKs)
> - Delayed ACKs (wait briefly before ACKing)
> - Adaptive timeout calculation

## Related Concepts

> [!note]+ See Also
> - **[[TCP Structure]]**: Detailed segment header format
> - **[[TCP Flow Control]]**: Window management
> - **[[UDP]]**: Unreliable alternative to TCP
> - **[[Reliable Data Transfer]]**: Principles TCP implements
> - **[[Go-Back-N]]**: Cumulative ACK protocol
> - **[[Selective Repeat]]**: Buffering strategy
> - **[[Checksum]]**: Error detection in TCP
> - **[[Socket]]**: Interface for TCP communication
> - **[[Transport Layer]]**: Layer where TCP operates
> - **[[RTT]]**: Affects TCP timeout calculation

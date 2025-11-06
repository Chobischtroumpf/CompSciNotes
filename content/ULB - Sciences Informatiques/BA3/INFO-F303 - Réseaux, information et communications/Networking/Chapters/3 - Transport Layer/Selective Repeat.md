---
title: Selective Repeat
authors: Alessandro Dorigo
tags:
  - Network
---


> [!info]+ Definition
> **Selective Repeat (SR)** is a pipelined [[Reliable Data Transfer]] protocol where the receiver individually acknowledges all correctly received packets and buffers out-of-order packets for eventual in-order delivery. The sender maintains a timer for each unACKed packet and only retransmits individual lost packets.

## Core Concept

> [!abstract]+ Individual Acknowledgment and Retransmission
> **Key differences from [[Go-Back-N]]**:
> - **Receiver**: Individually acknowledges all correctly received packets
> - **Receiver**: Buffers out-of-order packets for eventual in-order delivery
> - **Sender**: Maintains timer for each unACKed packet
> - **Sender**: Only retransmits individual unACKed packets (selective retransmission)
>
> **Result**: More efficient than GBN but more complex implementation

## Sender and Receiver Windows

> [!note]+ Window Structure
> ![[Pasted image 20251102103332.png]]
>
> **Sender window**:
> - $N$ consecutive sequence numbers
> - Limits sequence numbers of sent, unACKed packets
> - Tracks which packets have been ACKed individually
>
> **Receiver window**:
> - $N$ consecutive sequence numbers
> - Defines acceptable range for incoming packets
> - Buffers out-of-order packets within window

## Sender Behavior

### Data from Above

> [!abstract]+ New data to send
> **Condition**: Application has data and next sequence number available in window
>
> **Action**:
> - Check if next available sequence number is in window
> - If yes: create packet, send it, start timer for this packet
> - If no: refuse data (window full)

### Timeout($n$)

> [!abstract]+ Timer expires for packet $n$
> **Action**:
> - Resend **only packet $n$** (selective retransmission)
> - Restart timer for packet $n$
> - Do not resend other packets

### ACK($n$) Received

> [!abstract]+ ACK for packet $n$ in range $[\text{sendbase}, \text{sendbase} + N - 1]$
> **Action**:
> - Mark packet $n$ as received
> - Stop timer for packet $n$
> - **If n is smallest unACKed packet** ($\text{sendbase}$):
>   - Advance window base ($\text{sendbase}$) to next unACKed sequence number
>   - May advance multiple positions if several consecutive packets ACKed

> [!tip]+ Sender Summary
> - Maintains individual timers (conceptually) for each packet
> - Window slides forward only when base packet is ACKed
> - Can have ACKed packets in middle of window (gaps)

## Receiver Behavior

### Packet $n$ in $[\text{rcvbase}, \text{rcvbase} + N - 1]$

> [!abstract]+ Packet in receiver window
> **Action**:
> - Send ACK($n$)
> - **If out-of-order**: Buffer packet for later delivery
> - **If in-order** (packet `n == rcvbase`):
>   - Deliver packet $n$ to application
>   - Deliver any buffered, consecutive packets starting from $n + 1$
>   - Advance window base ($\text{rcvbase}$) to next not-yet-received packet

### Packet $n$ in $[\text{rcvbase} - N, \text{rcvbase} - 1]$

> [!abstract]+ Packet below window (already received before)
> **Reason**: Sender can lag behind receiver by at most $N$ packets
>
> **Action**:
> - Send ACK($n$)
> - Packet was previously received, ACK might have been lost
> - Resending ACK helps sender advance its window

### Otherwise

> [!abstract]+ Packet outside acceptable range
> **Action**:
> - Ignore packet
> - Too old or too far ahead

> [!tip]+ Receiver Summary
> - Buffers out-of-order packets within window
> - Individually ACKs each correctly received packet
> - Window slides forward as in-order data delivered to application
> - Must handle old ACKs (sender lagging behind)

## Window Positions

> [!info]+ Relative Window Positions
> ![[Pasted image 20251102104117.png]]
>
> **Scenario shown**: Receiver window ahead of sender window
>
> **Explanation**:
> - Sender transmitted packets, window hasn't moved (waiting for ACKs)
> - Receiver successfully received packets and advanced window
> - ACKs are still in transit back to sender
> - Once ACKs arrive, sender window will slide forward to catch up
>
> **Note**: Receiver can be ahead by at most $N$ packets

> [!warning]+ Invalid Positions
> ![[Pasted image 20251102104211.png]]
>
> **Analysis of three scenarios**:
>
> **Left (Receiver behind sender)**:
> - Impossible: Receiver cannot receive packets sender hasn't sent
> - Receiver cannot go backwards in sequence space
>
> **Middle (Receiver slightly ahead)**:
> - Valid: Packets transmitted, receiver got them, ACKs in transit
> - Common occurrence during normal operation
>
> **Right (Receiver far ahead)**:
> - Invalid: Gap too large to be explained by in-flight packets
> - Receiver can only advance by receiving sent packets
> - Maximum distance receiver can be ahead is limited by sender window size

## Selective Repeat in Action

> [!example]+ Protocol Operation
> ![[Pasted image 20251102105859.png]]
>
> **Scenario walkthrough**:
>
> **Initial transmission**:
> - Sender sends pkt0, pkt1, pkt2, pkt3
> - Receiver receives pkt0: sends ACK(0), delivers to app
> - Receiver receives pkt1: sends ACK(1), delivers to app
> - **Pkt2 is lost** (X)
> - Receiver receives pkt3: sends ACK(3), **buffers pkt3** (out-of-order)
>
> **Sender behavior**:
> - Receives ACK(0): marks pkt0 as received, slides window
> - Receives ACK(1): marks pkt1 as received, slides window
> - Receives ACK(3): marks pkt3 as received, but **window doesn't slide** (pkt2 still missing)
> - **Timeout for pkt2**: retransmits only pkt2
>
> **Recovery**:
> - Receiver gets pkt2: sends ACK(2)
> - Has pkt2 in order, delivers pkt2 to application
> - Has buffered pkt3, delivers pkt3 to application
> - Advances window
> - Sender receives ACK(2), slides window forward

## Maximum Window Size

> [!warning]+ Window Size Dilemma
> **Problem**: With finite sequence number space, how large can windows be?
> **If sequence number size = $K$**, what is maximum window size $N$?

### Why $N \leq K/2$

> [!example]+ Example: $K = 4, N = 3$ (Too Large)
> ![[Pasted image 20251102110216.png]]
>
> **Scenario that causes failure**:
> 1. Sender sends pkt0, pkt1, pkt2 ($N = 3$)
> 2. All packets received successfully by receiver
> 3. Receiver sends ACK(0), ACK(1), ACK(2)
> 4. Receiver advances window to `[3, 0, 1]` (wraps around)
> 5. **All ACKs are lost**
> 6. Sender times out and resends pkt0, pkt1, pkt2
> 7. **Problem**: Receiver's window is now `[3, 0, 1]`
> 8. Receiver accepts pkt0 as **new data** (within window)
> 9. **Duplicates delivered to application**

### Correct Window Size

> [!example]+ Example: $K = 4, N = 2$ (Correct)
> ![[Pasted image 20251102110728.png]]
>
> **Diagrams a/b: $K = 4, N = 3$ (incorrect)**
> - a) Initial situation with a window of size $N = 3$
> - b) After 3 frames have been sent and received but not ACK’ed, the upper side of the rec window falls in the sending window
>
> **Diagrams c/d: $K = 4, N = 2$ (correct)**
> - c) Initial situation with a window of size $N = 2$
> - d) After 2 frames sent and received but not ACK’ed, the upper side of the rec window does not fall in the sending window

> [!success]+ Window Size Rule
> **Constraint for correctness**:
> ```
> Window size (N) ≤ Sequence number space (K) / 2
> ```
>
> **Why**: Ensures receiver can distinguish between:
> - New packets in next window cycle
> - Retransmitted packets from current window cycle

## Related Concepts

> [!note]+ See Also
> - **[[Reliable Data Transfer]]**: RDT protocol overview
> - **[[Go-Back-N]]**: Simpler alternative to SR
> - **[[TCP]]**: Uses SR-like buffering with cumulative ACKs
> - **[[Transport Layer]]**: Layer where SR operates
> - **[[RTT]]**: Affects timeout and performance

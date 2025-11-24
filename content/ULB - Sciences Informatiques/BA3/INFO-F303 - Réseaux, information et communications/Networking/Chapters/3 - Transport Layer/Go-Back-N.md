---
title: Go-Back-N
authors: Alessandro Dorigo
tags:
  - Network
---


> [!info]+ Definition
> **Go-Back-N (GBN)** is a pipelined [[Reliable Data Transfer]] protocol where the sender can have up to $N$ unacknowledged packets in the pipeline. It uses cumulative acknowledgments and retransmits all packets from the first unacknowledged packet onward when a timeout occurs.

## Core Concept

> [!abstract]+ Sliding Window Protocol
> **Sender's perspective**:
> - Maintains window of (max) $N$ consecutive transmitted but unACKed packets
> - Window slides forward as ACKs are received
> - Can send multiple packets without waiting for individual ACKs
>
> ![[606ce61871818d5526c551d5e95b40ea.png]]
>
> **Window positions**:
> - `base`: Sequence number of oldest unACKed packet
> - `nextseqnum`: Smallest unused sequence number (next to be sent)
> - **Window size**: $N$ packets maximum

## Key Mechanisms

> [!success]+ Cumulative Acknowledgments
> **ACK($n$) acknowledges all packets up to and including sequence number $n$**
>
> **On receiving ACK($n$)**:
> - Move window forward to begin at $n + 1$
> - All packets $\leq n$ are considered received
> - Frees up window space for new packets
>
> **Benefits**:
> - Simple to implement
> - Lost ACKs less problematic (later ACKs cover earlier ones)
> - Reduces `ACK` overhead

> [!info]+ Single Timer
> **Conceptually for the oldest in-flight packet**
>
> **Timer behavior**:
> - Start timer when first packet sent (when `base == nextseqnum`)
> - Restart timer when `ACK` received and packets still outstanding
> - Stop timer when all packets acknowledged (`base == nextseqnum`)
>
> **On timeout($n$)**:
> - Retransmit packet $n$ (base packet)
> - Retransmit all higher sequence number packets in window
> - This is the "Go-Back-N" behavior - go back and resend everything

## Sender Behavior

> [!note]+ Sender Extended FSM
> ![[5165594c82ca3d4ae704caed08604b7a.png]]
>
> **Single state**: Wait
>
> **Four possible events**:

### Event 1: New Data to Send

> [!abstract]+ `rdt_send(data)` - Application has data
> **Action**:
> - Check if window is full: `nextseqnum < base + N`
> - **If window has space**:
>   - Create packet with sequence number `nextseqnum`
>   - Send packet via `udt_send()`
>   - If first unACKed packet (`base == nextseqnum`): start timer
>   - Increment `nextseqnum`
> - **If window is full**:
>   - Refuse data (or buffer at application layer)
>   - Must wait for ACKs before sending more

### Event 2: Corrupted ACK Received

> [!abstract]+ `rdt_rcv(rcvpkt) && corrupt(rcvpkt)` - Bad ACK
> **Action**:
> - Do nothing (Λ)
> - Ignore corrupted `ACK`
> - Timer will eventually trigger retransmission if needed

### Event 3: Valid ACK Received

> [!abstract]+ `rdt_rcv(rcvpkt) && notcorrupt(rcvpkt)` - Good ACK
> **Action**:
> - Set `base = getacknum(rcvpkt) + 1`
> - Move window forward to next unACKed packet
> - **If `base == nextseqnum`**:
>   - All packets ACKed, stop timer
> - **Else**:
>   - Still waiting for some packets, restart timer

### Event 4: Timer Expires

> [!abstract]+ `timeout` - No ACK received in time
> **Action (Go-Back-N behavior)**:
> - Restart timer
> - Resend packet `base`
> - Resend packet `base + 1`
> - Continue resending through last sent packet
> - Retransmit entire window

> [!tip]+ Event Summary Table
>
> | Event | Condition | Action |
> |-------|-----------|--------|
> | `rdt_send(data)` | Application has data | Send if window not full |
> | Corrupted `ACK` | `corrupt(rcvpkt)` | Do nothing (Λ) |
> | Valid `ACK` | `notcorrupt(rcvpkt)` | Slide window forward |
> | Timeout | Timer expires | **Retransmit entire window** |

## Receiver Behavior

> [!note]+ Receiver Extended FSM
> ![[e4b4fe22c79e24af75e16fee361ffcd4.png]]
>
> **Single state**: Wait
>
> **Key characteristic**: `ACK`-only, always send `ACK` for correctly-received packet with highest in-order sequence number

### Receiver Logic

> [!abstract]+ Expected Packet Arrives
> **`rdt_rcv(rcvpkt) && notcorrupt(rcvpkt) && hasseqnum(rcvpkt, expectedseqnum)`**
>
> **Action**:
> - Extract data from packet
> - Deliver data to application layer
> - Send `ACK(expectedseqnum)`
> - Increment `expectedseqnum`

> [!abstract]+ Out-of-Order or Corrupted Packet
> **Any other case**
>
> **Action for out-of-order packet**:
> - **Discard packet** (no buffering!)
> - Re-`ACK` packet with highest in-order sequence number
> - Send `ACK(expectedseqnum - 1)`
> - Generates duplicate ACKs
>
> **Action for corrupted packet**:
> - Discard packet
> - Re-`ACK` last correctly received packet

> [!warning]+ No Receiver Buffering
> **Important characteristic**:
> - Receiver only remembers `expectedseqnum`
> - Does not buffer out-of-order packets
> - Simpler receiver implementation
> - But causes retransmission of successfully received packets

## Go-Back-N in Action

> [!example]+ Protocol Operation
> ![[224d16a1a632f51355f3991c80af2308.png]]
>
> **Scenario walkthrough**:
>
> **Initial transmission**:
> - Sender sends packets 0, 1, 2, 3 (window size N=4)
> - Packets 0, 1 arrive successfully at receiver
> - **Packet 2 is lost** (X)
> - Packet 3 arrives but is out-of-order
>
> **Receiver behavior**:
> - Receives `pkt0`: sends `ACK(0)`, expects `pkt1`
> - Receives `pkt1`: sends `ACK(1)`, expects `pkt2`
> - `pkt2` never arrives
> - Receives `pkt3` (out-of-order): **discards `pkt3`**, sends `ACK(1)` again
> - Continues to discard all packets until `pkt2` received
>
> **Sender behavior**:
> - Receives `ACK(0)`, `ACK(1)` normally
> - Receives duplicate `ACK(1)` - ignores it
> - **Timeout occurs** (no `ACK` for `pkt2`)
> - Retransmits `pkt2`, `pkt3` (goes back to `pkt2`)
>
> **Recovery**:
> - Receiver gets `pkt2`: sends `ACK(2)`
> - Receiver gets `pkt3` (again): sends `ACK(3)`
> - Transmission continues normally

> [!success]+ Why It Works
> **GBN fixes [[RDT 3.3]] problems**:
> - Pipeline of packets queued and sent
> - Moving window maintains order
> - Lost packets eventually retransmitted via timeout
> - Cumulative ACKs reduce `ACK` overhead

## Maximum Window Size

> [!warning]+ Window Size Constraint
> **Problem**: If sequence number space is finite, window size must be limited
>
> **If sequence number size = $K$**:
> - Can have sequence numbers: $0, 1, 2, \dots, K - 1$
> - What is maximum window size $N$?

### Why $N$ Cannot Equal $K$

> [!example]+ Example: $K = 4, N = 4$ (Incorrect)
> ![[0c92e5f53e2a36f7bdae5d0ae5e8821c.png]]
>
> **Scenario**:
> 1. Sender sends `pkt0`, `pkt1`, `pkt2`, `pkt3` (window full)
> 2. All packets received and delivered to application
> 3. **All ACKs are lost**
> 4. Timeout occurs at sender
> 5. Sender retransmits `pkt0`, `pkt1`, `pkt2`, `pkt3`
> 6. Receiver expects `pkt0` (sequence numbers wrapped around)
> 7. **Problem**: Receiver accepts retransmitted packets as new data
> 8. **Duplicates delivered to application**

### Correct Window Size

> [!example]+ Example: $K = 4, N = 3$ (Correct)
> ![[6d669389adac4f5f98fe9ec3a0f0d50c.png]]
>
> **Scenario**:
> 1. Sender sends `pkt0`, `pkt1`, `pkt2` (window size N=3)
> 2. All packets received successfully
> 3. **All ACKs are lost**
> 4. Timeout occurs at sender
> 5. Sender retransmits `pkt0`, `pkt1`, `pkt2`
> 6. Receiver expects `pkt3` (not `pkt0`)
> 7. Receiver discards `pkt0`, `pkt1`, `pkt2` as out-of-order
> 8. Receiver sends back ACKs
> 9. **No duplicates delivered**

> [!success]+ Window Size Rule
> **Constraint for correctness**:
> ```
> Window size (N) ≤ Sequence number space (K) - 1
> ```
>
> **Why**: Ensures receiver can distinguish retransmissions from new packets

## Related Concepts

> [!note]+ See Also
> - **[[Reliable Data Transfer]]**: RDT protocol overview
> - **[[RDT 3.3]]**: Stop-and-wait protocol that GBN improves upon
> - **[[Selective Repeat]]**: More sophisticated alternative to GBN
> - **[[TCP]]**: Uses cumulative ACKs like GBN (but with enhancements)
> - **[[Transport Layer]]**: Layer where GBN operates
> - **[[RTT]]**: Affects timeout and performance

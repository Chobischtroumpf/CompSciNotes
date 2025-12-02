---
title: RDT 3.2
authors: Mihai Bors
tags:
  - Network
---
> [!info]+ Definition
> **RDT 3.2** fixes the race condition in [[RDT 3.1]] by adding sequence numbers to ACK messages. The receiver must specify which packet sequence number is being acknowledged, eliminating ambiguity.

## The Solution: Numbered ACKs

> [!success]+ What Changes
> **ACKs now include sequence number**:
> - Receiver specifies which packet it's acknowledging
> - ACK(0) means "I received packet 0 correctly"
> - ACK(1) means "I received packet 1 correctly"
>
> **Benefits**:
> - Sender knows exactly what was received
> - No ambiguity about which transmission is acknowledged
> - Breaks the deadlock from [[RDT 3.1]]

## Fixing the Race Condition
![[f7ebf54c84c214119d187692ea60ac93.png]]

> [!example]+ Recovered Scenario
> **Same situation as [[RDT 3.1]] problem**, but fixed:
> 1. Sender sends pkt(0), receiver gets it, sends ACK(0)
> 2. Timeout occurs, sender retransmits pkt(0)
> 3. **Receiver gets duplicate pkt(0)**, discards, sends ACK(0) again
> 4. **Sender sends pkt(1), but it gets lost**
> 5. **Event B**: Sender never receives ACK(1)
> 6. **Critical difference**: When timeout occurs:
>    - Sender knows it didn't receive ACK(1)
>    - Sender retransmits pkt(1) (not pkt(0)!)
> 7. Receiver gets pkt(1), sends ACK(1)

## Sender FSM
![[e4e2282240161ca6155a98420212e29d.png]]

> [!note]+ Sender States and Logic
> **States** (still 4, like [[RDT 2.1]]):
> 1. Wait for call from above (seq 0)
> 2. Wait for ACK 0
> 3. Wait for call from above (seq 1)
> 4. Wait for ACK 1
>
> **Key difference from earlier versions**:
> - Checks if received ACK has correct sequence number
> - ACK(0) only valid when waiting for ACK 0
> - ACK(1) only valid when waiting for ACK 1
> - Wrong ACK number treated like timeout -> retransmit

## Alternating-Bit Protocol

> [!info]+ Protocol Name
> **RDT 3.2 is called the "Alternating-Bit Protocol"**:
> - Sequence numbers alternate: 0, 1, 0, 1, 0, 1, ...
> - ACKs also alternate: ACK(0), ACK(1), ACK(0), ACK(1), ...
> - Simple but effective for stop-and-wait
> - Foundation for more complex protocols

## Example Scenarios
| ![[11cb1ae75adafb45e410057e48a712ac.png]] | ![[e1e4798225d86052b133ab938e1de846.png]] |
| :----------------------------------: | :----------------------------------: |
|        No loss / Packet loss         |     ACK loss / Premature timeout     |

## Related Concepts

> [!note]+ See Also
> - **[[Reliable Data Transfer]]**: RDT overview
> - **[[RDT 3.1]]**: Previous version (race condition problem)
> - **[[RDT 3.3]]**: Next version (performance analysis)
> - **[[TCP]]**: Real protocol using similar concepts
> - **[[Transport Layer]]**: Where RDT operates

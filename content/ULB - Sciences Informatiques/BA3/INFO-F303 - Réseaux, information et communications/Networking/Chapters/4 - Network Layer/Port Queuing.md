---
title: Port Queuing
authors: Alessandro Dorigo, Mihai Bors
tags:
  - Network
---
## Input Port Queueing

> [!info]+ Definition
> Input port queueing occurs when the switch fabric is slower than the combined rate of input ports, causing packets to queue at input buffers.

> [!abstract]+ Queueing Effects
> **Condition for queueing:**
>
> $$ \text{Switch fabric rate} < \sum_{i=1}^{N} \text{input port rate}_i \implies \text{queueing occurs} $$
>
> **Consequences:**
> - Queueing delay at input buffers
> - Packet loss due to input buffer overflow

> [!example]+
> ![[db110b18d02a2eba279f877fbfaf9fad.png]]
>
> **Initial situation:**
> - Output port contention: only one red packet can be transferred, lower red packet is *blocked*
> - Three input queues with colored packets (red, blue, green) waiting to be switched
>
> **One packet time later:**
> - Green packet experiences HOL blocking
> - Even though the green packet's output port is free, it cannot proceed because it is blocked by the red packet at the head of its queue

## Output Port Queueing

> [!info]+ Definition
> Output port queueing occurs when packets arrive at the output port via the switch fabric faster than they can be transmitted on the output link.

> [!example]+
> ![[d5351ee753d1c526422877d821439f6e.png]]
>
> **At time $t$:** Packets move from input to output through switch fabric
> **One packet time later:** Packets queue at output port waiting for transmission
>
> **Buffering condition:**
> $$ \text{Arrival rate via switch} > \text{output line speed} \implies \text{buffering required} $$
>
> **Consequences:**
> - Queueing (delay) at output port
> - Loss due to output port buffer overflow

> [!info]+ Buffering
> **Buffering** is required when packets arrive from fabric faster than link transmission rate. The question is: which packet to drop if no free buffers?
>
> ![[fc4f3c8ca86f7f63391d14a32a218cef.png]]

> [!info]+ Scheduling Discipline
> **Scheduling discipline** chooses among queued packets for transmission.
>
> **Scheduling options:**
> - FIFO scheduling
> - More advanced techniques (priority scheduling, WFQ - Weighted Fair Queueing)

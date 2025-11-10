---
title: TCP Connection Management
authors: Alessandro Dorigo
tags:
  - Network
---


> [!info]+ Definition
> **TCP Connection Management** is the process by which [[TCP]] establishes and terminates connections between sender and receiver through a handshaking procedure. Before exchanging data, endpoints agree to establish a connection and negotiate connection parameters.

## Connection Setup

> [!abstract]- Handshake Purpose
> Before exchanging data, sender and receiver "handshake" to:
> - Agree to establish connection (each knowing the other willing to establish connection)
> - Agree on connection parameters (starting sequence numbers, MSS, options)

## Client-Side Connection Initiation

> [!note]+ Client Socket Creation
> **Client initiates connection**:
> ```C
> Socket clientSocket = new Socket("hostname", "port number");
> ```
>
> ![[2b29a09e5b7b97c55cfdec0ebd2357ab.png]]
>
> **Process**:
> - Client creates socket and specifies server hostname and port
> - Triggers connection establishment process
> - Client transitions from CLOSED state

## Server-Side Connection Acceptance

> [!note]+ Server Socket Acceptance
> **Server accepts connection**:
> ```C
> Socket connectionSocket = welcomeSocket.accept();
> ```
>
> ![[0ed9d88c83359cd3e036a6aa5cc72068.png]]
>
> **Process**:
> - Server listens on welcome socket
> - Accepts incoming connection request
> - Creates new connection socket for this specific client
> - Server transitions from LISTEN state

## Handshake Protocols

> [!abstract]- Available Protocols
> TCP connection establishment can use different handshake protocols:
> - **[[2-way-handshake]]**: Simple but flawed approach
> - **[[3-way-handshake]]**: Standard TCP connection establishment

## Closing TCP Connections

> [!abstract]- Connection Termination Process
> **Graceful close procedure**:
> - Client and server each close their side of connection
> - Send TCP segment with FIN bit = 1
> - Symmetric/graceful release
> - Respond to received FIN with ACK
> - On receiving FIN, ACK can be combined with own FIN
> - Simultaneous FIN exchanges can be handled
>
> ![[c99e4546bc669ad74a5ad3e5d46c34aa.png]]

### Four-Way Close Sequence

> [!note]+ Step 1: Client Initiates Close
> **Client calls `clientSocket.close()`**:
> - Client sends `FIN(seq=x)` with `FINbit=1`
> - May include last data from client (possibly empty)
> - Client state: `ESTAB -> FIN_WAIT_1`
> - Client can no longer send data, but **can still receive**

> [!note]+ Step 2: Server Acknowledges Client's `FIN`
> **Server receives `FIN`**:
> - Server sends `ACK(x+1)` - acknowledging receipt of client's `FIN`
> - Server state: `ESTAB -> CLOSE_WAIT`
> - Client state: `FIN_WAIT_1 -> FIN_WAIT_2`
> - **Important**: Server application can still send data at this point!

> [!note]+ Step 3: Server Initiates Its Close
> **Server calls `serverSocket.close()`**:
> - Server sends `FIN(seq=y)` with `FINbit=1`
> - Server state: `CLOSE_WAIT -> LAST_ACK`
> - Server can no longer send data
> - Waiting for client to acknowledge server's `FIN`

> [!note]+ Step 4: Client Acknowledges Server's `FIN`
> **Client receives server's FIN**:
> - Client sends `ACK(y+1)` - acknowledging server's `FIN`
> - Client state: `FIN_WAIT_2 -> TIMED_WAIT`
> - Server receives `ACK` and goes to `CLOSED` state

### `TIMED_WAIT` State

> [!warning]+ Why Wait 2 × MSL?
> **Client waits for 2 × MSL (Maximum Segment Lifetime) before closing**
>
> **Reasons for this wait**:
> 1. **Allow for lost `ACK` retransmission**:
>    - If the final `ACK` gets lost, server will retransmit its `FIN`
>    - Client needs to be around to respond to that retransmission
> 2. **Prevent old segments from confusing new connections**:
>    - Ensures all segments from this connection die in the network
>    - Prevents delayed packets from appearing in a new connection using same ports
>
> **After `TIMED_WAIT` expires**: Client -> `CLOSED`

## Connection State Machine

![[b5c1652f6c2bb4b80a76b91f46594916.png]]

### Active Close Path (Initiator)

> [!info]+ From `ESTAB -> FIN_WAIT_1`
> - Application calls `connectionSocket.close()`
> - Send `FIN` segment
> - Enter `FIN_WAIT_1` state

> [!info]+ From `FIN_WAIT_1` -> Two Possible Paths
> **Path 1: Normal 4-way close**:
> - Receive `ACK` (just `ACK`, no `FIN` yet)
> - Enter `FIN_WAIT_2` state
> - Wait for other side's `FIN`
>
> **Path 2: Simultaneous close**:
> - Receive `FIN+ACK` (both at once)
> - Send `ACK`
> - Enter `CLOSING` state

> [!info]+ From `FIN_WAIT_2 -> TIME_WAIT`
> - Receive `FIN` from other side
> - Send `ACK`
> - Enter `TIME_WAIT` state

> [!info]+ From `CLOSING -> TIME_WAIT`
> - Receive `ACK` (response to our `ACK`)
> - Enter `TIME_WAIT` state
> - Just wait for `ACK`

> [!info]+ From `TIME_WAIT -> CLOSED`
> - Wait **2 × MSL** (Maximum Segment Lifetime)
> - Close socket
> - Enter `CLOSED` state

### Passive Close Path (Responder)

> [!info]+ From `ESTAB -> CLOSE_WAIT`
> - Receive `FIN` from other side
> - Send `ACK`
> - Enter `CLOSE_WAIT` state
> - **Application can still send data!**

> [!info]+ From `CLOSE_WAIT -> LAST_ACK`
> - Application calls `connectionSocket.close()`
> - Send `FIN`
> - Enter `LAST_ACK` state
> - Note: `TCP` continues to send previous bytes reliably after socket close

> [!info]+ From `LAST_ACK -> CLOSED`
> - Receive `ACK` for our `FIN`
> - Close socket
> - Enter `CLOSED` state immediately (no `TIME_WAIT`!)

### Simultaneous Close

> [!example]+ Both Sides Call `close()` Simultaneously
> **From `ESTAB`**:
> - Both send `FIN` simultaneously
> - Both enter `FIN_WAIT_1`
>
> **From `FIN_WAIT_1`**:
> - Both receive `FIN` from other side
> - Both send `ACK`
> - Both enter `CLOSING` state
>
> **From `CLOSING`**:
> - Both receive `ACK`
> - Both enter `TIME_WAIT`
> - Both wait 2 × MSL
> - Both go to `CLOSED`

## Related Concepts

> [!note]+ See Also
> - **[[TCP]]**: Main protocol overview
> - **[[2-way-handshake]]**: Flawed connection establishment
> - **[[3-way-handshake]]**: Standard connection establishment
> - **[[TCP Structure]]**: Segment format with SYN/FIN/ACK flags
> - **[[Socket]]**: Interface for connection management
> - **[[Transport Layer]]**: Layer where TCP operates

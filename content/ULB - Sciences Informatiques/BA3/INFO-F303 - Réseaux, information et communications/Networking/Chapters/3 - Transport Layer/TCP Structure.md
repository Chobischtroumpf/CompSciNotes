---
title: TCP Structure
authors: Mihai Bors
tags:
  - Network
---
> [!info]+ Definition
> The **TCP segment structure** defines the format of [[TCP]] packets, including header fields that enable reliable, ordered, connection-oriented communication. The header contains critical information for connection management, flow control, and error detection.

## TCP Segment Format

```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|          Source Port          |       Destination Port        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                        Sequence Number                        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Acknowledgment Number                      |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|  Data |           |U|A|P|R|S|F|                               |
| Offset| Reserved  |R|C|S|S|Y|I|            Window             |
|       |           |G|K|H|T|N|N|                               |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|           Checksum            |         Urgent Pointer        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Options                    |    Padding    |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                             data                              |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

## Header Fields

### Port Numbers

> [!note]+ Source Port (16 bits)
> **Identifies the sending process/application**
> - Port number on sending host
> - Used with source IP for connection identification
> - Enables [[Demultiplexing]] at receiver

> [!note]+ Destination Port (16 bits)
> **Identifies the receiving process/application**
> - Port number on receiving host
> - Combined with destination IP to identify target
> - Well-known ports (0-1023): HTTP (80), HTTPS (443), etc.

### Sequence and Acknowledgment

> [!note]+ Sequence Number (32 bits)
> **The sequence number of the first data byte in this segment**
>
> **Special case - SYN flag set**:
> - Value is Initial Sequence Number (ISN)
> - First data byte will be ISN + 1
>
> **Normal operation**:
> - Byte stream number of first byte in segment's data
> - Enables ordered delivery
> - Allows detection of duplicates
>
> See [[TCP]] for sequence number examples

> [!note]+ Acknowledgment Number (32 bits)
> **Next sequence number the sender expects to receive**
>
> **When ACK flag is set**:
> - Contains next expected sequence number
> - Cumulative acknowledgment
> - ACK(n) means "received all bytes up to n-1"
>
> **After connection established**:
> - This field is always sent
> - Always has meaning when ACK flag set

### Header Metadata

> [!note]+ Data Offset (4 bits)
> **Number of 32-bit words in TCP header**
>
> **Purpose**:
> - Indicates where data begins
> - TCP header is multiple of 32 bits (4 bytes)
> - Minimum value: 5 (20 bytes header)
> - Maximum value: 15 (60 bytes header with 40 bytes options)
>
> **Calculation**:
> - Multiply value by 4 to get header size in bytes
> - Example: Data Offset = 5 → 20 byte header

> [!note]+ Reserved (6 bits)
> **Reserved for future use**
> - Must be zero
> - Available for protocol extensions

### Control Flags

> [!info]+ Control Bits (6 bits)
> **From left to right**:
>
> | Flag | Name | Purpose |
> |------|------|---------|
> | **URG** | Urgent | Urgent Pointer field significant |
> | **ACK** | Acknowledgment | Acknowledgment field significant |
> | **PSH** | Push | Push function - deliver data immediately |
> | **RST** | Reset | Reset the connection |
> | **SYN** | Synchronize | Synchronize sequence numbers (connection setup) |
> | **FIN** | Finish | No more data from sender (connection close) |

> [!example]+ Common Flag Combinations
> - **SYN**: Connection request (seq = ISN)
> - **SYN + ACK**: Connection acceptance
> - **ACK**: Normal data transfer
> - **FIN + ACK**: Graceful connection close
> - **RST**: Abrupt connection termination
> - **PSH + ACK**: Immediate data delivery requested

### Flow Control

> [!note]+ Window (16 bits)
> **Receiver's advertised receive window**
>
> **Purpose**:
> - Number of bytes receiver willing to accept
> - Starts at byte indicated in acknowledgment field
> - Implements [[TCP Flow Control]]
>
> **Usage**:
> - Prevents sender from overwhelming receiver
> - Sender limits unACKed data to this value
> - Dynamic - changes based on receiver buffer availability
>
> **Example**:
> - Window = 4096 means "I can accept 4096 more bytes"
> - If ACK = 1000, can send bytes 1000-5095

### Error Detection

See [[Checksum]] for more details about error detection.

> [!info]+ Pseudo-Header for Checksum
> ```
> +--------+--------+--------+--------+
> |           Source Address          |
> +--------+--------+--------+--------+
> |         Destination Address       |
> +--------+--------+--------+--------+
> |  zero  |  PTCL  |    TCP Length   |
> +--------+--------+--------+--------+
> ```
>
> **Fields**:
> - Source/Destination Address: From IP header
> - PTCL: Protocol (6 for TCP)
> - TCP Length: Header + data length (not explicitly transmitted)
>
> **Purpose**: Protects against misrouted segments

### Urgent Data

> [!note]+ Urgent Pointer (16 bits)
> **Points to end of urgent data**
>
> **When URG flag set**:
> - Positive offset from sequence number
> - Points to sequence number of byte following urgent data
> - Allows out-of-band signaling
>
> **Usage**:
> - Rarely used in modern applications
> - Originally for interrupt signals (Ctrl+C in Telnet)
> - Most applications don't use urgent mechanism

## TCP Options

> [!info]+ Options Field (Variable)
> **Optional parameters at end of TCP header**
>
> **Characteristics**:
> - Multiple of 8 bits in length
> - All options included in checksum
> - Can begin on any byte boundary
> - Padding added to reach 32-bit boundary

> [!note]+ Option Format
> **Two cases**:
>
> **Case 1 - Single byte**:
> - One byte of option-kind
> - Example: End-of-Option, No-Operation
>
> **Case 2 - Multiple bytes**:
> - One byte: option-kind
> - One byte: option-length (includes kind and length bytes)
> - Variable: option-data

### Common TCP Options

> [!example]+ Option: End of Option List (Kind=0)
> ```
> +--------+
> |00000000|
> +--------+
>  Kind=0
> ```
>
> **Purpose**:
> - Marks end of option list
> - Used at end of all options
> - May not coincide with data offset boundary

> [!example]+ Option: No-Operation (Kind=1)
> ```
> +--------+
> |00000001|
> +--------+
>  Kind=1
> ```
>
> **Purpose**:
> - Used between options for alignment
> - Aligns subsequent options on word boundaries
> - Not guaranteed to be sent
> - Receivers must handle unaligned options

> [!example]+ Option: Maximum Segment Size (Kind=2)
> ```
> +--------+--------+---------+--------+
> |00000010|00000100|   max seg size   |
> +--------+--------+---------+--------+
>  Kind=2   Length=4      (16 bits)
> ```
>
> **Purpose**:
> - Communicates maximum receive segment size
> - Only sent in initial connection request (SYN segments)
> - Helps optimize segment size
> - If not used, any segment size allowed
>
> **Example values**:
> - 1460 bytes (common for Ethernet: 1500 MTU - 20 IP - 20 TCP)
> - 536 bytes (default minimum)

> [!tip]+ Other TCP Options
> Additional options exist (not shown in basic structure):
> - **Window Scale** (Kind=3): For windows > 65,535 bytes
> - **Timestamps** (Kind=8): For RTT measurement
> - **SACK Permitted** (Kind=4): Enable selective acknowledgments
> - **SACK** (Kind=5): Selective acknowledgment ranges

### Padding

> [!note]+ Padding (Variable)
> **Ensures header ends on 32-bit boundary**
>
> **Characteristics**:
> - Composed of zeros
> - Makes header length multiple of 4 bytes
> - Ensures data begins on 32-bit boundary
>
> **Example**:
> - If options are 10 bytes, add 2 bytes padding
> - Total header: 20 (base) + 10 (options) + 2 (padding) = 32 bytes

## Header Size Summary

> [!abstract]+ TCP Header Sizes
> **Minimum header**: 20 bytes
> - No options
> - Data Offset = 5
>
> **Maximum header**: 60 bytes
> - 40 bytes of options
> - Data Offset = 15
>
> **Typical header**: 20-32 bytes
> - Usually includes some options (MSS, timestamps, etc.)

## Related Concepts

> [!note]+ See Also
> - **[[TCP]]**: Protocol overview and behavior
> - **[[TCP Flow Control]]**: How window field is used
> - **[[Checksum]]**: Error detection mechanism
> - **[[Transport Layer]]**: Layer where TCP operates
> - **[[Reliable Data Transfer]]**: Principles implemented by TCP
> - **[[Socket]]**: Interface for TCP communication

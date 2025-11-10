---
title: Checksum
authors: Alessandro Dorigo
tags:
  - Network
---


> [!info]+ Definition
> A **checksum** is an error-detection mechanism used by transport protocols ([[UDP]], [[TCP]]) to detect bit errors in transmitted segments. It uses one's complement arithmetic to create a checksum value that's verified at the receiver.

![[fca18023c518126b5872a623c8dcf3c8.png]]

## Checksum Calculation Steps

> [!note]+ How to Calculate UDP Checksum
> **5-step process**:
>
> ### 1. Divide into 16-bit Words
> - Split payload and headers into 16-bit (2-byte) chunks
> - Includes some IP headers
> - All data treated as sequence of 16-bit integers
>
> ### 2. Sum the 16-bit Words
> - Add all 16-bit words together
> - Use one's complement addition
> - When addition produces carry, wrap it around
>
> ### 3. Handle Overflow
> - If sum exceeds 16 bits, carry bit wraps around
> - Add carry bit back to the result
> - This is key to one's complement arithmetic
>
> ### 4. Take One's Complement
> - Invert all bits of the sum
> - 0 becomes 1, 1 becomes 0
> - This produces the checksum value
> - Special case: checksum of 0 changed to all 1s (0xFFFF)
>
> ### 5. Append to Message
> - Checksum placed in checksum field of header
> - Transmitted along with the segment

## Detailed Example

> [!example]+ Checksum Calculation
> **Given hexadecimal values**:
> ```
> 84eb dfea 9edf
> ```
>
> **Step 1: Divide into 16-bit words**
> ```
> 84eb, dfea, 9edf
> ```
>
> **Step 2: Sum the words**
> ```
> 84eb
> +dfea
> +9edf
> ─────
> 203b4
> ```
>
> **Step 3: Handle overflow**
> - Sum `203b4` exceeds 16 bits (FFFF)
> - Overflow is `2` (from **2**03b4)
> - Wrap around and add:
> ```
> 03b4
> +   2
> ─────
> 03b6
> ```
>
> **Step 4: Take one's complement**
> ```
> 03b6 = 0000 0011 1011 0110 (binary)
> NOT  = 1111 1100 0100 1001 = fc49 (hex)
> ```
>
> **Step 5: Insert checksum**
> - Checksum value: `fc49`
> - Placed in UDP header checksum field

## Related Concepts

> [!note]+ See Also
> - **[[UDP]]**: Uses checksums for error detection
> - **[[TCP]]**: Mandatory checksums for reliability
> - **[[Transport Layer]]**: Layer where checksums computed
> - **[[Reliable Data Transfer]]**: Checksums part of reliability mechanisms
> - **[[Packet loss]]**: Different from bit errors detected by checksums

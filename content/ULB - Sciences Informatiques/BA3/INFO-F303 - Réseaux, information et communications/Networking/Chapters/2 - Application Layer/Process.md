---
title: Process
authors: Alessandro Dorigo
tags:
  - Network
---


> [!info]+ Definition
> A **process** is a program running within a [[Host|host]]. Processes are the entities that communicate over the network to provide distributed application functionality.

^6a45eb

> [!abstract]- Inter-Process Communication
> **Within Same Host**:
> - Processes communicate using **IPC (Inter-Process Communication)**
> - Operating system provides mechanisms for local process communication
> - Examples: shared memory, pipes, message queues
>
> **Between Different Hosts**
> - Processes communicate by exchanging [[Packet#^150f99|messages]] over the [[Network#^89dac9|network]]
> - Uses [[Socket#^d7aa97|sockets]] as the interface to the transport layer
> - Requires network [[Protocol#^4bfd4c|protocols]] for reliable communication
## Process Roles
> [!note]+ Client Process
> **Definition**: The process that initiates communication
>
> **Characteristics**:
> - Sends the first message
> - Typically initiates requests for services
> - Examples: web browser, email client, file transfer client

> [!note]+ Server Process
> **Definition**: The process that awaits contact from clients
>
> **Characteristics**:
> - Listens for incoming connections
> - Responds to client requests
> - Often runs continuously
> - Examples: web server, mail server, database server
## Process Identification
> [!abstract]- Process Identifiers
> To receive messages, processes must have a unique identifier consisting of:
>
> **1. IP Address**:
> - Identifies the host device on the network
> - Each host has at least one IP address
> - Can be IPv4 (e.g., 192.168.1.1) or IPv6
>
> **2. Port Number**:
> - Identifies the specific process on the host
> - 16-bit number (0-65535)
> - Well-known ports (0-1023) for standard services
> - Registered ports (1024-49151) for specific applications
> - Dynamic/private ports (49152-65535) for temporary use

> [!example]+ Common Port Numbers
>
> |Service|Protocol|Port Number|
> |---|---|---|
> |HTTP|TCP|80|
> |HTTPS|TCP|443|
> |SMTP (email)|TCP|25|
> |DNS|UDP/TCP|53|
> |FTP|TCP|20, 21|
> |SSH|TCP|22|

> [!tip]+ Complete Address Format
> A process is uniquely identified by:
> ```
> IP_Address:Port_Number
> ```
>
> Example: `192.168.1.100:8080`
## Related Concepts
> [!note]+ See Also
> - Processes use [[Socket#^d7aa97|sockets]] to send/receive messages
> - Communication follows [[Application layer protocol|application layer protocols]]
> - Can use either [[Client-server paradigm]] or [[Peer-to-peer paradigm]]
> - Transport layer ([[TCP]] or [[UDP]]) handles actual message delivery

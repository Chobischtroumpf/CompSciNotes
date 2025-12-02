---
title: DNS protocol messages
authors: Mihai Bors
tags:
  - Network
---
> [!info]+ Definition
> **DNS protocol messages** are the standardized format for queries and responses in the Domain Name System. These messages enable the translation of human-readable domain names to IP addresses.

## DNS Message Structure

![[9de3cc54950bf4e96565fd0d07511b17.png]]
- DNS messages consist of several sections, each serving a specific purpose in the name resolution process.

## Message Header

> [!note]+ Header Fields
> **Identification**:
> - **Size**: 16-bit number
> - **Purpose**: Match queries with responses
> - **Usage**: Client sets this value; server copies it in response
>
> **Flags**:
> - **Query/Reply**: Indicates if message is a query (0) or reply (1)
> - **Recursion Desired**: Client requests recursive query processing
> - **Recursion Available**: Server indicates it can perform recursive queries
> - **Authoritative Answer**: Server is authoritative for the domain
> - **Additional flags**: Truncation, error codes, etc.

## Message Sections

> [!note]+  Questions Section
> **Purpose**: Contains the queries being asked
>
> **Fields**:
> - **Name**: Domain name being queried (e.g., www.example.com)
> - **Type**: Type of record requested
>     - A (IPv4 address)
>     - AAAA (IPv6 address)
>     - MX (Mail exchange)
>     - NS (Name server)
>     - CNAME (Canonical name)
>     - PTR (Pointer for reverse lookup)
> - **Class**: Usually IN (Internet)
>
> **Example**: "What is the A record for www.example.com?"

> [!note]+ Answers Section
> **Purpose**: Contains Resource Records (RRs) that answer the query
>
> **Content**:
> - Resource Records responding to the questions
> - Format: Name, Type, Class, TTL, Data
> - May contain multiple records
>
> **Example**: "www.example.com A 93.184.216.34 TTL=3600"

> [!note]+ Authority Section
> **Purpose**: Records for authoritative name servers
>
> **Content**:
> - Information about authoritative servers for the domain
> - Used when answer is not available
> - Points to servers that may have the answer
> - Contains NS (Name Server) records
>
> **Example**: Points to name servers like ns1.example.com

> [!note]+ Additional Section
> **Purpose**: Additional helpful information
>
> **Content**:
> - Records that may be useful but weren't explicitly requested
> - Often includes A records for name servers mentioned in Authority section
> - Reduces need for additional queries
> - Improves efficiency
>
> **Example**: IP addresses of name servers listed in Authority section

## DNS Message Types

> [!tip]+ DNS Query Message
> **Characteristics**:
> - Questions section contains the query
> - Answers, Authority, and Additional sections are empty
> - Flags indicate this is a query
> - Client sets recursion desired if wanted
>
> **Example Query**:
> ```
> Header:
>   ID: 12345
>   Flags: Query, Recursion Desired
> Questions: 1
>   www.example.com, Type A, Class IN
> Answers: 0
> Authority: 0
> Additional: 0
> ```

> [!tip]+ DNS Response Message
> **Characteristics**:
> - Questions section echoes the query
> - Answers section contains the response
> - May include authority and additional information
> - Flags indicate authoritative answer status
>
> **Example Response**:
> ```
> Header:
>   ID: 12345
>   Flags: Response, Authoritative, Recursion Available
> Questions: 1
>   www.example.com, Type A, Class IN
> Answers: 1
>   www.example.com A 93.184.216.34 TTL=3600
> Authority: 2
>   example.com NS ns1.example.com
>   example.com NS ns2.example.com
> Additional: 2
>   ns1.example.com A 192.168.1.1
>   ns2.example.com A 192.168.1.2
> ```

## Message Flags in Detail

> [!info]+ Query/Response Flag (QR)
> - **0**: Message is a query
> - **1**: Message is a response

> [!info]+ Authoritative Answer (AA)
> - Set in responses
> - Indicates server is authoritative for the domain
> - Important for determining answer reliability

> [!info]+ Recursion Desired (RD)
> - Set in queries
> - Requests server to perform recursive resolution
> - Most client queries set this flag

> [!info]+ Recursion Available (RA)
> - Set in responses
> - Indicates server supports recursive queries
> - Tells client if recursion is possible

## DNS Resource Records (RRs)

> [!note]+ Resource Record Format
> Each RR in the message contains:
> - **Name**: Domain name
> - **Type**: Record type (A, AAAA, MX, NS, CNAME, etc.)
> - **Class**: Usually IN (Internet)
> - **TTL**: Time to Live in seconds (caching duration)
> - **RDLength**: Length of RDATA field
> - **RDATA**: The actual data (IP address, name server, etc.)

> [!example]+ Common Record Types
>
> |Type|Purpose|Example|
> |---|---|---|
> |A|IPv4 address|93.184.216.34|
> |AAAA|IPv6 address|2001:db8::1|
> |MX|Mail server|mail.example.com|
> |NS|Name server|ns1.example.com|
> |CNAME|Alias|www → webserver|
> |PTR|Reverse lookup|IP → name|
> |SOA|Zone authority|Zone metadata|

> [!tip]+ Message Efficiency
> **Optimization Techniques**:
> - Name compression to reduce message size
> - Additional section provides related records
> - TTL enables caching to reduce queries
> - Multiple answers in one response when possible

## Related Concepts

> [!note]+ See Also
> - DNS uses [[UDP]] (port 53) for most queries
> - Uses [[TCP]] (port 53) for zone transfers or large responses
> - Part of [[Application layer protocol|application layer]]
> - Works with [[Client-server paradigm]]

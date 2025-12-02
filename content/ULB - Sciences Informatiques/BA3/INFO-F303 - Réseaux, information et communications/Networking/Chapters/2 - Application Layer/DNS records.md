---
title: DNS records
authors: Mihai Bors
tags:
  - Network
---
> [!info]+ Definition
> **DNS Resource Records (RRs)** are entries in the [[DNS]] database that map domain names to various types of information. Each record has a specific format and purpose.

## Resource Record Format

> [!note]+ RR Structure
>
> ```
> (name, value, type, ttl)
> ```
>
> - **name**: Domain name or hostname
> - **value**: Data associated with the name (depends on type)
> - **type**: Record type (A, NS, CNAME, MX, etc.)
> - **ttl**: Time To Live (how long to cache the record)

## Record Types

> [!info]+ A Record (Address)
> **IPv4 address mapping**
> - **name**: Hostname (e.g., `www.example.com`)
> - **value**: IPv4 address (e.g., `93.184.216.34`)
> - **Purpose**: Maps hostname to IP address
>
> **Example**:
> ```
> (www.example.com, 93.184.216.34, A, 3600)
> ```

> [!info]+ AAAA Record
> **IPv6 address mapping**
> - **name**: Hostname
> - **value**: IPv6 address
> - **Purpose**: Maps hostname to IPv6 address
>
> **Example**:
> ```
> (www.example.com, 2001:db8::1, AAAA, 3600)
> ```

> [!info]+ NS Record (Name Server)
> **Authoritative name server**
> - **name**: Domain or DNS zone (e.g., `example.com`)
> - **value**: Hostname of authoritative name server
> - **Purpose**: Delegates subdomain to name server
>
> **Example**:
> ```
> (example.com, ns1.example.com, NS, 86400)
> ```

> [!info]+ CNAME Record (Canonical Name)
> **Alias mapping**
> - **name**: Alias hostname (e.g., `www.ibm.com`)
> - **value**: Canonical (real) hostname (e.g., `servereast.backup2.ibm.com`)
> - **Purpose**: Creates alias for another hostname
>
> **Example**:
> ```
> (www.ibm.com, servereast.backup2.ibm.com, CNAME, 3600)
> ```

> [!info]+ MX Record (Mail Exchange)
> **Mail server**
> - **name**: Domain (e.g., `example.com`)
> - **value**: Hostname of mail server
> - **Purpose**: Specifies mail server for domain
>
> **Example**:
> ```
> (example.com, mail.example.com, MX, 3600)
> ```
>
> Note: MX records also have a priority value (lower = higher priority)

> [!info]+ PTR Record (Pointer)
> **Reverse DNS lookup**
> - **name**: Reversed IP address (e.g., `34.216.184.93.in-addr.arpa`)
> - **value**: Hostname
> - **Purpose**: Maps IP address back to hostname

> [!info]+ TXT Record (Text)
> **Arbitrary text data**
> - **name**: Domain
> - **value**: Text string
> - **Purpose**: Store text information (SPF, DKIM, verification, etc.)

## Example DNS Zone

> [!example]+ Complete Zone Example
>
> ```
> example.com.         86400  IN  A      93.184.216.34
> example.com.         86400  IN  NS     ns1.example.com.
> example.com.         86400  IN  NS     ns2.example.com.
> example.com.         86400  IN  MX  10 mail.example.com.
> www.example.com.     3600   IN  CNAME  example.com.
> ns1.example.com.     86400  IN  A      192.0.2.1
> ns2.example.com.     86400  IN  A      192.0.2.2
> mail.example.com.    3600   IN  A      198.51.100.1
> ```

## Related Concepts

> [!note]+ See Also
> - [[DNS]]: Main DNS system overview
> - [[DNS protocol messages]]: How records are queried and returned
> - Used in [[Application layer protocol|application layer]]

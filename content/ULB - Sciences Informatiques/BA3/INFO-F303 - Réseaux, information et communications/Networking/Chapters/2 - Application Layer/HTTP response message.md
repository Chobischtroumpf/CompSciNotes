---
title: HTTP response message
authors: Mihai Bors
tags:
  - Network
---
> [!info]+ Definition
> An **HTTP response message** is a message sent by a server to a client in response to an [[HTTP request message|HTTP request]]. It consists of a status line, headers, and optionally a message body containing the requested resource.

## Response Message Structure

> [!note]+ Status Line
> **First line of the response**:
>
> ```
> HTTP/VERSION STATUS_CODE REASON_PHRASE
> ```
>
> **Components**:
> - **HTTP Version**: Protocol version (HTTP/1.1, HTTP/2, etc.)
> - **Status Code**: 3-digit code indicating result
> - **Reason Phrase**: Human-readable status description
>
> **Example**:
> ```
> HTTP/1.1 200 OK
> ```

> [!note]+ Headers
> **Key-value pairs providing metadata**:
> - Server information
> - Response characteristics
> - Resource metadata
> - Caching directives
> - Each header on separate line
> - End with blank line (CRLF CRLF)

> [!note]+ Message Body (Optional)
> **The actual content**:
> - HTML page, image, JSON data, etc.
> - Separated from headers by blank line
> - Length specified by `Content-Length` header
> - May be compressed (gzip, deflate)

## HTTP Response Example

> [!example]+ Complete Response
>
> ```
> HTTP/1.1 200 OK\r\n
> Date: Sun, 26 Sep 2010 20:09:20 GMT\r\n
> Server: Apache/2.0.52 (CentOS)\r\n
> Last-Modified: Tue, 30 Oct 2007 17:00:02 GMT\r\n
> ETag: "17dc6-a5c-bf716880"\r\n
> Accept-Ranges: bytes\r\n
> Content-Length: 2652\r\n
> Keep-Alive: timeout=10, max=100\r\n
> Connection: Keep-Alive\r\n
> Content-Type: text/html; charset=ISO-8859-1\r\n
> \r\n
> data data data data data ...
> ```
>
> **Notes**:
> - `\r\n` represents CRLF (Carriage Return + Line Feed)
> - Empty line (`\r\n\r\n`) separates headers from body
> - Body contains the actual HTML, JSON, or other content

## HTTP Status Codes
The status code appears in the first line in the server-client response message.

> [!success]+ 1xx: Informational
> **Request received, continuing process**
>
> |Code|Meaning|Description|
> |---|---|---|
> |100|Continue|Client should continue request|
> |101|Switching Protocols|Server switching protocols as requested|

> [!success]+ 2xx: Success
> **Request successfully received, understood, and accepted**
>
> |Code|Meaning|Description|
> |---|---|---|
> |200|OK|Request succeeded|
> |201|Created|Resource created successfully|
> |202|Accepted|Request accepted, processing not complete|
> |204|No Content|Success but no content to return|
> |206|Partial Content|Partial GET fulfilled (range request)|

> [!info]+ 3xx: Redirection
> **Further action needed to complete request**
>
> |Code|Meaning|Description|
> |---|---|---|
> |301|Moved Permanently|Resource permanently moved to new URL|
> |302|Found|Resource temporarily at different URL|
> |304|Not Modified|Cached version still valid (see [[Conditional GET]])|
> |307|Temporary Redirect|Temporary redirect, use same method|
> |308|Permanent Redirect|Permanent redirect, use same method|

> [!warning]+ 4xx: Client Error
> **Request contains bad syntax or cannot be fulfilled**
>
> |Code|Meaning|Description|
> |---|---|---|
> |400|Bad Request|Malformed request syntax|
> |401|Unauthorized|Authentication required|
> |403|Forbidden|Server refuses to fulfill request|
> |404|Not Found|Resource does not exist|
> |405|Method Not Allowed|Method not supported for resource|
> |408|Request Timeout|Client took too long to send request|
> |409|Conflict|Request conflicts with current state|
> |410|Gone|Resource permanently removed|
> |413|Payload Too Large|Request body too large|
> |414|URI Too Long|Request URI too long|
> |429|Too Many Requests|Rate limit exceeded|

> [!fail]+ 5xx: Server Error
> **Server failed to fulfill valid request**
>
> |Code|Meaning|Description|
> |---|---|---|
> |500|Internal Server Error|Generic server error|
> |501|Not Implemented|Server doesn't support functionality|
> |502|Bad Gateway|Invalid response from upstream server|
> |503|Service Unavailable|Server temporarily unavailable|
> |504|Gateway Timeout|Upstream server timeout|
> |505|HTTP Version Not Supported|HTTP version not supported by server|

## Common Response Headers

> [!note]+ Server Information
>
> ```
> Server: Apache/2.0.52 (CentOS)
> Date: Sun, 26 Sep 2010 20:09:20 GMT
> ```
>
> - **Server**: Server software identification
> - **Date**: Response timestamp

> [!note]+ Content Description
>
> ```
> Content-Type: text/html; charset=ISO-8859-1
> Content-Length: 2652
> Content-Encoding: gzip
> Content-Language: en-US
> ```
>
> - **Content-Type**: MIME type of response body
> - **Content-Length**: Size of body in bytes
> - **Content-Encoding**: Compression applied
> - **Content-Language**: Language of content

> [!note]+ Caching Headers
>
> ```
> Last-Modified: Tue, 30 Oct 2007 17:00:02 GMT
> ETag: "17dc6-a5c-bf716880"
> Cache-Control: max-age=3600, public
> Expires: Sun, 26 Sep 2010 21:09:20 GMT
> ```
>
> - **Last-Modified**: When resource was last changed
> - **ETag**: Unique identifier for resource version
> - **Cache-Control**: Caching directives
> - **Expires**: When cached copy expires
> - Used with [[Conditional GET]]

> [!note]+ Connection Management
>
> ```
> Connection: Keep-Alive
> Keep-Alive: timeout=10, max=100
> ```
>
> - Connection persistence settings
> - [[Persistent HTTP]] configuration
> - Timeout and max requests per connection

> [!note]+ Content Range (for partial requests)
>
> ```
> Accept-Ranges: bytes
> Content-Range: bytes 0-1023/4096
> ```
>
> - Indicates server supports range requests
> - Specifies which portion of content is being sent

> [!note]+ Redirection
>
> ```
> Location: https://www.newlocation.com/page.html
> ```
>
> - Used with 3xx status codes
> - Specifies new resource location

> [!note]+ Authentication
>
> ```
> WWW-Authenticate: Basic realm="Admin Area"
> Set-Cookie: sessionid=abc123; Path=/; HttpOnly
> ```
>
> - **WWW-Authenticate**: Authentication method required
> - **Set-Cookie**: Set cookies on client

## Related Concepts

> [!note]+ See Also
> - **[[HTTP request message]]**: Client's request to server
> - **[[HTTP]]**: Main protocol overview
> - **[[Conditional GET]]**: Efficient caching using 304 responses
> - **[[HTTP 1.1]]**: Protocol version and features
> - **[[HTTP 2]]**: Binary framing of response messages
> - **[[RTT]]**: Time to receive response
> - **[[Persistent HTTP]]**: Connection reuse for multiple responses

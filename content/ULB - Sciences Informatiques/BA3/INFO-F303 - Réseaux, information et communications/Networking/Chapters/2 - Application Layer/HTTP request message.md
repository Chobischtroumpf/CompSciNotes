---
title: HTTP request message
authors: Alessandro Dorigo
tags:
  - Network
---


> [!info]+ Definition
> An **HTTP request message** is a message sent by a client to a server to request a resource or perform an action. It consists of a request line, headers, and optionally a message body.
## Request Message Structure
![[7d49708b48f80f02f9913028dfd39326.png]]

> [!note]+ Request Line
> **First line of the request**:
>
> ```
> METHOD /path/to/resource HTTP/VERSION
> ```
>
> **Components**:
> - **Method**: Action to perform (`GET`, `POST`, `PUT`, etc.)
> - **Request-URI**: Path to the resource
> - **HTTP Version**: Protocol version (HTTP/1.1, HTTP/2, etc.)
>
> **Example**:
> ```
> GET /index.html HTTP/1.1
> ```

> [!note]+ Headers
> **Key-value pairs providing metadata**:
> - Request configuration
> - Client capabilities
> - Resource specifications
> - Each header on separate line
> - End with blank line (CRLF CRLF)

> [!note]+ Message Body (Optional)
> **Data being sent to server**:
> - Present in `POST`, `PUT` requests
> - Contains form data, file uploads, JSON, etc.
> - Separated from headers by blank line
> - Length specified by `Content-Length` header
## HTTP Request Example
> [!example]+ Complete GET Request
>
> ```
> GET /index.html HTTP/1.1\r\n
> Host: www-net.cs.umass.edu\r\n
> User-Agent: Firefox/3.6.10\r\n
> Accept: text/html,application/xhtml+xml\r\n
> Accept-Language: en-us,en;q=0.5\r\n
> Accept-Encoding: gzip,deflate\r\n
> Accept-Charset: ISO-8859-1,utf-8;q=0.7\r\n
> Keep-Alive: 115\r\n
> Connection: keep-alive\r\n
> \r\n
> ```
>
> **Notes**:
> - `\r\n` represents CRLF (Carriage Return + Line Feed)
> - Empty line (`\r\n\r\n`) separates headers from body
> - No body in GET request (this example)
## HTTP Request Methods
> [!info]+ GET
> **Request data from a specified resource**
>
> **Characteristics**:
> - Most common method
> - Should only retrieve data (no side effects)
> - Can include user data in URL query string
> - Format: `www.somesite.com/animalsearch?monkeys&banana`
> - Data visible in URL
> - Limited data length (URL length restrictions)
> - Can be cached and bookmarked
>
> **Example**:
> ```
> GET /search?q=networking&lang=en HTTP/1.1
> Host: www.example.com
> ```

> [!info]+ POST
> **Send data to a remote object specified in URL field**
>
> **Characteristics**:
> - Data sent in message body (not URL)
> - Used for form submissions
> - Creates or modifies resources
> - Not idempotent (multiple requests may have different effects)
> - Data not visible in URL
> - No practical data length limit
> - Cannot be cached (usually)
>
> **Example**:
> ```
> POST /api/users HTTP/1.1
> Host: www.example.com
> Content-Type: application/json
> Content-Length: 47
> {"username":"john","email":"john@example.com"}
> ```

> [!info]+ HEAD
> **Request headers (only) of a URL**
>
> **Characteristics**:
> - Identical to GET but without response body
> - Used to check if resource exists
> - Check resource metadata (size, modification date)
> - Verify links without downloading content
> - Test server availability
>
> **Example**:
> ```
> HEAD /largefile.zip HTTP/1.1
> Host: www.example.com
> ```

> [!info]+ PUT
> **Replace file/object at specified URL with content in entity body**
>
> **Characteristics**:
> - Uploads or updates a resource
> - Idempotent (same request multiple times = same result)
> - Creates resource if doesn't exist
> - Updates resource if exists
> - Full replacement of resource
>
> **Example**:
> ```
> PUT /api/users/123 HTTP/1.1
> Host: www.example.com
> Content-Type: application/json
> {"username":"john_updated","email":"new@example.com"}
> ```

> [!info]+ DELETE
> **Remove a resource at the specified URL**
>
> **Characteristics**:
> - Deletes specified resource
> - Idempotent
> - May not be immediately executed
>
> **Example**:
> ```
> DELETE /api/users/123 HTTP/1.1
> Host: www.example.com
> ```
## Common Request Headers
> [!note]+ Host Header (Required in HTTP/1.1)
>
> ```
> Host: www.example.com
> ```
>
> - Specifies domain name and port
> - Required for virtual hosting
> - Allows multiple domains per IP address

> [!note]+ User-Agent
>
> ```
> User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
> ```
>
> - Identifies client software
> - Browser type and version
> - Operating system
> - Used for analytics and compatibility

> [!note]+ Accept Headers
>
> ```
> Accept: text/html,application/xhtml+xml
> Accept-Language: en-us,en;q=0.5
> Accept-Encoding: gzip,deflate
> Accept-Charset: ISO-8859-1,utf-8;q=0.7
> ```
>
> - **Accept**: Content types client can process
> - **Accept-Language**: Preferred languages
> - **Accept-Encoding**: Supported compression methods
> - **Accept-Charset**: Character encodings

> [!note]+ Connection Management
>
> ```
> Connection: keep-alive
> Keep-Alive: timeout=5, max=100
> ```
>
> - Controls connection persistence
> - `keep-alive`: Use [[Persistent HTTP]]
> - `close`: Close after response

> [!note]+ Content Headers (for POST/PUT)
>
> ```
> Content-Type: application/json
> Content-Length: 1234
> Content-Encoding: gzip
> ```
>
> - **Content-Type**: Format of body data
> - **Content-Length**: Size of body in bytes
> - **Content-Encoding**: Body compression

> [!note]+ Caching Headers
>
> ```
> If-Modified-Since: Wed, 21 Oct 2025 07:28:00 GMT
> If-None-Match: "686897696a7c876b7e"
> Cache-Control: no-cache
> ```
>
> - Support [[Conditional GET]]
> - Cache validation
> - See [[Conditional GET]] for details

> [!note]+ Authentication
>
> ```
> Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
> Cookie: sessionid=abc123; userid=456
> ```
>
> - Authentication credentials
> - Session tokens
> - Cookies for state management
## Related Concepts
> [!note]+ See Also
> - **[[HTTP response message]]**: Server's reply to requests
> - **[[HTTP]]**: Main protocol overview
> - **[[Conditional GET]]**: Efficient caching with If-Modified-Since
> - **[[HTTP 1.1]]**: Protocol version defining these methods
> - **[[HTTP 2]]**: Binary framing of these messages
> - **[[TCP]]**: Underlying transport for message delivery

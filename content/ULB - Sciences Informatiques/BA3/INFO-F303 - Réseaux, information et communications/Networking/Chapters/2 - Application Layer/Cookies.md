---
title: Cookies
authors: Alessandro Dorigo
tags:
  - Network
---


> [!info]+ Definition
> **Cookies** are used by websites and browsers to maintain state between [[HTTP]] transactions (since HTTP is stateless).

> [!abstract]- Common Applications
> - **Session management**: Login sessions, shopping carts
> - **Personalization**: User preferences, themes
> - **Tracking**: User behavior, analytics
## Four Components
> [!abstract]- Cookie System Components
> 1. **Cookie header line in [[HTTP response message]]**
> 2. **Cookie header line in [[HTTP request message]]**
> 3. **Cookie file kept on user's host**, managed by browser
> 4. **Backend database at website** storing user information
## How Cookies Work
> [!example]+ Example Flow
> Susan visits e-commerce site for first time:
>
> **First Visit**:
> - Initial HTTP request arrives at site
> - Site creates unique ID (cookie) and entry in backend database
>
> **Subsequent Visits**:
> - Browser sends cookie ID in HTTP request
> - Site uses ID to identify Susan and retrieve her data
>
> ![[Pasted image 20251020134337.png]]
## Cookie Headers
> [!note]+ HTTP Headers
> **Server sets cookie** (in response):
> ```
> Set-Cookie: id=1234
> ```
>
> **Client sends cookie** (in request):
> ```
> Cookie: id=1234
> ```

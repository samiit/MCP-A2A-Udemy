# MCP server and client

## Server setup
With latest version of `fastmcp 3.x.x` version, we need to fix the imports

```python
from fastmcp.server.server import FastMCP
```

### Transport methods
It's like the highway between server and client
Afterwards, when running the server, we need to specify `transport` protocol as one of:
1. http
2. stdio
    - fine for local development/testing
    - never for production
3. sse
    - server sent events
    - eventloop type
        - server keeps pushing updates to the client, streaming
        - client communicates via POST request, discretely
    - default until May 2025; now deprecated
    - highly criticized by the community
    - Pros:
        - supports advanced use cases, e.g., sampling
    - Cons:
        - not possible serverless, horizontal scaling (kubernettes)
4. streamable-http
    - fully stateless MCP servers
        - every request contains all data necessary for running; server doesn't need to keep any session data/state from previous requests!
    - can switch to stateful mode, when needed!
    - good for serverless, or horizontal scaling

### Shell call to an MCP server
Need 3 calls:
1. Initialize - returns a session ID
2. Notifications - notifications/initialized sets up the incoming and outgoing streams of transport
3. Call the specific tool - can also be things other than tools. Here is where you call the specific function defined in the MCP server
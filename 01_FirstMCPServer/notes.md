# MCP server and client

## Server setup
With latest version of `fastmcp 3.x.x` version, we need to fix the imports

```python
from fastmcp.server.server import FastMCP
```

Afterwards, when running the server, we need to specify `transport` protocol as one of:
1. http
2. stdio
3. sse
4. streamable-http

## Shell call to an MCP server
Need 3 calls:
1. Initialize - returns a session ID
2. Notifications - notifications/initialized sets up the incoming and outgoing streams of transport
3. Call the specific tool - can also be things other than tools. Here is where you call the specific function defined in the MCP server
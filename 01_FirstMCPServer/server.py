"""FastMCP demo server"""

from fastmcp.server.server import FastMCP

mcp = FastMCP("Demo Server")


@mcp.tool(description="Add two integers")
def add(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    mcp.run(transport="streamable-http")

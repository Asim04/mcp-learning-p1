
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP(name="My FastMCP Server", stateless_http=True) # when true we dont need handshake or inilitaze thing. Enable stateless HTTP mode!  when stateless_http is True,  FastMCP will not maintain any session state for HTTP requests, making it more scalable and suitable for serverless environments.

mcp_app = mcp.streamable_http_app() # Enable streamable HTTP app mode! when streamable_http_app is True, FastMCP will allow streaming responses for HTTP requests, enabling real-time data delivery and improved performance for long-running tasks.


# Add Greeting tool in the tools directory
@mcp.tool(name="greet", description="Greet the user with a message")
def greet(name: str) -> str:
    return f"Hello, {name}! Welcome to FastMCP!"

# Add another tool for adding two numbers
@mcp.tool(name="add", description="Add two numbers")
def add(a: int, b: int) -> int:
    return a + b    

# add another tools for weather information
@mcp.tool(name="weather", description="Get weather information for a city")
def weather(city: str) -> str:
    # For demonstration purposes, we'll return a static weather report
    return f"The current weather in {city} is sunny with a temperature of 25°C."     


# Define a simple handler for incoming messages
# @mcp.on_message()
# def handle_message(message):
#     print(f"Received message: {message}")
#     return f"Echo: {message}"c
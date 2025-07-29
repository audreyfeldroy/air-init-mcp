from fastmcp import FastMCP
import air
from fastapi import FastAPI

app = air.Air()
api = FastAPI()



@app.page
def index():
    return air.layouts.picocss(
        air.H1('Hello, world'),
        air.P(air.A('Go to API root', href='/api')),
        air.P(air.A('Go to MCP', href='/api')),

    )

@api.get('/')
def root():
    return {'root': 'all roads lead here'}


app.mount("/api", api) 
mcp = FastMCP.from_fastapi(app=app)


@mcp.tool
def greet(name: str) -> str:
    """Greet the user with their name."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    mcp.run()

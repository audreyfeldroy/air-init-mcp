import air
from .cli import app as cli_app

app = air.Air()

@app.get("/")
async def index():
    return air.Html(air.H1("Welcome to Air Init MCP!", style="color: blue;"))


if __name__ == "__main__":
    cli_app()

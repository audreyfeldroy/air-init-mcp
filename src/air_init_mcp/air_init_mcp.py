"""Main module."""
from cookiecutter.main import cookiecutter
from fastmcp import FastMCP

mcp = FastMCP("Air Init MCP Server")


@mcp.tool
def greet(name: str) -> str:
    """Greet the user with their name."""
    return f"Hello, {name}!"


@mcp.tool
def air_init(domain_name: str) -> str:
    """Initialize a new Air project."""
    cookiecutter(
        template="https://github.com/audreyfeldroy/cookiecutter-pypackage",
        extra_context={"pypi_package_name": domain_name},
    )
    return f"Air project '{domain_name}' initialized successfully."


@mcp.tool
def air_init(pypi_package_name: str) -> str:
    """Initialize a new Air package."""
    cookiecutter(
        template="https://github.com/audreyfeldroy/cookiecutter-pypackage",
        extra_context={"pypi_package_name": pypi_package_name},
    )
    return f"Air package '{pypi_package_name}' initialized successfully."


if __name__ == "__main__":
    mcp.run(host="127.0.0.1", port=4200,)

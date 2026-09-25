from typing import Any, Dict
from mcp.server.fastmcp import FastMCP
import json

# Initialize FastMCP server
mcp = FastMCP(
    name="circuits-mcp-server",
    host="0.0.0.0",
    port=8000
)

@mcp.tool(
    name="get_circuits_by_Billing_number",
    description="Get circuits info based on the Billing_number provided by the user.",
    structured_output=True
)
def get_circuit(name: int | str) -> Dict[str, Any]:
    with open("circuits.json", "r") as file:
        circuits = json.load(file)
    for circuit in circuits:
        if circuit["name"].lower() == name.lower():
            return circuit
    return {"error": "circuit not found"}


@mcp.tool(
    name="get_circuits_by_id",
    description="Get circuits info based on the ID provided by the user.",
    structured_output=True
)
def get_circuit_by_id(id: int | str) -> Dict[str, Any]:
    with open("circuits.json", "r") as file:
        circuits = json.load(file)
    for circuit in circuits:
        if circuit["id"] == id:
            return circuit
    return {"error": "circuit not found"}


if __name__ == "__main__":
    mcp.run(transport="streamable-http", mount_path="/mcp")

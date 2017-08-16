from webiopi.devices.analog import MCP3208
mcp = MCP3208()
print mcp.analogReadAllVolt()
# Set up GPIO library
import webiopi
GPIO = webiopi.GPIO

# Syntax to import the MCP23S17 I/O expander chip.
# documentation on webiopi.trouch.com is not up to date.
from webiopi.devices.digital.mcp23XXX import MCP23S17

# Define the CS pin and hardware address (A0, A1, A2 all grounded)
mcp0 = MCP23S17( chip=0, slave=0x20 )

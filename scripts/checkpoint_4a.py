# Imports
import webiopi
from webiopi.devices.digital import PCF8574A
mcp = PCF8574A(slave=0x38)

# Retrieve GPIO lib
GPIO = webiopi.GPIO

LED0 = 0 # Set which PCF8574 GPIO pin is connected to the LED (negative logic)

# Setup GPIOs
mcp.setFunction(LED0, 0) #Set Pin as output

# Turn on the LED for the first time
mcp.digitalWrite(LED0, GPIO.LOW)
 
# Loop for ever
#    Insert your code here
# Include a delay 
webiopi.sleep(0.10)

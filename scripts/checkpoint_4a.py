# Imports
import webiopi
import time
from webiopi.devices.digital.pcf8574 import PCF8574A

# Retrieve GPIO lib
GPIO = webiopi.GPIO

# Setup chip
mcp = PCF8574A(slave=0x38)

# Set which PCF8574 GPIO pin is connected to the LED (negative logic)
LED0 = 0

# Setup GPIOs
mcp.setFunction(LED0, GPIO.OUT) #Set Pin as output

# Turn on the LED for the first time
mcp.digitalWrite(LED0, GPIO.LOW)
 
# Loop for ever
#    Insert your code here
# Include a delay 
time.sleep(0.10)

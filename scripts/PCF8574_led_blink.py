#Written by G. Sidiropoulos
#The following simple code utilizes the PCF8574A GPIO Expander
#The code toggles the state of the LED in time interval defined in the sleep method

# Imports
import webiopi
from webiopi.devices.digital import PCF8574A
mcp = PCF8574A(slave=0x38)

GPIO = webiopi.GPIO

LED0 = 0 # Set which PCF8574 GPIO pin is connected to the LED (negative logic)


# Setup GPIOs
mcp.setFunction(LED0, 0) #Set Pin as output


mcp.digitalWrite(LED0, GPIO.LOW) #Turn on the LED for the first time

# Loop for ever
while True:
    #Read the value of the LED, invert it and save it to variable value
    value = not mcp.digitalRead(LED0)
    #Write variable value to the LED
    mcp.digitalWrite(LED0, value)
    webiopi.sleep(0.05) #Delay 



# Import webIOPi
import webiopi

# Make a GPIO object
GPIO = webiopi.GPIO

# Set which GPIO pin is connected to the LED
LED0 = 24 

# Set which GPIO pin is connected to the switch
SWITCH0 = 23 

# Setup GPIOs
GPIO.setFunction(LED0, GPIO.OUT) # Set Pin as output
GPIO.digitalWrite(LED0, GPIO.HIGH) # Turn on the LED 
GPIO.digitalWrite(LED0, GPIO.LOW) # Turn off the LED 

# Loop for ever
while True:

# Read the switch and if it is pressed toggle the state of the LED
	if (GPIO.digitalRead(SWITCH0) == GPIO.LOW):

# Read the value of the LED, invert it and save it to variable value
# Write variable value to the LED
		value = not GPIO.digitalRead(LED0)
		GPIO.digitalWrite(LED0, value)

# Wait		
	webiopi.sleep(1)






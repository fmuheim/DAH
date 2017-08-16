# Import webIOPi
import webiopi

# Make a GPIO object
GPIO = webiopi.GPIO

# Set which GPIO pin is connected to the LED
LED0 = 24 

# Setup GPIOs
GPIO.setFunction(LED0, GPIO.OUT) # Set Pin as output
GPIO.digitalWrite(LED0, GPIO.HIGH) # Turn on the LED 
GPIO.digitalWrite(LED0, GPIO.LOW) # Turn off the LED 

# Loop for ever
while True:

# Toggle LED after time in seconds as defined inside sleep method
	value = not GPIO.digitalRead(LED0)
	GPIO.digitalWrite(LED0, value)
	webiopi.sleep(2)


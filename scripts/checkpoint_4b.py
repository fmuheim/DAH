# Loop for ever
while True:
    # Read the switch and if it is pressed toggle the state of the LED
    if (mcp.digitalRead(SWITCH0) == GPIO.HIGH):
        # Insert your code here

        # dummy write to reset switch register
        mcp.digitalWrite(SWITCH0, GPIO.LOW)

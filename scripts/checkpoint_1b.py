# Loop for ever
while True

# Toggle LED after time in seconds as defined inside sleep method
value = not GPIO.digitalRead(LED0)
GPIO.digitalWrite(LED0, value)
webiopi.sleep(2)

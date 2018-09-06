import time

# Loop for ever
while True:

# Toggle LED after time in seconds as defined inside sleep method
    value = not GPIO.input(LED0)
    GPIO.output(LED0, value)
    time.sleep(2)

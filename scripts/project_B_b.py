# open the serial port with baud rate 115200bps
# this is the rate used by the Arduino microcontroller
# Arduino will be on port ttyACM0 by default
import serial
ser=serial.Serial('/dev/ttyACM0',115200, timeout=5)  

# a small delay may be necessary to give the microcontroller time to respond
# you may want to experimentally find the shortest delay that makes the code work
time.sleep(1)

# clear the serial port buffer
# this is sometimes required to properly initialize communication between R-Pi and Arduino
ser.flushInput()  

# a small delay may be necessary to give the microcontroller time to respond
# you may want to experimentally find the shortest delay that makes the code work
time.sleep(1)

# send desired sampling frequency to Arduino and order it to begin sampling
# the first value can be anything between 4 and 255. The larger the value the slower the sampling will be
# the second value should always be 2
ser.write(bytes([4,2]))

# a small delay may be necessary to give the microcontroller time to respond
# you may want to experimentally find the shortest delay that makes the code work
time.sleep(1)

# read data sample from Arduino ADC (1024 bytes, 8-bit resolution)
data=ser.read(1024)

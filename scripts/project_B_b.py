# open the serial port with baud rate 115200bps
import serial
ser=serial.Serial('/dev/ttyACM0',115200)  

# send desired sampling frequency to Arduino and order it to begin sampling
ser.flushInput()  # clear the serial port buffer
ser.write( '\x04\x02')  # the first byte can be anything between 4 and 255. 

# The larger the value the slower the sampling will be
# read data sample from Arduino ADC (1024 bytes, 8-bit resolution)
data=ser.read(1024)

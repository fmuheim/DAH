# instruction for ADC to measure a voltage sample

import spidev
spi=spidev.SpiDev()	# initialization
spi.open(0,0)     	# opens the port
spi.max_speed_hz=1000000 	# sets the clock speed to 1MHz = max 

# recommended for VDD=3.3V
# to read ADC output
adc=spi.xfer2([6,0,0]) 	# read voltage from CH0 of MCP3208   
# after executing this commabd, "adc" will be an array of three bytes,
# where the 2nd and 3rd will hold the output of the ADC

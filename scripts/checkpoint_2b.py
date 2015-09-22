# Import ADC and DAC chip libraries
from webiopi.devices.analog import MCP3208, MCP4922
 
# Define DAC on Chip Enable 1 (CE1/GPIO7)
DAC1 = MCP4922(chip=1)

# Output 1.3V on channel 0 of DAC1
print 'output 1.3V on channel 0 of DAC1'
DAC1.analogWriteVolt(0, 1.3)

# Print value of channel 0 of DAC1
print 'value of register for channel 0 of DAC1'
print DAC1.analogReadVolt(0)


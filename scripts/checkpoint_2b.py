# Import DAC chip libraries
from webiopi.devices.analog.mcp492X import MCP492X

# Define DAC on Chip Enable 1 (CE1/GPIO7)
DAC1 = MCP492X(chip=1, channelCount=2, vref=3.3)

# Output 1.3V on channel 0 of DAC1
print ('output 1.3V on channel 0 of DAC1')
DAC1.analogWriteVolt(0, 1.3)

# Print value of channel 0 of DAC1
print ('value of register for channel 0 of DAC1')
print (DAC1.analogReadVolt(0))


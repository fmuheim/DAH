# Find out the current time
import datetime
datetime.datetime.now()

# Make a list from a measurement, add another measurement
# to the end of the list
someData = [ oneMeasurement ]
someData.append( anotherMeasurement )

# Pylab makes graph plotting very easy:
import pylab
pylab.ion()                             # Turns interactive mode on
pylab.plot( someXValues, someYValues )  # Make an xy plot
pylab.draw()                            # Display the current plot
pylab.clf()                             # Clear the display

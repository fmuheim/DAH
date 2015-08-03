#===========================================================
# This is somewhat more scientifically orented code to show you examples of things
# you might want to do.

# pylab has a LOT of useful things in it.  Google for it.
import pylab
# numpy is the fundamental package for scientific computing with Python. Google for it.
import numpy as np



#==========================================================
# Create lists of x, y
#  - the x values
#  - the y values

x = np.linspace(-10, 10, 100)  # 100 evenly-spaced values from -10 to 10
p = np.poly1d([1, 0, 0])       # Polynomial y = x^2 + 0x + 0 
y = p(x)                       # where y = f(x) is a polymonial, e.g. y = x^2

print x, y



#==========================================================
# Plot x against y using pylab plotting facilities
# Google for customizing the plot.

pylab.plot(x, y)
pylab.xlabel('x values')
pylab.ylabel('y values')
pylab.title('This is the title')
pylab.grid(True)
pylab.savefig("test.pdf")
pylab.show()




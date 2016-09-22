from numpy import matrix

import pylab as pl

import numpy as np


#==========================================================
#  Class to evaluate y = mx + c

class Linear:
    
    # Constructor, sets m=0, c=1.
    def __init__(self ):
        self.m     = 0.0
        self.c     = 1.0
    
    # This method assigns m and c
    def set_elements(self, parameters):
        if (len(parameters) != 2):
            print 'Invalid parameters - m and c must be specified'
        
        self.m = float(parameters[0])
        self.c = float(parameters[1])
    
    # This is the evaluate method for a single data point.
    def eval(self, x):
        return self.m*x + self.c
    
    # Here we vectorize a function.  Having defined a function eval which acts on a scalar
    # (i.e number) and returns a scalar, vecfn = vectorize(eval) gives us a function vecfn which
    # will act on np.arrays or matrices and returns a np.array or matrix in which "out_array[i]"
    # is "eval(in_array[i])" **(pseudocode)**.
    def veval(self, j):
        vecfn  = np.vectorize(self.eval)
        return vecfn(j)



#==========================================================
# Create three row vectors (i.e. 1 dimensional matrices) which contain
#  - the x values
#  - the y values
#  - the errors

xvals = matrix( ' 1, 2, 3, 4, 5, 6 ,7, 8 , 9, 10')
yvals = matrix( ' 1.05, 0.93, 0.99, 1.06, 0.94, 1.08 ,1.01, 0.89 , 0.95, 1.03')
evals = matrix( ' 0.03, 0.04, 0.02, 0.02, 0.01, 0.03 ,0.02, 0.04 , 0.025, 0.03')

npts =  xvals.size

print xvals
print yvals
print evals


#==========================================================
# Plot x against y using pylab.

pl.plot( xvals, yvals, 'yo-')
pl.xlabel('x values')
pl.ylabel('y values')
pl.title('About as simple as it gets, folks')
pl.grid(True)
#savefig("test.png")
pl.show()


#=============================================================
# Now make a chis-squared for a given value of m and c

ytheory = matrix(np.zeros( (1, xvals.size) ) )

m = 0.
c = 1.0
aline = Linear()
aline.set_elements( [m,c] )


for i in range(0,npts):
    x = xvals[0,i]
    y = aline.eval(x)
    ytheory[0,i] = y

print ytheory


errormatrix = matrix( np.zeros( (npts, npts) ) )
for i in range(0,npts):
    errormatrix[i,i] = evals[0,i]**2

print errormatrix.I


ydifference = yvals - ytheory

chisq = ydifference * errormatrix.I * ydifference.T

print chisq

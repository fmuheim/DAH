#===========================================================
# This is somewhat more scientifically orented code to show you examples of things
# you might want to do.

# pylab has a LOT of useful things in it.  Google for it.
import pylab as pl


#==========================================================
#  Class to evaluate y = mx + c

class Linear:
    
    # Constructor, sets m=0, c=1.
    def __init__(self ):
        self.m     = 0.0
        self.c     = 1.0
    
    # This method sets m and c
    def setParameters(self, parameters):
        if (len(parameters) != 2):
            print 'Invalid parameters - m and c must be specified'
        
        self.m = float(parameters[0])
        self.c = float(parameters[1])
    
    # This is the evaluate method for a single data point.
    def eval(self, x):
        return self.m*x + self.c
    



#==========================================================
# Create three lists of x,y measurements plus the error on the measurement of y
#  - the x values
#  - the y values
#  - the errors

xvals = [ 1, 2, 3, 4, 5, 6 ,7, 8 , 9, 10 ]
yvals = [ 1.05, 0.93, 0.99, 1.06, 0.94, 1.08 ,1.01, 0.89 , 0.95, 1.03 ]
evals = [ 0.03, 0.04, 0.02, 0.02, 0.01, 0.03 ,0.02, 0.04 , 0.025, 0.03 ]


print xvals
print yvals
print evals



#==========================================================
# Plot x against y using pylab plotting facilities

pl.plot( xvals, yvals, 'yo')    # 'yo'  means yellow and use circles as the data points.
pl.xlabel('x values')
pl.ylabel('y values')
pl.title('This is the title')
pl.grid(True)
#savefig("test.png")
#pl.show()




#==========================================================
# Make a corresponding set of y = mx+c points from theory and add them to the plot

#Make an empty list of theory points
ytheory = []

# create an instance of a linear function
theoryFunction = Linear()
theoryFunction.setParameters( [0.01,0.9])

#calculate 10 theory points
for i in range(0,len(xvals)):
    x = xvals[i]
    y = theoryFunction.eval(x)
    ytheory.append(y)

print ytheory

#add them to the plot
pl.plot( xvals, ytheory, 'r.-')
pl.show()



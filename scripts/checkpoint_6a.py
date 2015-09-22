# Import
# pylab has a LOT of useful things in it.
import pylab

# numpy is the fundamental package for scientific computing with Python.
import numpy as np

# Make a histogram with arrays of nr. of entries and of bin edges
entries, binedges, patches = pylab.hist(xmass, bins = Nbins, range = [binMin,binMax])

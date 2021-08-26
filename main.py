from numpy import random
from matplotlib import pyplot
x = random.rand(50)
c = random.rand(50)
pyplot.plot(x, 2*x+c, 'o')
pyplot.show()

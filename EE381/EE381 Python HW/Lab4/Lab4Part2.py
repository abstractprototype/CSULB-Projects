import math
import numpy
import matplotlib
import matplotlib.pyplot

def createGraph(urv: int, a: int, b: int, mu: int, sig: int, nbooks: int):

   # Setup the graph
   edgecolor='w'
   bins = [float(x) for x in numpy.linspace(nbooks * a, nbooks * b, 51)]
   h1, bin_edges = numpy.histogram(urv, bins, density=True)
   be1 = bin_edges[0:numpy.size(bin_edges) - 1]
   be2 = bin_edges[1:numpy.size(bin_edges)]
   b1 = (be1 + be2) / 2
   barwidth = b1[1] - b1[0]
   matplotlib.pyplot.close('all')
 
   # Plot the graph
   matplotlib.pyplot.bar(b1, h1, width=barwidth, edgecolor=edgecolor)
   matplotlib.pyplot.title('PDF of book stack height and comparison with Gaussian')
   matplotlib.pyplot.xlabel('Book stack height for n = %d books' % (nbooks))
   matplotlib.pyplot.ylabel('Probability Density Function')
 
   # Generate normal pdf
   m = mu * nbooks
   s = sig * numpy.sqrt(nbooks)
   f = numpy.exp(-(b1 - m) ** 2 / (2 * s ** 2)) / (s * numpy.sqrt(2 * numpy.pi))

   #Plot the gaussian function
   matplotlib.pyplot.plot(b1, f, 'r')
   matplotlib.pyplot.show()

def generateValues(a: int, b: int, nbooks: int, n=10000):
    z = numpy.zeros((n, 1))

    for k in range(0, n):
       x = numpy.random.uniform(a, b, nbooks)
       w = numpy.sum(x)
       z[k] = w

    return z

def part2(a: float = 1.0, b: float = 4.0):

   # Calculate the theoretical mean and std
   # Generate the values of the RV X
   mu_x = (a + b) / 2
   sig_x = numpy.sqrt((b - a) ** 2 / 12)
 
   print('Mean from thickness: %f\nStd. Dev. from thickness: %f\n' % (mu_x, sig_x))
 
   # Plot graph for 1 book stack
   nbooks = 1
   urv = generateValues(a, b, nbooks)
   createGraph(urv, a, b, mu_x, sig_x, nbooks)
 
   # Plot graph for 5 book stack
   nbooks = 5
   urv = generateValues(a, b, nbooks)
   createGraph(urv, a, b, mu_x, sig_x, nbooks)
 
   # Plot graph for 15 book stack
   nbooks = 15
   urv = generateValues(a, b, nbooks)
   createGraph(urv, a, b, mu_x, sig_x, nbooks)
 
   print(f'Mean n=1: {mu_x}\nStd.Dev n=1: {sig_x}')
   print(f'Mean n=5: {mu_x * 5}\nStd.Dev n=5: {sig_x * numpy.sqrt(5)}')
   print(f'Mean n=10: {mu_x * 10}\nStd.Dev n=10: {sig_x * numpy.sqrt(10)}')
   print(f'Mean n=15: {mu_x * 15}\nStd.Dev n=15: {sig_x * numpy.sqrt(15)}')

if __name__ == '__main__':

    print('Part 2')
    part2()
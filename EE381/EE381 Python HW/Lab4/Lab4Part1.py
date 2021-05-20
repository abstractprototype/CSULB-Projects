import math
import numpy
import matplotlib
import matplotlib.pyplot

def part1(a: float = 1.0, b: float = 4.0, n: int = 10000):
    #Generate values of the RV X
    x = numpy.random.uniform(a, b, n) 

    #Get experimental mean and standard deviation
    mu_x = numpy.mean(x)
    sig_x = numpy.std(x)

    #Get theoretical mean and standard deviation
    theomux = (a+b) / 2
    theosigx = (abs(b-a) ** 2) / 12

    print('Mean from experimental: %f\nStd. Dev. from experimental: %f\n' % (mu_x, sig_x))
        
    print('Mean from theoretical: %f\nStd. Dev. from theoretical: %f\n' % (theomux, theosigx))

    # The plot variables
    edgecolor='w'
    bins = [float(i) for i in numpy.linspace(a, b, 31)]
    h1, bin_edges = numpy.histogram(x, bins, density=True)
    be1 = bin_edges[0:numpy.size(bin_edges) - 1]
    be2 = bin_edges[1:numpy.size(bin_edges)]
    b1 = (be1 + be2) / 2
    barwidth = b1[1] - b1[0]
    matplotlib.pyplot.close('all')
    
    # Plot the graph
    figure1 = matplotlib.pyplot.figure(1)
    matplotlib.pyplot.bar(b1, h1, width=barwidth, edgecolor=edgecolor)
    matplotlib.pyplot.title('PDF and Random Variable with Uniform Distribution')
    matplotlib.pyplot.xlabel('Random Variable X with Uniform Distribution')
    matplotlib.pyplot.ylabel('PDF')
    
    #Plot the uniform Probabiliy Density Function
    size = numpy.size(b1)
    f = (1 / abs(b - a)) * numpy.ones(size)
    matplotlib.pyplot.plot(b1, f, 'r')
    matplotlib.pyplot.show()
    figure1.savefig('Part1.1.jpg')

def part12(beta: int = 40, n: int = 10000):
    #random variable T with an exponential distribution
    t = numpy.random.exponential(beta, n)

    #Get experimental mean of the RV
    expMean = numpy.mean(t)
    std = numpy.std(t)

    print('Mean from experimental: %f\nStd. Dev. from experimental: %f\n' % (expMean, std))
        
    print('Mean from theoretical: %f\nStd. Dev. from theoretical: %f\n' % (beta, beta))
         
    # The plot variables
    edgecolor='w'
    bins = [float(t) for t in numpy.linspace(0, 200, 51)]
    h1, bin_edges = numpy.histogram(t, bins, density=True)
    be1 = bin_edges[0:numpy.size(bin_edges) - 1]
    be2 = bin_edges[1:numpy.size(bin_edges)]
    b1 = (be1 + be2) / 2
    barwidth = b1[1] - b1[0]

    # Plot the graph
    matplotlib.pyplot.close('all')
    matplotlib.pyplot.bar(b1, h1, width=barwidth, edgecolor=edgecolor)
    matplotlib.pyplot.title('PDF and Random Variable with Exponential Distribution')
    matplotlib.pyplot.xlabel('Random Variable X with Exponential Distribution')
    matplotlib.pyplot.ylabel('Probabily Density Function')
    
    #Plot the probability density function for the RV
    f = numpy.ones(numpy.size(b1))
    for i in range(numpy.size(b1)):
        f[i] = (1 / abs(beta)) * math.exp(-b1[i] / abs(beta))
 
    matplotlib.pyplot.plot(b1, f, 'r')
    matplotlib.pyplot.show()

def part13(mu: float = 2.5, sigma: float = 0.75, n: int = 10000):
    #Generate values of RV x
    x = numpy.random.normal(mu, sigma, n)

    # Get the experimental mean and std
    mu_x = numpy.mean(x)
    sig_x = numpy.std(x)
    
    print('Mean from experimental: %f\nStd. Dev. from experimental: %f\n' % (mu_x, sig_x))
            
    print('Mean from theoretical: %f\nStd. Dev. from theoretical: %f\n' % (mu, sigma))
            
    # Setup graph
    edgecolor='w'
    bins = [float(x) for x in numpy.linspace((mu - (4 * sigma)), (mu + (4 * sigma)), 51)]
    h1, bin_edges = numpy.histogram(x, bins, density=True)
    be1 = bin_edges[0:numpy.size(bin_edges) - 1]
    be2 = bin_edges[1:numpy.size(bin_edges)]
    b1 = (be1 + be2) / 2
    barwidth = b1[1] - b1[0]
    matplotlib.pyplot.close('all')
    
    # Plot graph
    matplotlib.pyplot.bar(b1, h1, width=barwidth, edgecolor=edgecolor)
    matplotlib.pyplot.title('PDF and Random Variable with Normal Distribution')
    matplotlib.pyplot.xlabel('Random Variable X with Normal Distribution')
    matplotlib.pyplot.ylabel('Probability Density Function')

    # Plot the probability density function for the RV
    f = numpy.ones(numpy.size(b1))
    for i in range(numpy.size(b1)):
        f[i] = (1 / (sigma * (math.sqrt(2 * math.pi)))) * math.exp(-(((b1[i] - mu) ** 2) / (2 * (sigma ** 2))))
            
    matplotlib.pyplot.plot(b1, f, 'r')
    matplotlib.pyplot.show()



if __name__ == '__main__':
    print('Part 1.1: ')
    part1()

    print('Part 1.2: ')
    part12()

    print('Part 1.3: ')
    part13()





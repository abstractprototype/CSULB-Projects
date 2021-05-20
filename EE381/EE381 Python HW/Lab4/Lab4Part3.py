import math
import numpy
import matplotlib
import matplotlib.pyplot

def part3(beta: int = 40, n: int = 10000):
    x = numpy.zeros((n, 1))
    #Repeat experiment 10000 times
    for i in range(n):
        # Carton size is 24
        carton = numpy.zeros(24)
        # Generate exponential distribution
        for k in range(0, 24):
            t = numpy.random.exponential(beta)
            carton[k] = t

        #Sum of the elements of vector is a random variable
        t = numpy.sum(carton)
        x[i] = t

    # calculate mean and std
    mu_x = numpy.mean(x)
    sig_x = numpy.std(x)

    print('Mean: %f\nStd.Dev: %f\n' % (mu_x, sig_x))
    normDist = numpy.random.normal(mu_x, sig_x, n)
 
    # Setup the graph
    edgecolor='w'
    bins = [float(x) for x in numpy.linspace(0, 2000, 101)]
    h1, bin_edges = numpy.histogram(normDist, bins, density=True)
    be1 = bin_edges[0:numpy.size(bin_edges) - 1]
    be2 = bin_edges[1:numpy.size(bin_edges)]
    b1 = (be1 + be2) / 2
    barwidth = b1[1] - b1[0]
    matplotlib.pyplot.close('all')

    # Plot the graph
    figure1 = matplotlib.pyplot.figure(1)
    matplotlib.pyplot.bar(b1, h1, width=barwidth, edgecolor=edgecolor)
    matplotlib.pyplot.title('PDF and Random Variable with Battery Normal Distribution')
    matplotlib.pyplot.xlabel('Battery Lifetime RV in days')
    matplotlib.pyplot.ylabel('PDF')
   

    # Calculate the norm pdf
    # f = numpy.ones(numpy.size(b1))
    # for i in range(numpy.size(b1)):
    #     f[i] = (1 / (sig_x * (math.sqrt(2 * math.pi)))) * \
    #         math.exp(-(((b1[i] - mu_x) ** 2) / (2 * (sig_x ** 2))))
    f = (1 / (sig_x * numpy.sqrt(2 * numpy.pi))) * numpy.exp(-(((b1 - mu_x) ** 2) / (2 * (sig_x ** 2)))) * numpy.ones(numpy.size(b1))
    
    matplotlib.pyplot.plot(b1, f, 'r')
    matplotlib.pyplot.show()
    figure1.savefig('Figure1.jpg')

    # Calculate CDF
    tempPDF = numpy.zeros(numpy.size(f))
    for i in range(numpy.size(f)):
        tempPDF[i] = f[i] * barwidth
    cdf = numpy.cumsum(tempPDF)
 
    # Plot cdf figure
    figure2 = matplotlib.pyplot.figure(2)
    matplotlib.pyplot.plot(b1, cdf, 'b')
    matplotlib.pyplot.title('CDF for Battery Normal Distribution')
    matplotlib.pyplot.xlabel('Battery Lifetime in days')
    matplotlib.pyplot.ylabel('CDF')
    matplotlib.pyplot.show()
    figure2.savefig('Figure 2')


if __name__ == '__main__':
    print('Part 3: ')
    part3()


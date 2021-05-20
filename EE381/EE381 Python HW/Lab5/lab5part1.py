import numpy
import random
import matplotlib.pyplot 

N = 1500000   # total number of bearings
mu_x = 55  # population mean
sig_x = 5  # pupulation standard deviation

def interval(n):

    # 95% CONFIDENCE INTERVAL
    #Make lists to store values of x, upper bound, and lower bound
    xlist = []        
    upper_bound = []     
    lower_bound = []     

    rand = numpy.random.normal(mu_x, sig_x, N)

    #Generate all the x's
    for i in range(n):
        if i == 0:
            i += 1
        x = rand[random.sample(range(N), i)]
        xbar = numpy.mean(x)
        xlist.append(xbar) #adds to the list of x_list
        a = mu_x + 1.96 * (sig_x / numpy.sqrt(i)) # calculate the 95% confidence upper interval
        b = mu_x - 1.96 * (sig_x / numpy.sqrt(i)) # calculate the 95% confidence lower interval
        upper_bound.append(a)  # add upper/lower limits values into list
        lower_bound.append(b)  

    #Make scatterplot
    bonk = list(range(1, n + 1))
    matplotlib.pyplot.scatter(bonk, xlist, color='b', marker='x', label='xlist')
    matplotlib.pyplot.title('Sample means and 95% confidence interval')
    matplotlib.pyplot.xlabel('Sample size of %d' % n)
    matplotlib.pyplot.ylabel('xbar')
    matplotlib.pyplot.plot(upper_bound, 'r--', label='Upper bound')
    matplotlib.pyplot.plot(lower_bound, 'r--', label='Lower bound')
    matplotlib.pyplot.legend()
    matplotlib.pyplot.show()




    # 99% CONFIDENCE INTERVAL
    #Make lists to store values of x, upper bound, and lower bound
    xlist = []         
    upper_bound = []     
    lower_bound = []     

    rand = numpy.random.normal(mu_x, sig_x, N)

    #Generate all the x's
    for i in range(n):
        if i == 0:
            i += 1
        x = rand[random.sample(range(N), i)]
        xbar = numpy.mean(x)
        xlist.append(xbar) #adds value to x_list
        a = mu_x + 2.58 * (sig_x / numpy.sqrt(i)) # calculate the 99% confidence upper interval
        b = mu_x - 2.58 * (sig_x / numpy.sqrt(i)) # calculate the 99% confidence lower interval
        upper_bound.append(a)  # add upper/lower limits values into list
        lower_bound.append(b) 

    #Make the scatterplot
    bonk = list(range(1, n + 1))
    matplotlib.pyplot.scatter(bonk, xlist, color='b', marker='x', label='xlist')
    matplotlib.pyplot.title('Sample means and 99% confidence interval')
    matplotlib.pyplot.xlabel('Sample size of %d' % n)
    matplotlib.pyplot.ylabel('xbar')
    matplotlib.pyplot.plot(upper_bound, 'g--', label='Upper bound')
    matplotlib.pyplot.plot(lower_bound, 'g--', label='Lower bound')
    matplotlib.pyplot.legend()
    matplotlib.pyplot.show()

if __name__ == '__main__':
    n = int(input('Enter size of n: ')) #Input 1 - 200
    interval(n)
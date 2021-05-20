import numpy
import random

N = 1500000   # total number of bearings
mu_x_gram = 55  # population mean
sig_x_gram = 5  # population standard deviation

def normaldistribution(n):
    # Counters to determine number of times the mean falls into the confidence intervals
    counter95 = 0
    counter99 = 0

    rando = numpy.random.normal(mu_x_gram, sig_x_gram, N)
    for i in range(10000):
        a = rando[random.sample(range(N), n)]
        bonk = numpy.std(a, ddof=1)
        xbar = numpy.mean(a) 

        # Calculate the limits
        lower95 = xbar - 1.96 * (bonk / numpy.sqrt(n))
        upper95 = xbar + 1.96 * (bonk / numpy.sqrt(n))
        lower99 = xbar - 2.78 * (bonk / numpy.sqrt(n))
        upper99 = xbar + 2.78 * (bonk / numpy.sqrt(n))

        if mu_x_gram >= lower95 and mu_x_gram <= upper95:
            counter95 += 1
        if mu_x_gram >= lower99 and mu_x_gram <= upper99:
            counter99 += 1

    counter95 = counter95 / 100
    counter99 = counter99 / 100

    print("Normal 95% distribution at n =", n, ":", counter95)
    print("Normal 99% distribution at n =", n, ":", counter99)

def tdistribution(n):
    bonkert95 = 0
    bonkert99 = 0
    rando = numpy.random.normal(mu_x_gram, sig_x_gram, N)
    for i in range(10000):
       #All the t values from student
        if n == 5:
            t95 = 2.78
            t99 = 4.60
        elif n == 40:
            t95 = 2.02
            t99 = 2.71
        elif n == 120:
            t95 = 1.98
            t99 = 2.62

        a = rando[random.sample(range(N), n)]
        bonk = numpy.std(a, ddof=1)
        xbar = numpy.mean(a)

        # Calculate the limits
        lowert95 = xbar - t95 * (bonk / numpy.sqrt(n))
        uppert95 = xbar + t95 * (bonk / numpy.sqrt(n))
        lowert99 = xbar - t99 * (bonk / numpy.sqrt(n))
        uppert99 = xbar + t99 * (bonk / numpy.sqrt(n))

        if mu_x_gram >= lowert95 and mu_x_gram <= uppert95:
            bonkert95 += 1
        if mu_x_gram >= lowert99 and mu_x_gram <= uppert99:
            bonkert99 += 1

    bonkert95 = bonkert95 / 100
    bonkert99 = bonkert99 / 100

    print("Student t 95% distribution at n =", n, ":", bonkert95)
    print("Student t 99% distribution at n =", n, ":", bonkert99)

if __name__ == '__main__':

    normalinput = int(input("Pick a normal input 5, 40, 120: ")) 
    tinput = int(input("Pick a t input 5, 40, 120: ")) 

    if normalinput == 5:
        normaldistribution(5)
    elif normalinput == 40:
        normaldistribution(40)
    elif normalinput == 120:
        normaldistribution(120)

    if tinput == 5:
        tdistribution(5)
    elif tinput == 40:
        tdistribution(40)
    elif tinput == 120:
        tdistribution(120)





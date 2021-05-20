import numpy 
import matplotlib.pyplot as pyplot
import random
import math

def nSidedDie(probabilities):
    #creates a cumulative summative list start at 0
    probabilities = numpy.append(0, numpy.cumsum(probabilities))

    rand = numpy.random.rand()
    for index, num in enumerate(probabilities):
        if rand < num: # random number will always be bigger than the starting elements so only check if its not true
            return index

def part1(probabilities):
    n = 1000
    success = 0
    for i in range(n):
        
        #make 3 dices and pass in the probability
        s1 = nSidedDie(probabilities)
        s2 = nSidedDie(probabilities)
        s3 = nSidedDie(probabilities)

        #checks the 3 dices for 1, 2, or 3
        if(s1 == 1 and s2 == 2 and s3 == 3):
            success += 1

    return success
       
def createHistogram1():
    n = 1000
    probabilities = numpy.array([0.2, 0.1, 0.15, 0.3, 0.2, 0.05]) 
    results = numpy.zeros((n, 1))

    for i in range(n):
        results[i] = part1(probabilities)  

    #x-axis
    bins = range(0, 20)
    sb = numpy.size(bins)
    h1, binEdges = numpy.histogram(results, bins=bins)
    b1 = binEdges[0:sb - 1] 
    probability = h1 / 1000
    pyplot.close('all')

    #make graph
    fig1 = pyplot.figure(1)
    pyplot.stem(b1, probability, use_line_collection=True)
    pyplot.title('PMF for Bernuolli Trials')
    pyplot.xlabel('Successes in 1000 trials')
    pyplot.ylabel('Probability')
    pyplot.xticks(b1)
    pyplot.show()
    fig1.savefig('Figure1.jpg')

def binomialformuler(success, probabilities):
    n = 1000
    q = 1 - probabilities
    combination = math.factorial(n) / (math.factorial(success) * math.factorial(n - success))
    formula = numpy.power(probabilities, success)  #Binomial distribution formula: p^x q^(n-x)
    formula2 = numpy.power(q, n - success)
    realformuler = combination * formula * formula2

    return realformuler

def part2(): #calculates part 1 but faster with binomial distribution
    n = 19
    probabilities = numpy.array([0.2, 0.1, 0.15, 0.3, 0.2, 0.05]) 
    results = numpy.zeros((n, 1))
    b1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

    for i in range (18):
        p = probabilities[0] * probabilities[1] * probabilities[2]
        results[i] = binomialformuler(i, p)  

    #make graph
    fig2 = pyplot.figure(2)
    pyplot.stem(b1, results, use_line_collection=True)
    pyplot.title('PMF for Bernuolli Distribution')
    pyplot.xlabel('Successes in 1000 trials')
    pyplot.ylabel('Probability')
    pyplot.xticks(b1)
    pyplot.show()
    fig2.savefig('Figure2.jpg')

def poisson(success, p):
    lamb = 1000 * p
    secretformuler = (numpy.power(lamb, success) * math.exp(-1 * lamb))/ math.factorial(success)
    
    return secretformuler

def part3():
    n = 19
    probabilities = numpy.array([0.2, 0.1, 0.15, 0.3, 0.2, 0.05]) 
    results = numpy.zeros((n, 1))
    b1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

    for i in range (18):
        p = probabilities[0] * probabilities[1] * probabilities[2]
        results[i] = poisson(i, p)  

    #make graph
    fig3 = pyplot.figure(3)
    pyplot.stem(b1, results, use_line_collection=True)
    pyplot.title('PMF for Poisson Distribution')
    pyplot.xlabel('Successes in 1000 trials')
    pyplot.ylabel('Probability')
    pyplot.xticks(b1)
    pyplot.show()
    fig3.savefig('Figure3.jpg')

if __name__ == '__main__':
    createHistogram1()
    part2()
    part3()




    


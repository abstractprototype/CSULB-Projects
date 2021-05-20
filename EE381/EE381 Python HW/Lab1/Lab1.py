import numpy 
import matplotlib.pyplot as pyplot
import random
import string

#Problem 1
def nSidedDie(probabilities):
    #creates a cumulative summative list start at 0
    probabilities = numpy.append(0, numpy.cumsum(probabilities))

    rand = numpy.random.rand()
    for index, num in enumerate(probabilities):
        if rand < num: # random number will always be bigger than the starting elements so only check if its not true
            return index

def createHistogram():
    n = 10000
    probabilities = numpy.array([0.10, 0.15, 0.20, 0.05, 0.30, 0.10, 0.10]) # adds up to 1
    results = numpy.zeros((n, 1))

    for i in range(n):
        results[i] = nSidedDie(probabilities)  

    #x-axis
    b = numpy.size(probabilities)
    bins = range(1, b + 2)
    sb = numpy.size(bins)
    h1, binEdges = numpy.histogram(results, bins=bins)
    b1 = binEdges[0:sb - 1] 
    probability = h1 / n
    pyplot.close('all')

    #make graph
    fig1 = pyplot.figure(1)
    pyplot.stem(b1, probability, use_line_collection=True)
    pyplot.title('Probability mass function for an n-sided die')
    pyplot.xlabel('Die number')
    pyplot.ylabel('Probability')
    pyplot.xticks(b1)
    pyplot.show()
    fig1.savefig('PMG for an unfair n-sided die.jpg')

if __name__ == '__main__':
    createHistogram()
    
#Problem 2
def rollPairUntil7():
    rolls = 0
    while True:
        a = numpy.random.randint(1,7)
        b = numpy.random.randint(1,7)
        rolls += 1

        if a + b == 7:
            return rolls

def createHistogram1():
    n = 100000
    results = numpy.zeros(n)
    for i in range(n):
        results[i] = rollPairUntil7()

    #make the graph    
    bins = range(1, 20)
    h1, binEdges = numpy.histogram(results, bins=bins)
    b1 = binEdges[0:len(bins) - 1]
    probability = h1 / n

    fig1 = pyplot.figure(1)
    pyplot.stem(b1, probability, use_line_collection=True)
    pyplot.title('PMF for sum of 7 of 2 die rolls')
    pyplot.xlabel('Probability that the dice sum is 7')
    pyplot.ylabel('Rolls')
    pyplot.xticks(b1)
    pyplot.show()
    fig1.savefig('PMG for an unfair n-sided die.jpg')

if __name__ == '__main__':
    createHistogram1()

#Problem 3
def tossCoin():
    heads = 0 
    for i in range(100): #flip 1 coin 100 times
        if numpy.random.randint(0, 2) == 0: 
            heads += 1

    return heads == 50

if __name__ == '__main__':
    success = 0
    for i in range(100000):
        success += int(tossCoin())

    probability = success / 100000
    print('Probability:', probability)

#Problem 4
# checking m
def checkSmallPassword(m, userInput):
    n = 1000
    success = 0

    print('Calculating small password...')
    for i in range(n): # cycle 1000 times
        babyArray = makeBabyList(m)
        if userInput in babyArray: # check if password is in our random array if it is then increment success
            success += 1

    probabilitySize = success / n # calculate probability
    return probabilitySize

#checking k * m
def checkBigPassword(k, m, userInput):
    n = 1000
    success = 0

    print('Calculating big password...')
    for i in range(n): # cycle 1000 times
        fatArray = makeFatList(k,m)
        if userInput in fatArray: # check if password is in our random array if it is then increment success
            success += 1

    probabilitySize = success / n #calculate probability
    return probabilitySize

def checkTrialPassword(m, userInput):
    n = 1000
    success = 0

    print('Calculating trial password...')
    for i in range(n): # cycle 1000 times
        trialArray = makeTrialList(m)
        if userInput in trialArray: # check if password is in our random array if it is increment success
            success += 1

    probabilitySize = success / n #calculate probability
    return probabilitySize


#make list with m
def makeBabyList(m):
    array = numpy.empty(m, dtype = 'object')# makes empty array 

    for i in range(m): #80000 times
        randWord = ''.join(random.choices(string.ascii_lowercase, k=4)) #generate 4 lowercase letter words
        array[i] = randWord #put the 4 letter word inside empty array with a for loop

    return array

#make list with k and m
def makeFatList(k,m):
    array = numpy.empty(k * m, dtype = 'object')# makes empty array but with k * m

    for i in range(k * m): # 7 * 80000 times
        randWord = ''.join(random.choices(string.ascii_lowercase, k=4)) #generate 4 lowercase letter words
        array[i] = randWord #put the 4 letter word inside empty array with a for loop

    return array

def makeTrialList(m):
    array = numpy.empty(m, dtype = 'object')# makes empty array

    for i in range(m): # 7 * 80000 times
        randWord = ''.join(random.choices(string.ascii_lowercase, k=4)) #generate 4 lowercase letter words
        array[i] = randWord #put the 4 letter word inside empty array with a for loop

    return array

if __name__ == '__main__':
    userInput = input('Enter your password: ')
    print(checkSmallPassword(80000, userInput))
    print(checkBigPassword(7, 80000, userInput))
    print(checkTrialPassword(315000, userInput))





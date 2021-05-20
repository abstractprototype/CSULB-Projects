import numpy
import random

P0 = 0.60
E0 = 0.05
E1 = 0.03
N = 100000

def nSidedDie(probabilities):
    #Make a cumulative list starting at 0
    probabilities = numpy.append(0, numpy.cumsum(probabilities))

    rand = numpy.random.rand()
    for index, num in enumerate(probabilities):
        #The random number will always be larger than starting elements
        if rand < num: # check when its not true
            return index

def part1():
    fail = 0

    for i in range(N):
        s = nSidedDie([P0, 1 - P0]) - 1

        if s == 1:
            r = nSidedDie([E1, 1 - E1]) - 1
        else:
            r = nSidedDie([1 - E0, E0]) - 1
            
        if s!= r:
            fail += 1

    fail /= N

    print('Part 1: ', fail)

def part2():
    success = 0
    total = 0

    for i in range(N):
        s = nSidedDie([P0, 1 - P0]) - 1

        if s == 1:
            r = nSidedDie([E1, 1 - E1]) - 1
        else:
            r = nSidedDie([1 - E0, E0]) - 1

        if s == 1:
            total += 1
            if r == 1:
                success += 1

    print('Part 2: ', (success/total))

def part3():
    success = 0
    total = 0

    for i in range(N):
        s = nSidedDie([P0, 1 - P0]) - 1

        if s == 1:
            r = nSidedDie([E1, 1 - E1]) - 1
        else:
            r = nSidedDie([1 - E0, E0]) - 1

        if r == 1:
            total += 1
            if s == 1:
                success += 1

    print('Part 3: ', (success/total))

def part4():
    fail = 0
    #Repeat experiement 100000 times
    for i in range(N):
       array = [] # array to store 3 bits
       s = nSidedDie([P0, 1 - P0]) - 1

       # Generate the 3 bits
       for i in range(3):
           if s == 1:
               bit = nSidedDie([E1, 1 - E1]) - 1
           else:
               bit = nSidedDie([1 - E0, E0]) - 1
           array.append(bit)

       #voting and majority rule 
       majority = sum(array)
       if majority > 1:
           majority = 1
       else: 
           majority = 0

       if s != majority:
           fail += 1

    print('Part 4: ', (fail / N))

    
if __name__ == '__main__':

  part1()
  part2()
  part3()
  part4()


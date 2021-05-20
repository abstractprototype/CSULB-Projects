import numpy
import matplotlib.pyplot as plt

def nSidedDie(p):
    n = len(p)
    cumulative = numpy.cumsum(p)
    cumlist = numpy.append(0, cumulative)
    rand = numpy.random.rand()
    for k in range(0, n):
        if rand > cumlist[k] and rand <= cumlist[k + 1]: #random number will always be bigger than the starting elements so only check if its not true
            index = k + 1
    return index - 1

def absorbingMarkov():
    Vector = []
    initial = [0, 1/3, 1/3, 1/3, 0]
    stm0 = [1, 0, 0, 0, 0] #Simulated Markov Chain 
    stm1 = [0.3, 0, 0.7, 0, 0]
    stm2 = [0, 0.5, 0, 0.5, 0]
    stm3 = [0, 0, 0.6, 0, 0.4]
    stm4 = [0, 0, 0, 0, 1]

    #Starts at a random transient state
    for i in range(15):#Single run simulation of the chain
        r = nSidedDie(initial)
        Vector.append(r)
    print("Initial states:", Vector)

    for k in range(1, 15):
        if Vector[k - 1] == 0:
            Vector[k] = nSidedDie(stm0)
        elif Vector[k - 1] == 1:
            Vector[k] = nSidedDie(stm1)
        elif Vector[k - 1] == 2:
            Vector[k] = nSidedDie(stm2)
        elif Vector[k - 1] == 3:
            Vector[k] = nSidedDie(stm3)
        else:
            Vector[k] = nSidedDie(stm4)

    #Absorbed by state 0        
    #Absorbed by state 4
    print("Final states:", Vector)
    b = list(range(0, len(Vector)))#use this for plotting

    plt.title("Five state absorbing Markov Chain")
    plt.xlabel("Step")
    plt.ylabel("State")
    plt.plot(b, Vector, 'b:')
    plt.plot(b, Vector, 'bo', label="State")
    plt.legend()
    plt.show()

if __name__ == '__main__':
    absorbingMarkov()
import numpy
import random
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

def markov():
    S = []
    start = [0.25, 0, 0.75] #intial probability distribution vector: 1/4, 0, 3/4
    stm1 = [1/2, 1/4, 1/4] #given state transition matrix
    stm2 = [1/4, 1/8, 5/8]
    stm3 = [1/3, 2/3, 0]

    for i in range(15): #15 steps
        r = nSidedDie(start)
        S.append(r)
    print("Starting States", S)

    for k in range(1, 15):
        if S[k - 1] == 0:
            S[k] = nSidedDie(stm1)
        elif S[k - 1] == 1:
            S[k] = nSidedDie(stm2)
        else:
            S[k] = nSidedDie(stm3)

    b = list(range(0, len(S)))

    print("Last States", S)
    plt.title("Three-state Markov Chain")
    plt.xlabel("Step")
    plt.ylabel("State")
    plt.plot(b, S, 'c:')
    plt.plot(b, S, 'bo', label="State")
    plt.legend()
    plt.show()


def markov_thousand(): #shows combined results of 10000 runs of the chain
    n = 15
    N = 10000
    initial = [0.25, 0, 0.75] #intial probability distribution vector: 1/4, 0, 3/4
    stm1 = [1 / 2, 1 / 4, 1 / 4] #given state transition matrix
    stm2 = [1 / 4, 1 / 8, 5 / 8]
    stm3 = [1 / 3, 2 / 3, 0]

    P = numpy.matrix([stm1,stm2,stm3])

    S = numpy.zeros((n, 3))#Fill with zeroes
    S[0, :] = initial

    for k in range(1, n):
        S[k, :] = S[k - 1, :] * P

    b = list(range(0, n))

    plt.plot(b, S[:, 0], 'b--*', label='State R')
    plt.plot(b, S[:, 1], 'g--o', label='State N')
    plt.plot(b, S[:, 2], 'c--h', label='State S')
    plt.title("Simulated Three State Markov Chain")
    plt.xlabel("Step")
    plt.ylabel("State")
    plt.legend()
    plt.show()

    M = numpy.zeros((n, 3))
    S = numpy.array(numpy.zeros((n, N)))
    for k in range(0, N):
        r = nSidedDie(initial)
        S[0, k] = r

    for k in range(0, N):
        for j in range(1, n):
            current = S[j - 1, k]
            if current  == 0:
                r = nSidedDie(stm1)
            elif current  == 1:
                r = nSidedDie(stm2)
            else:
                r = nSidedDie(stm3)
            S[j, k] = r

    for j in range(0, n):
        u = S[j, :]
        r = 0
        n = 0
        s = 0
        for k in range(0, N):
            if u[k] == 0:
                r += 1
            elif u[k] == 1:
                n += 1
            else:
                s += 1
        M[j, :] = [r / N, n / N, s / N]

    plt.plot(M[:, 0], 'b--*', label='State R')
    plt.plot(M[:, 1], 'g--o', label='State N')
    plt.plot(M[:, 2], 'c--+', label='State S')
    plt.title('Calculated Three State Markov Chain')
    plt.xlabel('Step')
    plt.ylabel('State')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    markov()
    markov_thousand()

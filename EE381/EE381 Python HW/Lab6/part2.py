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

def pagerank():
    n = 20 #20 steps
    initial = [0.2, 0.2, 0.2, 0.2, 0.2]
    #Creating the state transition matrix
    stm0 = [0, 1, 0, 0, 0]          # A
    stm1 = [0.5, 0, 0.5, 0, 0]      # B
    stm2 = [1/3, 1/3, 0, 0, 1/3]    # C
    stm3 = [1, 0, 0, 0, 0]          # D
    stm4 = [0, 1/3, 1/3, 1/3, 0]    # E
    P = numpy.matrix([stm0,stm1,stm2,stm3,stm4])

    State = numpy.zeros((n, 5))
    State[0, :] = initial
    for k in range(1, n):
        State[k, :] = State[k - 1, :] * P

    b = list(range(0, n)) #used for plotting
    fig1 = plt.figure(1)
    plt.plot(b, State[:, 0], '--*', label='A')
    plt.plot(b, State[:, 1], '--o', label='B')
    plt.plot(b, State[:, 2], '--h', label='C')
    plt.plot(b, State[:, 3], '--x', label='D')
    plt.plot(b, State[:, 4], '--+', label='E')
    plt.title("Probability Distribution Vector of v1 = [1/5, 1/5, 1/5, 1/5, 1/5]")
    plt.xlabel("Step")
    plt.ylabel("State")
    plt.legend()
    print(State)
    plt.show()

    #Repeat experiment with a new initial given
    initial = [0, 0, 0, 0, 1]
    fig2 = plt.figure(2)
    S = numpy.zeros((n, 5))
    S[0, :] = initial
    for k in range(1, n):
        S[k, :] = S[k - 1, :] * P
    plt.plot(b, S[:, 0], '--*', label='A')
    plt.plot(b, S[:, 1], '--o', label='B')
    plt.plot(b, S[:, 2], '--h', label='C')
    plt.plot(b, S[:, 3], '--x', label='D')
    plt.plot(b, S[:, 4], '--+', label='E')
    plt.title("Probability Distribution Vector of v2 = [0, 0, 0, 0, 1]")
    plt.xlabel("Step")
    plt.ylabel("State")
    plt.legend()
    print(S)
    plt.show()


if __name__ == '__main__':
    pagerank()


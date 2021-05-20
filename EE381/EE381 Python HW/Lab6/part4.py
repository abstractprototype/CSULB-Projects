import numpy

def nSidedDie(p):
    n = len(p)
    cumulative = numpy.cumsum(p)
    cumlist = numpy.append(0, cumulative)
    rand = numpy.random.rand()
    for k in range(0, n):
        if rand > cumlist[k] and rand <= cumlist[k + 1]: #random number will always be bigger than the starting elements so only check if its not true
            index = k + 1
    return index - 1

def absorption():
    Vector = []
    b20 = 0
    b24 = 0
    N = 10000
    initial = [0, 0, 1, 0, 0] #initial state
    stm0 = [1, 0, 0, 0, 0] 
    stm1 = [0.3, 0, 0.7, 0, 0]
    stm2 = [0, 0.5, 0, 0.5, 0]
    stm3 = [0, 0, 0.6, 0, 0.4]
    stm4 = [0, 0, 0, 0, 1]

    for o in range(N): #10000 times repeat
        for i in range(15):
            r = nSidedDie(initial)#pass in the initial state for nsideddie then append to vector
            Vector.append(r)
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

        if 4 in Vector:
            b20 += 1
        elif 0 in Vector:
            b24 += 1
        Vector = []

    print("Absorption probability at b20 = ", b20 / N)
    print("Absorption probability at b24 = ", b24 / N)

if __name__ == '__main__':
    absorption()
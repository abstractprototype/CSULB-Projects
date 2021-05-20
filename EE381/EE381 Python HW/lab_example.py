import numpy as np
import random

def nSidedDie(p):
    n=np.size(p)
    cs=np.cumsum(p)
    cp=np.append(0,cs)
    r=random.random()
    for k in range(0,n):
        if r>cp[k] and r<=cp[k+1]:
            d=k+1
            break
    print('Ramdom number generated {:1}'.format(d))
    return d

def experiment(p,N):
    n=np.size(p)
    s=np.zeros((N,1))
    for i in range(0,N):
        d=nSidedDie(p)
        s[i]=d

def main():
    p=np.array([0.25, 0.25, 0.25, 0.25])
    N=10
    experiment(p,N)

if __name__ == "__main__":
    main()
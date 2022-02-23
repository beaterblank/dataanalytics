from math import exp
from tabulate import tabulate
from numpy import transpose as t

x1 = [28,52,37,53,32,51] 
y = [0,1,0,1,0,1]

b1 = [-16,0.3]
b2 = [-13,0.3]


b = [b1,b2]
x = [x1]

def p(x,b):
    prob = [b[0]]*len(x[0])
    for i in range(len(x)):
        for j in range(len(x[i])):
            prob[j]+=b[i+1]*x[i][j]
    return prob

def nlexp(l):
    return [round(1/(1+exp(-x)),4) for x in l]

def formula(x,b):
    prob = p(x,b)
    pnexp = nlexp(prob)
    return pnexp

def likelyhood(f,y):
    tmp = []
    tmp.extend(f)
    for i in range(len(y)):
        if(y[i]==0):
            tmp[i] = round(1-tmp[i],4)
    return tmp

def show(x,b1,y):
    f = formula(x,b1)
    l = likelyhood(f,y)
    parr = []
    parr.extend(x)
    for i in b1:
        parr.append([i]*len(x[0]))
    parr.append(f)
    parr.append(y)
    parr.append(l)
    print(tabulate(t(parr)))
    mul = 1
    for i in l:
        mul=mul*i
    return round(mul,4)

for i in b:
    print()
    print(f"{i = }")
    print("likelyhood = ",show(x,i,y))
    print()


input()
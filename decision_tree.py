from math import log2
def entropy(l):
    print(l) 
    p = [round(x/sum(l),2) for x in l]
    print(f"{p = }")
    l = [round(-pi*log2(pi),2) if(pi!=0) else 0 for pi in p]
    print("E(s) = Σ-pi*log2(pi) = Σ",l," = ",round(sum(l),2))
    print()
    return round(sum(l),2)
def gain(l):
    tmp = list(l)
    for i in range(len(tmp)):
        tmp[i] = sum(tmp[i])
    li = []
    for i in range(len(l)):
        li.append(entropy(l[i]))
    print(li)
    g = li[-1]
    s = 0
    print("gain = ",g,end=" ")
    for i in range(len(l)-1):
        s = s+(tmp[i]/tmp[-1])*li[i]
        print(f"-({tmp[i]}/{tmp[-1]})*{li[i]}",end="")
    print(" = ",round(g-s,4))

print()
gain([[2,3],[4,0],[3,2],[9,5]])
print()
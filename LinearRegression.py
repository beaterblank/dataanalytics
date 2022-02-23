from math import sqrt

x =[2,3,4,5,6]
y =[5.6564,15.5835,32,55.9817,88.1816]



def sqr(lis):
  return [round(x**2,5) for x in lis]
def mul(lis1,lis2):
  return [lis1[i]*lis2[i] for i in range(len(lis1))]


print()
print(f"{x = }")
print(f"{y = }\n")

n = len(x)

sx = sum(x)
print("x^2 = ",sqr(x))
sx2 = sum(sqr(x))

sy = sum(y)
print("y^2 = ",sqr(y))
sy2= sum(sqr(y))

print("xy = ",mul(x,y))
sxy = sum(mul(x,y))

print(f"{n = }\nΣx = {sx :.3f}\nΣx² = {sx2 :.3f}\nΣy = {sy :.3f}\nΣy² = {sy2 :.3f}\nΣxy = {sxy :.3f}")

b = (sy*sx2-sx*sxy)/(n*sx2-sx**2)
a = (n*sxy-sx*sy)/(n*sx2-sx**2)

print("\nyp = a*x + b")
print(f"\na = (n*Σxy-Σx*Σy) / (n*Σx²-(Σx)²)  ")
print(f"{a = :.3f}")
print(f"\nb = (Σy*Σx²-Σx*Σxy) / (n*Σx²-(Σx)²)  ")
print(f"{b = :.3f}")

yp = [round(a*k+b,3) for k in x]
print(f"\nHence {yp = }\n")
k = [round(y[i]-yp[i],3) for i in range(len(y))]
print("y-yp = ",k)
rss = sum([(y[i]-yp[i])**2 for i in range(len(y))])
print("rss = Σ(y-yp)²")
print("rss = Σ",[round((y[i]-yp[i])**2,3) for i in range(len(y))])
print(f"rss = {rss :.4f}")
print("\nrse = sqrt(rss/(n-2))")
rse = sqrt(rss/(n-2))
print(f"{rse = :.3f}\n")
mx = sx/n
sxx2 = sum([(aaa-mx)**2 for aaa in x]) 
sea = rse*sqrt(1/sxx2)
print(f"SE(a) = rse*sqrt(1/(x-mx)^2) = {round(sea,3)}")
seb = rse*sqrt((1/n)+(mx*mx/sxx2))
print(f"SE(b) = rse*sqrt((1/n)+(mx*mx)/(x-mx)^2) = {round(seb,3)}")
print(f"\n95% confidence interval for a is [a-2*SE(a),a+2*SE(a)] = {[round(a-2*sea,3),round(a+2*sea,3)]}")
print(f"95% confidence interval for b is [b-2*SE(b),b+2*SE(b)] = {[round(b-2*seb,3),round(b+2*seb,3)]}")
my = sy/n
tss = [round((bbb-my)**2,3 )for bbb in y]
print(f"\ntss = Σ({tss}) = {sum(tss):.3f}")
tss = sum(tss)
r2 = 1-(rss/tss)
print(f"R^2 = 1-(rss/tss) = {r2:.3f}")
input()
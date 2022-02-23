x = [5,3,4,10,15]
y = [25,20,21,35,38]

def sqr(lis):
  return [round(x**2,5) for x in lis]
def mul(lis1,lis2):
  return [lis1[i]*lis2[i] for i in range(len(lis1))]

from math import sqrt

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

print(f"\n{n = }\nΣx = {sx :.3f}\nΣx² = {sx2 :.3f}\nΣy = {sy :.3f}\nΣy² = {sy2 :.3f}\nΣxy = {sxy :.3f}")
print("\nr = (n*Σxy-Σx^2)/sqrt(n*Σx^2-(Σx)^2)*sqrt(n*Σy^2-(Σy)^2)\n")
rn = n*sxy-sx*sy
rd1 = sqrt(n*sx2-sx*sx)
rd2 = sqrt(n*sy2-sy*sy)

print(f"Numerator = {rn:.3f}\ndenominator = {rd1:.3f}*{rd2:.3f} = {rd1*rd2:.3f}")
print(f"\nHence r = {rn/(rd1*rd2):.3f}")
input()
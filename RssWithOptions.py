x = [2,3,4,5,6]
y = [12.8978,17.7586,23.3192,28.3129,32.1351]

a1,b1=4,3
a2,b2=5,3
a3,b3=5,1
a4,b4=1,5

#x = input("X = ").split(" ")
#x = [int(k) for k in x]
#y = input("Y = ").split(" ")
#y = [float(k) for k in y]

# a1,b1 = input("a1 b1 = ").split(" ")
# a2,b2 = input("a2 b2 = ").split(" ")
# a3,b3 = input("a3 b3 = ").split(" ")
# a4,b4 = input("a4 b4 = ").split(" ")



a1 = int(a1)
b1 = int(b1)

a2 = int(a2)
b2 = int(b2)

a3 = int(a3)
b3 = int(b3)

a4 = int(a4)
b4 = int(b4)

def rss(a,b,ya,x):  
  print(f"\n{a = }\n{b = }\n")
  yp= [b+a*k for k in x]
  print(f"Y Predicted = a*x+b = {yp = }\n")
  rv = [round(ya[i]-yp[i],3) for i in range(len(ya))]
  print(f"Residual vector = ya-yp = {rv}\n")
  print("RSS = ",end="")
  rss = 0
  for i in range(len(ya)):
    print(f" [{ya[i]}-{yp[i]}]² ",end="+")
    rss += (ya[i]-yp[i])**2
  print("\n    = ",end="")
  for i in range(len(ya)):
    print(f" [{round(ya[i]-yp[i],3)}]² ",end="+")
  print(f"\n\nRSS = {round(rss,5)}")
  return a,b,yp,rss

r1 = rss(a1,b1,y,x)
r2 = rss(a2,b2,y,x)
r3 = rss(a3,b3,y,x)
r4 = rss(a4,b4,y,x)

print("\n[Parameters]        [Y Predicted]       [RSS]")
print(f"  {r1[0]},{r1[1]}       {r1[2]}            {round(r1[3],3)}")
print(f"  {r2[0]},{r2[1]}       {r2[2]}            {round(r2[3],3)}")
print(f"  {r3[0]},{r3[1]}       {r3[2]}            {round(r3[3],3)}")
print(f"  {r4[0]},{r4[1]}       {r4[2]}            {round(r4[3],3)}")

input()

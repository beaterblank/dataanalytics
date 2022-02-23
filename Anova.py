from tabulate import tabulate
from numpy import transpose as t
import scipy.stats

x1 = [82, 81, 86, 77, 74, 85, 89]
x2 = [82 ,85, 84, 89, 85, 90, 87]
x3 = [92 ,97, 99, 94, 98, 96, 95] 

# make changes
x = [x1,x2,x3] # make change 

def anova(x:list):
  print("Given Data : ")
  print(tabulate(t(x),floatfmt=".2f",numalign="right"))
  n = len(x)
  N = len(x[0])
  mx = []
  for i in range(n):
    mx.append(mean(x[i]))
  print("Means = ",mx)
  mm = round(mean(mx),2)
  print("Overall Mean  = ",mm)
  sst = []
  for i in range(len(x)):
    kk = []
    for j in range(len(x[0])):
      kk.append(0)
    sst.append(kk)
  for i in range(len(x)):
    for j in range(len(x[0])):
      sst[i][j] = round((mm-x[i][j])**2,3)
  sums = []
  for i in sst:
    sums.append(sum(i))
  print("\nsst : (overall mean - x)**2 :")
  print(tabulate(t(sst),floatfmt=".2f",numalign="right"))
  print(f"{sums = }")
  print(f"sst = Σsums = {sum(sums):.3f}")
  print()
  ssc = []
  for i in mx:
    ssc.append(round(N*(i-mm)**2,2))
    #print(i-mm)
  print("\nSSC = ΣN*(Column Mean - Overall Mean)**2 = ",ssc)
  ssc = round(sum(ssc),2)  #round off
  print("SSC = ΣN*(Column Mean - Overall Mean)**2 = ",ssc)
  xa = x[:]
  for i in range(len(x)):
    print(mx[i],x[i])
    for j in range(len(x[0])):
      
      xa[i][j] = (mx[i]-x[i][j])**2
      pass
  print("\n(X - Column Mean)^2 : ")
  print(tabulate(t(xa),floatfmt=".2f",numalign="right"))
  
  sse = []
  for i in range(n):
    sse.append(round(sum(xa[i]),2))
  print("Sum = ",sse)
  sse = round(sum(sse),2)  # round off
  print("SSE = Σsum = ",sse)
  N = len(x[0])
  C = len(x)
  dfc = C-1
  dfe = N*C-C
  print(f"\ndf(column) = {dfc}\ndf(error) = {dfe}\ndf(total) = {dfe+dfc}\n")
  MSC = ssc/dfc
  MSE = sse/dfe
  print(f"MSC = SSC/df(column) = {MSC:.2f}\nMSE = SSE/df(error) = {MSE:.2f}\n")
  f = MSC/MSE
  print(f"F Static Value = MSC/MSE = {f:.3f}")
  fcrit = scipy.stats.f.ppf(q= 1 -.05, dfn=dfc, dfd=dfe) #update confidence interval
  print(f"{fcrit = :.3f}")

  if(fcrit>f):
    print("\nf static < fcritical")
    print("Null hypothesis accepted")
    print("No significant difference in mean")
  else:
    print("\nf static > fcritical")
    print("Null hypothesis Rejected")
    print("Significant difference in mean is detected")



def mean(x:list):
  return round(sum(x)/len(x),2)


anova(x)

input()

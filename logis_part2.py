from math import log

b = [-13, 0.3] #b0, b1
px = 0.9 #confidence interval

lpx = log(px/(1-px)) 
xmin = (lpx-b[0])/b[1]
print(f"{xmin = :.2f}")

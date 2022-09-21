import math
N=int(input("ingrese N"))
lim=math.sqrt(N)
lim=int(round(lim,0))
for x in range(1,lim):
    a=x*x
    for y in range(1,lim):
        b=y*y
        if a+b==N:
            print(x)
            print(y)

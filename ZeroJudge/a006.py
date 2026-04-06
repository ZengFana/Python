import math
x=input()
x=x.split()
y=int(x[1])
z=int(x[2])
x=int(x[0])
q=y ** 2 - 4 * x * z#**
if q > 0:
    root1=int((-1*y+math.sqrt(q))/(2*x))
    root2=int((-1*y-math.sqrt(q))/(2*x))
    print(f'Two differnet roots x1={root1}, x2={root2}')
elif q==0:
    root=int((-1*y)/(2*x))
    print(f'Two same roots x={root}')
else:
    print(f'No real root')
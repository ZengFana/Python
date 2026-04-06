""" x=int(input())
for i in range(x):
    y=list(map(int,input().split()))
    if y[1]-y[0] == y[2] - y[1]:
        z = y[3] + (y[2] - y[1])
    else:
        z = y[3] * (y[2] // y[1])
    print(y[0],y[1],y[2],y[3],z) """
for i in range(int(input())):
    x=list(map(int,input().split()))
    print(' '.join(str(y) for y in x) + ' ' + str((x[3]*(x[1]//x[0])) if(x[1]/x[0] == x[2]/x[1]) else (x[3]+(x[1]-x[0]))))
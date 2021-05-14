"""ProjectEuler #001 
   Multiples of 3 and 5"""

t=int(input())
for i in range(t):
    d=int(input())
    n3=(d-1)//3
    n5=(d-1)//5
    n15=(d-1)//15
    print((n3*(6+(n3-1)*3)//2)+(n5*(10+(n5-1)*5)//2)-(n15*(30+(n15-1)*15)//2))


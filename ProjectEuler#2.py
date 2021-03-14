"""ProjectEuler #2 
   Even Fibonacci numbers"""

t=int(input())
for i in range(t):
    n=int(input())
    a,b,s=1,1,0
    while a<n:
        if a%2==0:
            s+=a
        b,a=a,a+b
    print(s)

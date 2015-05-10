import math

def chkprime(n):
    for k in range(2,int(math.sqrt(n))+1):
        if (n % k) == 0:
            return 0  
    return 1
           
t=int(input())
for j in range(0,t):
    num = int(input())
    i=0
    range=2
    prime=0
    while(j<num):
        if chkprime(range)==1:
            i=i+1
            prime=range
        range+=1

    print prime

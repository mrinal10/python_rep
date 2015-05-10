def fact(n):
    if n==1 or n==0:
        return 1
    else:
        fact=1
        for i in range(2,n+1):
            fact=fact*i
        return fact

def countzeros(n):
    count=0
    while n%10==0:
        count+=1
        n=n/10
    return count

t=input()
while t>0:
    t-=1
    n=input()
    f=fact(n)
    d=countzeros(f)
    print d

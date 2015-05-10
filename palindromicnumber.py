def palindrome(n):
    v=n
    k=0
    while v>0:
        k=(k*10)+(v%10)        
        v=v/10
        
    if k==n:
        return 1
    else:
        return 0

t=int(raw_input())
while t>0:
    t=t-1
    a, b=raw_input().split()
    a=int(a)
    b=int(b)
    count=0
    for i in range (a,b+1):
        k=palindrome(i)
        if(k==1):            
            count=count+1
    print count
    

def getgcd(n1,n2):
    if n1>n2:
        temp=n1
        n1=n2
        n2=temp

    for i in range(n1,0,-1):
        if n1%i==0 and n2%i==0:
            return i

        

n=input()
while n>0:
    n=n-1
    #print ('t =',n)
    s=raw_input()
    li= [0 for i in xrange(26)]
    l=len(s)
    for i in range (0,26):
        li[i]=0
        
    for i in range(0,l):
        t=ord(s[i])
        if t>64 and t<91:
            t=t-64
        else:
            t=t-97
        li[t]+=1
        
    flag=max(li)
    val=0
    for i in range(0,26):
        if li[i]!=0:
            val=li[i]
            flag=getgcd(flag,val)
    print flag
    
        

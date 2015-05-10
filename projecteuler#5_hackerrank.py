

def chkfactor(a,b):
    #print "a =",a
    #print "b =",b
    min=a
    if a<b:
       min=a
    else:
        min=b
        
    for i in range(min,1,-1):
        if (a%i==0 and b%i==0):
            return i
    return 1


    
t = int (input())
for j in range(0,t):
    n = int (input())
    res = 1
    for i in range(2,n+1):
        #print chkfactor(i,res)
        fac=i/chkfactor(i,res)
        res=res*fac
       # print res

    print res

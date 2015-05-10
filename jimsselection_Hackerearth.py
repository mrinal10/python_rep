t=int(raw_input())
while t>0:
    t-=1
    n=int(raw_input())
    i=1
    f=1
    p=pow(2,i)
    if n==1:
        f=0
    else:
        while n>=p:
            if n==p:
                f=0
                break		
            i+=1	
            p=pow(2,i)
	        
    if f==0: print "Yes"
    else: print "No"

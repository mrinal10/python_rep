t=input()
while t>0:
    t-=1
    n=input()
    line = raw_input()
    line=line.split(" ")
    boys=[]
    while len(boys)<n:
        b=int(line[len(boys)])
        #print b
        boys.append(b)
    boys.sort()
    #print boys
    
    line = raw_input()
    line=line.split(" ")
    girls=[]
    while len(girls)<n:
        g=int(line[len(girls)])
        #print g
        girls.append(g)
            
    girls.sort()
    girls.reverse()
    #print girls
    i=0
    count=0
    while i<n:
        if boys[i]%girls[i]==0 or girls[i]%boys[i]==0 :
            count+=1

    print count
        
        

import math
p,q,x=raw_input().split()
p=int(p)
q=int(q)
x=int(x)

count=0
maxhop=0
for i in range(1,p+1):
    for j in range(1,q+1):
        if i==1 or i==p:
            diffi=p
            diffmi=0
            di=(diffi+diffmi)
            xtim=math.floor(di/x)
            if j==1 or j==q:
                diffj=q
                diffmj=0
            else:
                diffj=q-j+1
                diffmj=j
            dj=(diffj+diffmj)
            ytim=math.floor(dj/x)
            
        else:
            diffi=p-i+1
            diffmi=i
            di=(diffi+diffmi)
            xtim=math.floor(di/x)
            if j==1 or j==q:
                diffj=q
                diffmj=0
            else:
                diffj=q-j+1
                diffmj=j
            dj=(diffj+diffmj)
            ytim=math.floor(dj/x)
        print xtim*(ytim-1)
        

def inp(n):
        a=[]
        l=raw_input().split(" ")
        print n
        for i in range(0,n):
            print i
            t=int(l[i])
            a.append(t)
        a.sort()
        return a

t=input()
while t>0:
	t-=1
	a=[]
	b=[]
	n=input()
	a=inp(n)
	#print a
	b=inp(n)
	#print b
	
	flag=0
	for i in range(0,n):
		if a[i]<b[i]:
			flag=1
			break
	
	if flag==1:
		print "NO"
	else:
		print "YES"

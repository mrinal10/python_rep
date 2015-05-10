def fact(n):
	f=1
	if n==1 or n==0:
		return 1
	else:
		for i in range(2,n):
			f=f*i
		return f

t=input()
while t>0:
	t-=1
	n=input()
	v=[]
	line=raw_input()
	p=line.split(' ')
	while len(v)<n:
		item = int(p[len(v)])
		v.append(item)
	v.sort()
	t=v[0]
	count=0
	for i in range(1,len(v)):
		t1=v[i]
		if t==t1:
			count=count+1
		else:
			t=t1
		r=fact(n)/(fact(count)*2)
	print r

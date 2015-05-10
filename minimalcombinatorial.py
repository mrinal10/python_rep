def fact(n):
	f=1
	for i in range(1,n+1):
		f=f*i
	return f

t=int(raw_input())
for i in range(1,t+1):
	a, b=raw_input().split()
	a=int(a)
	b=int(b)
	print a
	print b
	print(fact(a)/(fact(b)*fact(a-b)))

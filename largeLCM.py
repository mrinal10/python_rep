def gcd(a,b):
	if a>b:
		min=b
		b=a
		a=b
	for i in range (2,a+1):
		if a%i==0 and b%i==0:
			return i

def lcm(a,b):
	return int((a*b)/gcd(a,b))


t=int(raw_input())
while t>0:
	t-=1
	v=0
	n=int(raw_input())	
	for j in range(1,n+1):
		v=int(v)+lcm(j,n)
	ss = v/n
	print ss

import math
def isprime(n):
	for i in range(2,int(math.sqrt(n)+1)):
		if n%i==0:
			return 0;
	
	return 1
	
	
t=int(raw_input())
while(t>0):
	t=t-1
	a, b=raw_input().split()
	a, b=int(a), int(b)
	max=a
	min=b
	if a<b:
		max=b
		min=a
	flag=-1
	if isprime(min)==1:
		if max%min==0:
			flag=0
		else:
			flag=1
	else:
		"""print math.sqrt(min)"""
		for i in range(2,int(math.sqrt(min)+1)):
			if a%i==0 and b%i==0:
				flag=0
		
	if flag==0:
		print "Not a Co-Prime"
	else:
		print "Is a Co-Prime"

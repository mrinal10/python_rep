t = int(raw_input())
print t
while t>0:
	t = t-1
	bulbs = int(raw_input())
	arr = [0] * bulbs
	print arr
	i = 0
	while(i < bulbs):
		j=0
		while(j < bulbs):
			if( (i+1)%(j+1) == 0 ):
				if arr[i]==0:
					arr[i]=1
				else:
					arr[i]=0
			j = j+1
		i = i+1
	i=0
	while i<bulbs:
		if( arr[i] == 1):
			print (i+1)		
		i = i+1
	print arr

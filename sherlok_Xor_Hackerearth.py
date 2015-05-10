from array import *

t=int(raw_input())
while t>0:
	t=t-1
	n=int(raw_input())
	my_array = array('i')
	list1=raw_input()
	list1.split()
	count=0
	for i in range(0,n-1):
		for j in range(i+1,n):
			t1=int(list(i))
			t2=int(list1(j))
			if int(t1 ^ t2)%2==1:
				count+=1
	
	print count

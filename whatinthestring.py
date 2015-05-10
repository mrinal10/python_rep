s=raw_input()
count=0
for i in range (0,len(s)):
	t=int(s[i])
	if t==1:
		count=count+2
	elif t==2:
		count=count+5
	elif t==3:
		count=count+5
	elif t==4:
		count=count+4
	elif t==5:
		count=count+5
	elif t==6:
		count=count+6
	elif t==7:
		count=count+3
	elif t==8:
		count=count+7
	elif t==9:
		count=count+6
	elif t==0:
		count=count+6
		
print count	

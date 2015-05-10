def reverse(s):
	len=s.length()
	s1="";
	for i in range(0,len):
		s1.append(s[len-1-i]
    return s1;


val=int(raw_input())
s=[]
for i in range(0,val):
	s.append(raw_input())
	
for i in range(0,val-1):
	s1=s[i]
	s2=reverse(s1)
	for j in range(i+1,val):
		if(s2==s[j]):
			print s1
			print [s1(s1.length-1)/2]

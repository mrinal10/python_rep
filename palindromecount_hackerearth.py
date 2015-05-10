def strrev(s):
	for i in range(0,len(s)/2):
		s[i]=s[len(s)-i-1]
	return s

def str_palindrome(s):
	if s==strrev(s):
		return 1
	else:
		return 0


s=raw_input()
l=len(s)
for i in range(1,len(s)+1):
	for j in range(0,len(s)-i): 
		substr=s[j+i:]

s=raw_input()
length=len(s)

t=int(raw_input())
while(t>0):
    t=t-1
    a, b=raw_input().split()
    a=int(a)
    b=int(b)
    a=a%length
    b=b%length
    flag=-1
    if s[a-1]==s[b-1]:           
        print "YES"
    else:
        print "NO"

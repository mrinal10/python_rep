t=int(raw_input())
while(t>0):
    t=t-1
    s=raw_input()
    length=len(s);
    flag=-1
    for i in range(0,length-1):
       if s[i]==s[i+1]:
           flag=0
    if flag==0:
        print "SLAP"
    else:
        print "KISS"

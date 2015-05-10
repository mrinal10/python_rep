def palindrome(n):
    temp=n
    t=0
    while temp>0:
        t=(t*10)+(temp%10)
        temp=temp/10
    if t==n:
        return 1
    else:
        return 0

t=input()
while t>0:
    t-=1
    n=input()
    flag=0
    while flag!=1:
        n+=1
        #print "n"
        #print n
        flag=palindrome(n)
    print n

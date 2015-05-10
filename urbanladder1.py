def findthreefive(n):
    while n>0:
        temp=n%10
        n=n/10
        print "n"
        print n
        if temp!=3 and temp!=5:
            #print "Hello"
            return False
    return True

t=int(raw_input())
while t>0:
    t-=1
    n=int(raw_input())
    flag=False

    while flag!=True:
        #print n
        n+=1
        if findthreefive(n)==True:
            flag=True
    print n

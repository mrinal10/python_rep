import math

# take input from the user
t=int(input())
for j in range(0,t):
    num = int(input())
    a=0
    b=1
    t=0
    temp=0
    while(b<num):
        t=b
        b=a+b
        a=t
        if a%2 == 0:
            temp=temp+a;
        #print "a=",a
        #print "b=",b
        #print "temp=",temp
    print temp
        
    

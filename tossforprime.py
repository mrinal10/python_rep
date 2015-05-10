import math

def isprime(n):
        print n
        if n==1:
                return 0
        m=int(math.sqrt(n)+1)
        print m
        for i in range(2,m):
                print ("i = ",i)
                if n%i==0:
                    print "NO"
                    return 0
        return 1



n=2
print isprime(2)

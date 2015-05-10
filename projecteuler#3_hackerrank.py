import math

# Python program to check if
# the input number is
# prime or not
def chkprime(n):
    for i in range(2,int (math.sqrt(n))+1):
        if (n % i) == 0:
            #print(i)
            return 0    # if input number is less than
    # or equal to 1, it is not prime
    return 1
           

# take input from the user
t=int(input())
for j in range(0,t):
    num = int(input())
    #kk=int (math.sqrt(num))
    for i in range(num,2,-1):        
        if (num%i)==0:
            #print(i)
            ks= chkprime(i)
            #print(ks)
            if (ks==1):
                print i
                break
    

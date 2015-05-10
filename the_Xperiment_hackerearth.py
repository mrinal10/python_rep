import math

def check_prime(n):
    var = math.sqrt(n)+1
    var = int(math.floor(var))
    if n==1:
        return False
    for i in range(2,var):
        if n%i == 0:
            return False
    return True

t=int(input())
for i in range(0,t):
    n = raw_input()
    n = int(n)

    count=0
    j=1
    while count < n:
        j+=1
        if j==2:
            print j
            count+=1
        elif j%2!=0:
            if(check_prime(j)==True):
                print j
                count+=1
        


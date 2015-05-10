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
    m, n = raw_input().split()
    m, n = [int(m), int(n)]

    for j in range(m,n+1):
        if j==2:
            print j
        elif j%2!=0:
            if(check_prime(j)==True):
                print j
        


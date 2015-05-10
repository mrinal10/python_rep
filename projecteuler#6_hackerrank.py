import math

# Python program to check if
# the input number is
# prime or not
def difference(n):
    sq=0
    val=0
    for i in range (1,n+1):
        sq=sq+(i*i)
        val=val+i
    diff=(val*val)-sq
    return diff
           

# take input from the user
t=int(input())
for j in range(0,t):
    num = int(input())
    print difference(num)

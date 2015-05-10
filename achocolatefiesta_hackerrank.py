import math

a = int(raw_input())
list1=raw_input()
print list1
output=list();
for i in range(1,a+1):
    print len(list1)
    x = list1(i)
    print x
    if x not in output:
        output.append(x)
print output
distinct = len(output);
print distinct
print int(math.pow(2,distinct)-1)%1000000007

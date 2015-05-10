n=int(raw_input())
while n>0:
    n-=1
    m=int(raw_input())
    m=m%6
    temp=0
    if m==0:
        temp=3
    if m>0:
        m=m-1
        temp=1
    if m>0:
        m=m-2
        temp=2
    if m>0:
        m=m-3
        temp=3
    print temp
        

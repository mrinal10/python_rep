t=int(raw_input())
while t>0 :
    t=t-1
    index, N=raw_input().split()
    index, N=[int(index), int(N)]
    while N>0 :
        N=N-1
        if index==0 :
            index=1
        elif index==1 :
            index=0
        elif index==2 :
            index=1
    print(index)

t=int(raw_input())
while t>0:
    t-=1
    n, x=raw_input().split()
    n=int(n)
    x=int(x)
    line=raw_input()
    pricelist = []
    p=line.split(' ')
    while len(pricelist) < maxLengthList:
        item = int(x[len(pricelist)])
        pricelist.append(item)
    pricelist.sort()
    jk=pricelist[0]
    count=0
    if len(pricelist)==1:
        count=1
    else:
        for i in range (1,len(pricelist)):
            if jk!=pricelist[i]:
                count+=1
                jk=pricelist[i]
        if pricelist[len(pricelist)-1]!=pricelist[len(pricelist)-2]:
            count+=1
    if x==count:
        print "Perfect husband"
    else:
        print "Lame husband"

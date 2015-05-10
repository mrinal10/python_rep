catlist = [] 
callist = []
maxLengthList = int(raw_input())

line=raw_input()
x = line.split(' ')
while len(catlist) < maxLengthList:
    item = int(x[len(catlist)])
    catlist.append(item)
catlist.sort()
#print catlist

line=raw_input()
x = line.split(' ')
while len(callist) < maxLengthList:
    item = int(x[len(callist)])
    callist.append(item)
callist.sort()
#print callist
    
tot=0
for i in range(0,maxLengthList):
	tot=tot+(callist[i]*catlist[i])
print tot

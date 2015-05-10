n=int(raw_input())
s=[]
for i in range(0,n):
    s.append(raw_input())
        

for i in range(0,n-1):
    ss = s[i]
    ss = ss[::-1]
    for j in range(i+1,n):
        ss2=s[j]
        if ss==ss2:
            leng = len(ss)
            print leng
            print ss[((leng+1)/2)-1]
            

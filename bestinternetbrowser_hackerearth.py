tc=int(raw_input())
while(tc>0):
    tc=tc-1
    s=raw_input()
    a, e, i, o, u=s.count('a'), s.count('e'),  s.count('o'),  s.count('i'),  s.count('u')
    lens=len(s)
    ab=lens-3-a-e-i-o-u
    print str(ab)+ "/" +str(lens)

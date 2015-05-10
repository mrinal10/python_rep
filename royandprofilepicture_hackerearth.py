l=int(raw_input())
tc=int(raw_input())

while(tc>0):
    tc=tc-1
    w, h=raw_input().split()
    w, h= [int(w), int(h)]
    if w==h and w>=l:
        print("ACCEPTED")
    elif w>=l and h>=l:
        print("CROP IT")
    elif w<l or h<l:
        print("UPLOAD ANOTHER")

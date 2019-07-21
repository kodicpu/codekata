ran=input().split()
ran[0]=int(ran[0])
ran[1]=int(ran[1])
if ran[0]<=100000 and ran[1]<=100000:
    for i in range(ran[0]+1,ran[1]):
        if i % 2!=0:
            print(i,end=" ")

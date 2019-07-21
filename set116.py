ran=input().split()
ran[0]=int(ran[0])
ran[1]=int(ran[1])
for i in range(ran[0]+1,ran[1]):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print (i,end=" ")

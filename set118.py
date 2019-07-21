def arm(n):
    temp=n
    res=0
    while(n>0):
        res=res+(n%10)**3
        n=n//10
    if res==temp:
        return 1
    else:
        return 0
interval=input().split()
interval[0]=int(interval[0])
interval[1]=int(interval[1])
if interval[0]<=100000 and interval[1]<=100000:
    for i in range(interval[0]+1,interval[1]):
        if arm(i)==1:
            print (i,end=" ")

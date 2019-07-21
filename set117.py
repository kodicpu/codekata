def arm(n):
    temp=n
    res=0
    while(n>0):
        r=n%10
        res=res+(r*r*r)
        n=int(n/10)
    if res==temp:
        return 1
    else:
        return 0
number=int(input())
if number<=100000:
    if arm(number)==1:
        print ("yes")
    else:
        print ("no")

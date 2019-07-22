n=int(input())
if n>=1 and n<=1000:
    array=[i for i in input().split()]
    array.sort()
    for i in array:
        print (i,end=" ")

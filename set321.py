n,a,d=input().split()
n=int(n)
a=int(a)
d=int(d)
result=0
temp=a
for i in range(n):
    result+=temp
    temp=temp+d
print (result)

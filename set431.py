strdata=input()
length=len(strdata)
count=0
for i in range(length):
    if strdata[i].isalpha():
        count+=1
print (count)

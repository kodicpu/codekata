data=input()
leng=len(data)
count=0
for i in data:
  if i.isnumeric()==True:
    count+=1
print(count)

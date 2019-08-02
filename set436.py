x,count = input(),0
for i in x:
  if (ord(i) not in range(65,90)) and (ord(i) not in range(97,123)) and (ord(i)!=32) and (ord(i) not in range(47,58)):
    count+=1
print(count)

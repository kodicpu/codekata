number=input()
try:
    if " " in number:
        raise Exception('a space found')
    if '.' in number:
        val=float(number)
        print("Yes")
    else:
        val=int(number)
        print ("Yes")
    
except ValueError:
    print ("No")

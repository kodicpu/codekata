try:
  a=input()
  a=int(a)
  if a>0:
    print ("Positive")
  elif a<0:
    print ("Negative")
  else:
    print ("Zero")
except ValueError:
  print ("non numeric data found")
